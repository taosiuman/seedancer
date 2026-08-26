# Seedancer v7.0.0 — AIGC 影视导演操作系统

<p align="center">
  <a href="../README.md"><b>English</b></a> · <a href="README-cn.md">中文</a>
</p>

<div align="center">

**从剧本到成片的端到端智能制片管线**

[![版本](https://img.shields.io/badge/version-7.0.0-blue.svg)](https://github.com/taosiuman/seedancer/releases)
[![许可](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![ClawHub](https://img.shields.io/badge/ClawHub-seedancer-orange.svg)](https://clawhub.ai/skills/seedancer)
[![Seedance](https://img.shields.io/badge/Seedance-2.5-purple.svg)](https://seedance.ai)

**[快速开始](#快速开始)** · **[核心模块](#核心模块)** · **[使用示例](#使用示例)** · **[更新日志](CHANGELOG.md)**

</div>

---

##  简介

**Seedancer** 不是一个提示词生成器，而是一套**导演级 AI 影视制片操作系统**——完整的导演工作流引擎。

它将剧本自动转化为生产级视频提示词，内置 **12 大门控系统**、**10 大核心模块**、**30+ 参考文档**，覆盖从项目预生产到最终交付的全流程自动化。

### ✨ v7.0.0 新增

整合三大开源技能，新增 **5 大导演系统**：

| 系统 | 能力 |
|------|------|
| 🎭 **场景原型路由** | 9 种场景原型自动识别，决策树驱动 |
| 📷 **摄影机-情绪同步** | 6 种情绪 → 摄影机类型自动映射 |
|  **表演微节拍目录** | 情绪分解为具体肌肉/呼吸/眼神运动 |
|  **光源规则系统** | practicals-only 铁律 + 60:30:10 色彩规则 |
| 📋 **JSON API 输出模式** | 结构化双语输出，可接入自动化管线 |

---

##  核心模块

### 预生产管线 (P0–P2)

| 阶段 | 产出 |
|------|------|
| **P0** 项目接收 | 项目基准卡 |
| **P0A** 十项剧本解析 | 世界观 + 人物小传 + 情绪曲线图 |
| **P1** 创作基准 | 摄影/色彩/声音圣经 |
| **P2a** 角色资产 | 9:16 确认稿 + 16:9 设定板 |
| **P2b** 关键道具 | 3:4 道具母板 |

### 五大硬门系统 (v6.0.0)

确保提示词可执行性的硬性约束：

- **台词容量预检** — 语速四档 × 标点停顿 × 反应留白
- **分组硬门** — 模型时长上限 + 承接等式 + 组尾稳定态
- **镜头密度四道门** — Smin / Bmin / 新反馈 / Gmax 阈值
- **运镜设计系统** — 叙事功能表 + 三要素 + 运镜主轴
- **输出格式硬门** — 自然段写法 + 禁止代词 + 媒介翻译表

### 五大导演系统 (v7.0.0)

#### 🎭 场景原型路由

自动识别 9 种场景原型，每种有独立的摄影机焦点和空间动态：

- **动作类**：追逐 → 对决 → 冲击
- **通用类**：旅程 → 氛围 → 揭示
- **对话类**：对峙 → 审讯 → 谈判

#### 📷 摄影机-情绪同步

摄影机是焦点角色的情绪分身：

| 情绪 | 摄影机类型 | 效果 |
|------|-----------|------|
| 愤怒/紧张 | 手持呼吸，不稳定 | 画面有明显呼吸式漂移 |
| 平静/控制 | 手持呼吸，平滑 | 极细微规律的呼吸式微动 |
| 悲伤/脆弱 | 手持，缓慢低位 | 呼吸节奏放慢，轻微下沉感 |
| 震惊/揭示 | 静止 + 慢推/慢拉 | 严格静止，0.5s 后极缓慢移动 |
| 动作 | 60fps 180° 快门 | 流畅运动，快门范围内运动模糊 |
| 终拍/判词 | 俯拍定格 | 严格正上方俯拍，0.3–0.5s freeze |

#### 🎬 表演微节拍目录

**铁律**：泛化情绪 = 坏提示词；具体肌肉/呼吸/眼神 = 好提示词。

| 情绪 | 微节拍 |
|------|--------|
| 愤怒 | 咬肌搏动、颈动脉脉搏、鼻翼扩张、瞳孔收缩 |
| 焦虑 | 喉结吞咽、台词前短促浅吸气、舔润下唇 |
| 悲伤 | 眼角外缘下垂、湿润带眼神光但不流泪 |
| 震惊 | 身体冻结 0.3–0.5s、瞳孔扩张、延迟急促鼻吸气 |

每句台词三节拍：前节拍（吞咽/吸气）+ 中强调 + 后节拍（0.5s 凝视）。

#### 💡 光源规则

**Practicals-only 铁律**——严格仅使用场景内实际存在的光源：

- 摄影机始终在人物的阴影侧（shadow side）拍摄
- 色彩 60:30:10 — 主色/辅色/点缀色
- 全程大气薄雾 haze，禁止可见光束（god rays）
- 场景变体：夜景/地下基地/日外/夜外/暖室内各有独立灯光条款

#### 📋 JSON API 输出模式

可选结构化双语 JSON 输出，适配自动化管线：

```json
[
  {"lang": "en", "prompt": "Style & Mood: ...\nNarrative: ...\nDynamic: ...\nStatic: ...\nAudio: ..."},
  {"lang": "zh", "prompt": "风格与氛围：...\n叙事：...\n动态：...\n静态：...\n音频：..."}
]
```

中文硬上限 1800 字符，含完整反垃圾词汇表。

### 支持模型

| 模型 | 类型 | 最大时长 | 最佳场景 |
|------|------|---------|---------|
| Seedance 2.5 | 视频 | 30s | 复杂动作与长对白 |
| Seedance 2.0 | 视频 | 15s | 高性价比通用 |
| Kling 3.0 | 视频 | 15s | 动作与物理交互 |
| Veo 3 | 视频 | 8s | 短氛围镜 |
| GPT Image 2 | 图像 | — | 极致照片真实感 |
| Seedream 5.0 Pro | 图像 | — | 图层分离与商业视觉 |

### 12 门控路由

```
门控 0  — 预生产检测
门控 0A — 预生产阶段
门控 1  — 接收
门控 2  — 来源核查
门控 3  — 模式选择
门控 4  — 能力检查
门控 5  — 参考映射
门控 6  — 安全门控
门控 7  — 提示词构建
门控 7A — 台词容量预检
门控 7B — 分组与密度门控
门控 8  — 质量检查
```

---

## 🚀 快速开始

### 安装

```bash
clawhub install seedancer
```

### 完整项目流程

```
用户：读取我的剧本，帮我完成从剧本解析到角色资产到分镜的全流程

系统：
1. P0  项目接收 → 输出项目基准卡
2. P0A 十项剧本解析 → 世界观 + 人物小传 + 情绪曲线图
3. P1  创作基准 → 摄影/色彩/声音圣经
4. P2a 角色资产 → 9:16 确认稿 + 16:9 设定板
5. P2b 关键道具 → 3:4 道具母板
6. 制片管线 → 12 门控路由 → 分镜生成
```

### 单镜头快速生成

```
用户：帮我拍一个赛博朋克风格的雨夜街道镜头，15秒，16:9

系统：跳过 P0-P2 → 门控 1 → 场景路由（氛围类）
      → 摄影机-情绪同步（忧郁 → 手持缓慢低位）
      → 双语提示词输出
```

### JSON API 自动化

```bash
curl -X POST https://api.clawhub.ai/v1/skills/seedancer/execute \
  -H "Content-Type: application/json" \
  -d '{"input": "雨夜，赛博朋克街道，女主角悲伤",
        "options": {"output_mode": "json", "duration": 15, "aspect_ratio": "16:9"}}'
```

---

## 📁 参考文档 (30+)

```
references/
├── scene-prototypes.md          # 场景原型路由 (v7)
├── camera-emotion-sync.md       # 摄影机-情绪同步 (v7)
├── performance-micro-beats.md   # 表演微节拍目录 (v7)
├── json-api-mode.md             # JSON API 输出模式 (v7)
├── lighting-rules.md            # 光源规则系统 (v7)
── dialogue-capacity.md         # 台词容量预检
├── grouping-density.md          # 分组硬门 + 镜头密度
├── camera-design.md             # 运镜设计系统
── output-format.md             # 输出格式硬门
├── story-analysis.md            # P0A 十项剧本解析
├── emotion-curve.md             # 情绪曲线可视化
├── creative-baseline.md         # 创作基准
├── character-assets.md          # 角色资产
├── prop-assets.md               # 关键道具
├── cinedance-video-prompt.md    # CINEDANCE 16-block
├── lira-image-prompt.md         # LIRA 4-D
├── acting-performance.md        # ACTING 表演系统
── geo-spatial-layout.md        # GEO 空间锁定
├── style-prefix.md              # Style Prefix
├── ai-director.md               # AI 导演方法论
├── failure-codes.md             # 失败诊断（6 类 33 码）
└── ...
```

---

## 📜 版本历史

| 版本 | 日期 | 亮点 |
|------|------|------|
| **v7.0.0** | 2026-08-24 | 5 大导演系统：场景路由、摄影机-情绪同步、微节拍、光源规则、JSON API |
| **v6.0.0** | 2026-08-24 | 5 大硬门系统：台词容量、分组、密度、运镜设计、输出格式 |
| **v5.0.0** | 2026-08-14 | P0-P2 预生产管线 |
| **v4.1.0** | 2026-08-13 | CINEDANCE / LIRA / ACTING / GEO / Style Prefix 整合 |
| **v4.0.0** | 2026-08-09 | Seedance 2.5 全面适配 |
| **v3.0.0** | 2026-06-22 | 架构级重构 |

---

## 🤝 致谢

- **shotlist-builder** — 场景原型路由 + 摄影机-情绪同步 + 表演微节拍
- **seedance-director** — JSON API 输出模式
- **hellgrind** — ACTING / CINEDANCE / LIRA
- **ifeihong/aigc-film-studio** — CINEDANCE / LIRA / ACTING / GEO / Style Prefix
- **chaoge-assets-trial** — P0-P2 预生产管线
- **Elio_AIGC** — 五大硬门系统
- **Emily2040/seedance-2.0** — 模型机制 + 反空洞词典

完整归属声明见 [LICENSE](LICENSE)。

---

## 🔗 链接

**GitHub** · [taosiuman/seedancer](https://github.com/taosiuman/seedancer)  
**ClawHub** · [seedancer](https://clawhub.ai/skills/seedancer)  
**问题反馈** · [Report a bug](https://github.com/taosiuman/seedancer/issues)

---

<div align="center">

** Seedancer v7.0.0 — 从剧本到成片的端到端智能制片管线**

*Made with ❤️ for AI filmmakers*

</div>
