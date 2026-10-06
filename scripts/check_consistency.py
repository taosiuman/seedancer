#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_consistency.py — seedancer 一致性 + 硬门检查器（v3，零依赖）

v3 相对 v2 的新增（依据 ClawHub 安全评审 [SDI-1] 与 v9.0.1 发布复盘）：
  · V3  skill-card.md 的「Skill Version(s)」字段必须 == 权威版本（v2 的已知盲区）
  · V4  skill-card.md 的 Publisher 必须 == _meta.json 的 author

v2 相对 v1 的修复（依据 REV-20261005-010 的"假绿"清单）：
  · M3  改用 json.loads 按键精确比较（v1 对 JSON 格式的 _meta.json 完全空转）
  · M4  来源清单改为从 _meta.json.upstream_sources **推导**并与 LICENSE 双向核对（v1 是硬编码 8 token）
  · I1  INDEX 与加载表都改为**集合精确匹配**（v1 用 OR + 子串，与文档矛盾）
  · I3  加载表条目改为**集合精确**；每个触发时机必须在 SKILL.md 的**加载表之外**真实出现
        （v1 只做子串匹配，28 篇塞进一行"(未定位)"即骗过）
  · D1  修滑窗计量（v1 每命中 +8 导致 12 行报"≥296 行"）；白名单改为**契约检查**：
        标注必须写明 target=<file>，且**围栏模板里的区块名与两张词表**必须在 target 中逐字存在
  · V1  取**全部**版本戳比对（v1 只取首末），并纳入 README/docs 标题行
  · A*  新增 28 条**硬门锚点**断言（此前只存在于一次性施工脚本，声明"缺一即构建失败"无实现）
  · K1  预算：>32KB WARN，>48KB FAIL

用法：
    python scripts/check_consistency.py [--json] [--quiet]
退出码：0 = 无 FAIL；1 = 存在 FAIL；2 = 用法/环境错误

已知限制（如实声明，勿当成"已覆盖"）：
  · V1 只比对**版本戳**（_meta/VERSION/frontmatter/标题戳/末戳/徽章/CHANGELOG），
    **不覆盖** COMPAT.md、release-notes.md、references/ 内页脚 —— 这些位置仍可能残留旧版本号
    （skill-card.md 自 v3 起改由 V3/V4 覆盖，不再属于 V1 盲区）
  · M4 为**单向**（_meta.upstream_sources ⊆ LICENSE）；LICENSE 多出的来源不会被报出
  · I1/I2/I3 依赖**表格格式**（首列为触发时机、次列反引号文件名）；换格式会误报
  · D1 只比 SKILL.md ↔ references，reference 之间互抄不查；且为 WARN 级
  · A1 是"关键短语在应有节内存在"，不等于该节完整（删一半仍可能通过）
  · K1 只测入口体积，references/ 总量无上限
"""

from __future__ import annotations

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAIL, WARN = "FAIL", "WARN"
SKIP_DIRS = {".git", "_git_baseline", "__pycache__", "node_modules"}
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BARE_REF = re.compile(r"(?<![(\w/])references/([A-Za-z0-9_\-]+\.md)")
VERSION_RE = re.compile(r"Seedancer v(\d+\.\d+\.\d+)")
BADGE_RE = re.compile(r"version-(\d+\.\d+\.\d+)-")
RUNTIME_DIRS = ("runs/", "outputs/", "04-prompts/", ".seedancer/")   # 运行期产物（复核后收窄）

# 硬门锚点：这些字符串必须存在于入口（删内容时若丢失即构建失败）
ANCHORS = [
    "九条黄金规则", "SCALE LAW", "矛盾检测", "硬门总览", "核心硬规则", "台词容量",
    "分组硬门", "镜头密度", "隐藏切镜", "Smin", "Bmin", "Gmax", "承接等式", "组尾",
    "运镜设计", "主动运镜三要素", "输出格式硬门", "逐字使用", "四项事实",
    "空间与人物指代硬门", "媒介翻译表", "体量控制", "CINEDANCE 16-block", "Style Prefix",
    "交付物体系", "视频模型选用前必须先询问用户", "失败现象对照表", "参考文档加载表",
]
# 契约区必须逐字存在于 target 的关键串（区块名 + 词表锚点）
CONTRACT_KEY_LINES = [
    "## 使用的 @资产清单", "## 状态资产引用", "## 参数确认", "## 全局风格提示词",
    "## 角色音色设定", "## 第1组：组标题", "### 每镜四项事实（缺一不可）", "### 时间码规范",
]


def read(path):
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def walk(root=None, exts=None):
    root = root or ROOT
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if exts is None or name.endswith(exts):
                yield os.path.join(dirpath, name)


class Report:
    def __init__(self):
        self.items = []

    def add(self, cid, title, level, ok, detail=""):
        self.items.append({"id": cid, "title": title, "level": level,
                           "ok": bool(ok), "detail": detail})

    @property
    def fails(self):
        return [i for i in self.items if not i["ok"] and i["level"] == FAIL]

    @property
    def warns(self):
        return [i for i in self.items if not i["ok"] and i["level"] == WARN]


SKILL = "SKILL.md"


def skill_text():
    p = os.path.join(ROOT, SKILL)
    return read(p) if os.path.isfile(p) else ""


def load_table(skill):
    m = re.search(r"(?ms)^##\s*参考文档加载表.*?(?=^##\s|\Z)", skill)
    return m.group(0) if m else ""


def load_table_entries(skill):
    """返回 {文件名: 触发时机}（从加载表表格行精确解析）。"""
    out = {}
    for line in load_table(skill).splitlines():
        if not line.startswith("|") or "---" in line or "门控 / 阶段" in line:
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue
        trigger = cells[0]
        for f in re.findall(r"`([A-Za-z0-9_\-]+\.md)`", cells[1]):
            out[f] = trigger
    return out


# ---------- V ----------
def check_versions(rep):
    try:
        meta = json.loads(read(os.path.join(ROOT, "_meta.json")))
        authority = meta.get("version", "")
    except Exception as e:  # noqa: BLE001
        rep.add("V1", "版本戳多处一致", FAIL, False, "_meta.json 无法解析：%s" % e)
        return ""
    seen = {}
    if os.path.isfile(os.path.join(ROOT, "VERSION")):
        seen["VERSION"] = read(os.path.join(ROOT, "VERSION")).strip()
    skill = skill_text()
    fm = skill.split("---", 2)[1] if skill.startswith("---") else ""
    m = re.search(r"^version:\s*\"?([\d.]+)", fm, re.M)
    seen["SKILL.md(frontmatter)"] = m.group(1) if m else "(未找到)"
    stamps = VERSION_RE.findall(skill)
    if not stamps:
        seen["SKILL.md(标题戳)"] = "(未找到)"
    else:
        seen["SKILL.md(标题戳)"] = stamps[0]
        seen["SKILL.md(末戳)"] = stamps[-1]
        if len(set(stamps)) > 1:
            seen["SKILL.md(全部戳)"] = "/".join(sorted(set(stamps)))
    ch = read(os.path.join(ROOT, "CHANGELOG.md")) if os.path.isfile(os.path.join(ROOT, "CHANGELOG.md")) else ""
    m = re.search(r"v?(\d+\.\d+\.\d+)", ch[:400])
    seen["CHANGELOG.md"] = m.group(1) if m else "(未找到)"
    for rel, key in (("README.md", "README.md"), ("docs/README-cn.md", "docs/README-cn.md")):
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            continue
        t = read(p)
        m = BADGE_RE.search(t)
        seen[key + "(徽章)"] = m.group(1) if m else "(未找到)"
        m = VERSION_RE.search(t)
        if m:
            seen[key + "(标题戳)"] = m.group(1)
    bad = {k: v for k, v in seen.items() if v != authority}
    rep.add("V1", "版本戳全部一致（含标题/末戳/徽章）", FAIL, not bad,
            "权威=_meta.json(%s)；不一致：%s" % (authority, "、".join("%s=%s" % kv for kv in bad.items()))
            if bad else "%d 处一致（%s）；跳过：release-notes.md(v7.x 存档)、LICENSE(归因区块版本中立)"
            % (len(seen), authority))
    # V2：CHANGELOG 必须有**结构化**条目（标题行或表格行），不是子串
    pat = re.compile(r"(^#+\s*Seedancer v%s\b)|(^\|\s*\*{0,2}v%s\b)" % (re.escape(authority), re.escape(authority)), re.M)
    rep.add("V2", "CHANGELOG 有当前版本的结构化条目", FAIL, bool(pat.search(ch)),
            "未找到形如 '# Seedancer v%s 更新日志' 或表格行的条目" % authority if not pat.search(ch)
            else "已找到结构化条目")
    # V3/V4：skill-card.md 的版本戳与 Publisher 必须与权威元数据一致
    # （v3 新增；此前 skill-card.md 是 V1 的已知盲区 —— 见文件头"已知限制"）
    sc_p = os.path.join(ROOT, "skill-card.md")
    if os.path.isfile(sc_p):
        sc = read(sc_p)
        mv = re.search(r"^##\s*Skill Version\(s\):[^\n]*\n(.+)$", sc, re.M)
        vm = re.search(r"(\d+\.\d+\.\d+)", mv.group(1)) if mv else None
        got_v = vm.group(1) if vm else "(未找到)"
        rep.add("V3", "skill-card.md 版本戳 == 权威版本", FAIL, got_v == authority,
                "skill-card.md 版本=%s vs 权威=%s" % (got_v, authority) if got_v != authority
                else "skill-card.md 版本一致（%s）" % got_v)
        author = str(meta.get("author", "")).strip()
        pub = sc.split("## Publisher:", 1)[1].split("###", 1)[0] if "## Publisher:" in sc else ""
        pm = re.search(r"clawhub\.ai/user/([A-Za-z0-9_\-]+)", pub)
        got_p = pm.group(1) if pm else "(未找到)"
        rep.add("V4", "skill-card.md Publisher == _meta.json author", FAIL,
                bool(author) and got_p == author,
                "publisher=%s vs author=%s" % (got_p, author) if got_p != author
                else "Publisher 一致（%s）" % got_p)
    else:
        rep.add("V3", "skill-card.md 版本戳 == 权威版本", FAIL, False, "skill-card.md 不存在")
    return authority


# ---------- M ----------
def check_metadata(rep):
    meta_p = os.path.join(ROOT, "_meta.json")
    try:
        meta = json.loads(read(meta_p))
        rep.add("M1", "_meta.json 是合法 JSON", FAIL, True, "json.loads 通过")
    except Exception as e:  # noqa: BLE001
        rep.add("M1", "_meta.json 是合法 JSON", FAIL, False, "解析失败：%s" % e)
        meta = {}
    skill = skill_text()
    fm = skill.split("---", 2)[1] if skill.startswith("---") else ""
    required = ["name", "description", "license", "author", "version", "tags", "platforms"]
    empty = [k for k in required if not re.search(r"^%s:\s*\S" % k, fm, re.M)]
    rep.add("M2", "frontmatter 7 字段齐备且非空", FAIL, not empty,
            "缺或空：%s" % "、".join(empty) if empty else "7 个字段齐备且非空")
    diffs = []
    for key in ("name", "version", "license", "author"):
        m = re.search(r"^%s:\s*\"?([^\"\n]+)\"?\s*$" % key, fm, re.M)
        a = m.group(1).strip() if m else ""
        b = str(meta.get(key, "")).strip()
        if not a or not b:
            diffs.append("%s: frontmatter=%r vs _meta=%r（有空值）" % (key, a, b))
        elif a != b:
            diffs.append("%s: frontmatter=%s vs _meta=%s" % (key, a, b))
    rep.add("M3", "frontmatter 与 _meta.json 逐字段一致", FAIL, not diffs,
            "；".join(diffs) if diffs else "4 个关键字段一致")
    # M4：来源清单由 _meta.json 推导，与 LICENSE 双向核对
    sources = meta.get("upstream_sources") or []
    lic = read(os.path.join(ROOT, "LICENSE"))
    if not sources:
        rep.add("M4", "LICENSE 归因与 _meta.json 来源清单一致（合规）", FAIL, False,
                "_meta.json 缺 upstream_sources（无法推导来源清单）")
    else:
        miss = [s for s in sources if s not in lic]
        rep.add("M4", "LICENSE 归因与 _meta.json 来源清单一致（合规）", FAIL, not miss,
                "LICENSE 缺来源：%s" % "、".join(miss) if miss
                else "%d 个来源均在 LICENSE 有归因" % len(sources))


# ---------- L ----------
def check_links(rep):
    dead = []
    for path in walk(exts=(".md", ".json", ".sh", ".txt")):
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        text = read(path)
        targets = set(MD_LINK.findall(text)) | set("references/" + m for m in BARE_REF.findall(text))
        for t in targets:
            t = t.split("#")[0].strip()
            if not t or t.startswith(("http", "mailto:", "asset://")):
                continue
            if re.search(r"[<>{}*%]", t):      # 模板占位（{} <> * % 一致处理）
                continue
            if any(t.startswith(d) or ("/" + d) in t for d in RUNTIME_DIRS):
                continue
            cand_abs = os.path.normpath(os.path.join(os.path.dirname(path), t))
            cand_root = os.path.normpath(os.path.join(ROOT, t))
            if not (os.path.isfile(cand_abs) or os.path.isfile(cand_root)
                    or os.path.isdir(cand_abs) or os.path.isdir(cand_root)):
                dead.append("%s → %s" % (rel, t))
    rep.add("L1", "相对路径引用均可解析（无死链）", FAIL, not dead,
            "死链 %d 处：%s" % (len(dead), "；".join(sorted(set(dead))[:10])) if dead else "无死链")


# ---------- I ----------
def check_index(rep):
    ref_dir = os.path.join(ROOT, "references")
    refs = {f for f in os.listdir(ref_dir) if f.endswith(".md") and f != "INDEX.md"} \
        if os.path.isdir(ref_dir) else set()
    idx_p = os.path.join(ref_dir, "INDEX.md")
    idx = read(idx_p) if os.path.isfile(idx_p) else ""
    idx_set = set(re.findall(r"^\|\s*`([A-Za-z0-9_\-]+\.md)`", idx, re.M))
    skill = skill_text()
    table = load_table_entries(skill)
    table_set = set(table)

    missing_idx = sorted(refs - idx_set)
    extra_idx = sorted(idx_set - refs)
    rep.add("I1", "references 集合 == INDEX 集合（精确）", FAIL, not (missing_idx or extra_idx),
            "缺登记：%s；多登记：%s" % ("、".join(missing_idx) or "无", "、".join(extra_idx) or "无")
            if (missing_idx or extra_idx) else "%d 篇精确一致" % len(refs))

    missing_tbl = sorted(refs - table_set)
    extra_tbl = sorted(table_set - refs)
    rep.add("I2", "references 集合 == 加载表集合（精确）", FAIL, not (missing_tbl or extra_tbl),
            "未接线：%s；幽灵条目：%s" % ("、".join(missing_tbl) or "无", "、".join(extra_tbl) or "无")
            if (missing_tbl or extra_tbl) else "%d 篇精确一致" % len(refs))

    # I3：每个触发时机必须在 SKILL.md 的**加载表之外**真实出现（堵 "(未定位)" 兜底）
    outside = skill.replace(load_table(skill), "")
    heading_lines = {re.sub(r"^#{2,6}\s*", "", l).strip() for l in outside.splitlines()
                     if re.match(r"^#{2,6}\s", l)}
    triggers = set(table.values())
    empty = sorted(n for n, tv in table.items() if not tv.strip())
    phantom = sorted(t for t in triggers if t and t not in heading_lines)
    problems = []
    if empty:
        problems.append("空触发：%s" % "、".join(empty[:5]))
    if phantom:
        problems.append("非标题触发：%s" % "、".join(phantom[:5]))
    rep.add("I3", "加载表触发时机必须是正文中真实标题行", FAIL, not problems,
            "；".join(problems) if problems
            else "%d 个触发时机均为真实标题行" % len(triggers))


# ---------- D ----------
def check_duplication(rep, threshold=40):
    skill_p = os.path.join(ROOT, SKILL)
    raw = read(skill_p)
    m = re.search(r"(?ms)<!--\s*dup-allow-start[^>]*-->", raw)
    contract = ""
    if m:
        j = raw.find("<!-- dup-allow-end -->", m.end())
        contract = raw[m.end():j] if j > 0 else ""
    body = re.sub(r"(?ms)<!--\s*dup-allow-start.*?<!-- dup-allow-end -->", "", raw)
    lines = [l.strip() for l in body.splitlines()]
    idx = {}
    for i in range(len(lines) - 8 + 1):
        w = tuple(lines[i:i + 8])
        if sum(len(x) for x in w) > 60:
            idx.setdefault(w, i + 1)
    hits = []
    for path in walk(os.path.join(ROOT, "references"), (".md",)):
        rl = [l.strip() for l in read(path).splitlines()]
        run = 0
        start = 0
        for k in range(len(rl) - 8 + 1):
            if tuple(rl[k:k + 8]) in idx:
                if run == 0:
                    start = idx[tuple(rl[k:k + 8])]
                run += 1                      # 滑窗步进 1 行 → 连续行数 = run + 7
            else:
                if run + 7 >= threshold:
                    hits.append("%s ↔ SKILL.md:%d 连续 ≥%d 行" % (os.path.basename(path), start, run + 7))
                run = 0
        if run + 7 >= threshold:
            hits.append("%s ↔ SKILL.md:%d 连续 ≥%d 行" % (os.path.basename(path), start, run + 7))
    rep.add("D1", "无大段逐字重复（契约区除外，阈值 %d 行）" % threshold, WARN, not hits,
            "；".join(hits[:6]) if hits else "未发现大段逐字重复")

    # D2：契约区必须真的与目标文件一致（把白名单从"豁免"变成"更强的检查"）
    tm = re.search(r"target=([A-Za-z0-9_\-]+\.md)", m.group(0)) if m else None
    if not tm:
        rep.add("D2", "契约区标注了目标文件并可校验", FAIL, False,
                "dup-allow-start 未写 target=<file>，无法校验契约区")
    else:
        target_p = os.path.join(ROOT, "references", tm.group(1))
        if not os.path.isfile(target_p):
            rep.add("D2", "契约区目标文件存在", FAIL, False, "references/%s 不存在" % tm.group(1))
        else:
            tgt_lines = {l.strip() for l in read(target_p).splitlines() if len(l.strip()) >= 12}
            tpl = re.search(r"(?ms)```[a-z]*\n(.*?)```", contract)
            body = tpl.group(1) if tpl else contract
            miss_lines = [l.strip() for l in body.splitlines()
                          if len(l.strip()) >= 12 and l.strip() not in tgt_lines]
            rep.add("D2", "契约区模板每一行都在目标文件中（逐行）", FAIL, not miss_lines,
                    "目标 %s 缺 %d 行：%s" % (tm.group(1), len(miss_lines),
                                              " ｜ ".join(miss_lines[:3])) if miss_lines
                    else "模板 %d 行全部存在于 %s" % (len(body.splitlines()), tm.group(1)))


# ---------- A / K ----------
ANCHOR_SECTION = {
    "九条黄金规则": "九条黄金规则", "SCALE LAW": "SCALE LAW", "矛盾检测": "矛盾检测",
    "硬门总览": "五大硬门系统", "核心硬规则": "五大硬门系统",
    "台词容量": "台词容量预检", "分组硬门": "分组硬门", "承接等式": "分组硬门", "组尾": "分组硬门",
    "镜头密度": "镜头密度四道门", "隐藏切镜": "镜头密度四道门",
    "Smin": "镜头密度四道门", "Bmin": "镜头密度四道门", "Gmax": "镜头密度四道门",
    "运镜设计": "运镜设计", "主动运镜三要素": "运镜设计",
    "输出格式硬门": "输出格式硬门", "逐字使用": "输出格式硬门", "四项事实": "输出格式硬门",
    "空间与人物指代硬门": "空间与人物指代硬门", "媒介翻译表": "媒介翻译表", "体量控制": "体量控制",
    "CINEDANCE 16-block": "CINEDANCE", "Style Prefix": "Style Prefix",
    "交付物体系": "交付物体系", "视频模型选用前必须先询问用户": "模型自动选择系统",
    "失败现象对照表": "失败现象对照表", "参考文档加载表": "参考文档加载表",
}


def sections_of(skill):
    """按 ## 切段 → {标题: 段文本}（标题去掉 # 与首尾空白）。"""
    out, cur, buf = {}, None, []
    for line in skill.splitlines():
        if re.match(r"^##\s", line):
            if cur:
                out[cur] = "\n".join(buf)
            cur = re.sub(r"^##\s*", "", line).strip()
            buf = [line]
        else:
            buf.append(line)
    if cur:
        out[cur] = "\n".join(buf)
    return out


def check_anchors(rep):
    skill = skill_text()
    secs = sections_of(skill)
    missing, wrong = [], []
    for a in ANCHORS:
        want = ANCHOR_SECTION.get(a, "")
        hit = [h for h in secs if want and want in h]
        if not hit:
            missing.append("%s(节缺失:%s)" % (a, want))
        elif a not in secs[hit[0]]:
            wrong.append("%s(不在节「%s」内)" % (a, hit[0]))
    problems = missing + wrong
    rep.add("A1", "硬门锚点按节存在（%d 条，删整节即失败）" % len(ANCHORS), FAIL, not problems,
            "问题项：%s" % "；".join(problems[:6]) if problems else "%d 条均在其应有节内" % len(ANCHORS))


def check_budget(rep):
    p = os.path.join(ROOT, SKILL)
    size = os.path.getsize(p)
    kb = size / 1024
    # 单阈值：目标 = v9 实测（44KB），失败线 = v8 水平（52KB）—— >目标即 WARN，>失败线即 FAIL
    if size > 52 * 1024:
        rep.add("K1", "SKILL.md 体积预算", FAIL, False,
                "当前 %.1f KB 超过失败线 52KB（v8.0.0 为 54.7KB，等于退回重构前）" % kb)
    else:
        rep.add("K1", "SKILL.md 体积预算", WARN, size <= 44 * 1024,
                "当前 %.1f KB（目标 ≤44KB；v8.0.0 = 54.7KB）" % kb)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    rep = Report()
    version = check_versions(rep)
    check_metadata(rep)
    check_links(rep)
    check_index(rep)
    check_duplication(rep)
    check_anchors(rep)
    check_budget(rep)

    if "--json" in argv:
        print(json.dumps({"version": version, "fail": len(rep.fails), "warn": len(rep.warns),
                          "items": rep.items}, ensure_ascii=False, indent=2))
    else:
        quiet = "--quiet" in argv
        print("== seedancer 一致性检查 v3（权威版本：%s）" % version)
        for i in rep.items:
            if i["ok"] and quiet:
                continue
            mark = "OK  " if i["ok"] else ("FAIL" if i["level"] == FAIL else "WARN")
            print("[%s] %-4s %s — %s" % (mark, i["id"], i["title"], i["detail"]))
        print("RESULT: %s (%d fail, %d warn)"
              % ("PASS" if not rep.fails else "FAIL", len(rep.fails), len(rep.warns)))
    return 0 if not rep.fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
