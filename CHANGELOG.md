# Seedancer v7.0.0 更新日志

_发布日期：2026-08-24_

---

## 🎉 重大更新：五大导演系统

**Seedancer v7.0.0** 整合了三大开源技能（shotlist-builder、seedance-director、hellgrind），新增五大导演系统，将 Seedancer 从"提示词生成器"进化为"真正的 AI 导演操作系统"。

---

## ✨ 新增功能

### 1. 🎭 场景原型路由系统

**整合自**：shotlist-builder

自动识别 9 种场景原型，决策树驱动：

**动作类**：
- 追逐 → 对决 → 冲击

**通用类**：
- 旅程 → 氛围 → 揭示

**对话类**：
- 对峙 → 审讯 → 谈判

每种原型有独立的摄影机焦点、空间动态和决策逻辑，无需手动判断场景类型。

**参考文档**：`references/scene-prototypes.md`

---

### 2. 📷 摄影机-情绪同步系统

**整合自**：shotlist-builder

摄影机是焦点角色的情绪分身。6 种情绪自动映射到摄影机类型：

| 情绪 | 摄影机类型 | 效果描述 |
|------|-----------|---------|
| 愤怒/紧张 | 手持呼吸，不稳定 | 画面有明显呼吸式漂移、上下微抖 |
| 平静/控制 | 手持呼吸，平滑 | 极细微的、规律的呼吸式微动 |
| 悲伤/脆弱 | 手持，缓慢低位 | 呼吸节奏放慢，极轻微下沉感 |
| 震惊/揭示 | 静止 + 慢推/慢拉 | 开始严格静止，0.5秒后极缓慢移动 |
| 动作 | 60fps 180°快门 | 流畅运动，快门范围内运动模糊 |
| 终拍/判词 | 俯拍定格 | 严格正上方俯拍，0.3-0.5秒freeze |

情绪变化时摄影机同步分阶段变化，绑定到编号表演节拍（① ② ③ ...）。

**参考文档**：`references/camera-emotion-sync.md`

---

### 3. 🎬 表演微节拍目录

**整合自**：shotlist-builder + hellgrind

**铁律**：泛化情绪 → 坏提示词；具体肌肉/呼吸/眼神 → 好提示词

每种情绪分解为具体的肌肉运动：

**愤怒**：
- 咬肌搏动、颈动脉脉搏、鼻翼扩张、瞳孔收缩

**焦虑**：
- 喉结吞咽、台词前短促浅吸气、舔润下唇

**悲伤**：
- 眼角外缘下垂、湿润带眼神光但不流泪

**震惊**：
- 身体冻结 0.3-0.5秒、瞳孔扩张、延迟急促鼻吸气

每句台词有前节拍（吞咽/吸气）+ 中 emphasis + 后节拍（0.5秒凝视）。

**参考文档**：`references/performance-micro-beats.md`

---

### 4. 💡 光源规则系统

**整合自**：shotlist-builder

**practicals-only 铁律**：严格仅使用场景内实际存在的光源

- 摄影机始终在人物的阴影侧（shadow side）拍摄
- 色彩 60:30:10 — 主色/辅色/点缀色
- 全程大气薄雾 haze，禁止可见光束（god rays）
- 场景变体：夜景/地下基地/日外/夜外/暖室内各有独立灯光条款

**参考文档**：`references/lighting-rules.md`

---

### 5. 📋 JSON API 输出模式

**整合自**：seedance-director (skill_cn.md)

可选输出模式，返回结构化 JSON 数组：

```json
[
  {"lang": "en", "prompt": "..."},
  {"lang": "zh", "prompt": "..."}
]
```

提示词内嵌 5 个分节标签：
1. Style & Mood / 风格与氛围
2. Narrative Summary / 叙事概要
3. Dynamic Description / 动态描述
4. Static Description / 静态描述
5. Audio / 音频

**特性**：
- 中文硬上限 1800 字符
- 完整反垃圾词汇表（EN 30+ / ZH 20+ 禁用词）
- 可自动化集成

**参考文档**：`references/json-api-mode.md`

---

## 📊 系统架构升级

### v7.0.0 完整架构

```
Seedancer v7.0.0
├── P0-P2 预生产管线 (v5.0.0)
│   ├── P0 项目接收
│   ├── P0A 十项剧本解析
│   ├── P1 创作基准
│   ├── P2a 角色资产
│   └── P2b 关键道具
│
├── 五大硬门系统 (v6.0.0)
│   ├── 台词容量预检
│   ├── 分组硬门
│   ├── 镜头密度四道门
│   ├── 运镜设计系统
│   └── 输出格式硬门
│
├── 五大导演系统 (v7.0.0) 🆕
│   ├── 场景原型路由
│   ├── 摄影机-情绪同步
│   ├── 表演微节拍目录
│   ├── 光源规则系统
│   └── JSON API 输出模式
│
├── 核心模块
│   ├── CINEDANCE 16-block
│   ├── LIRA 4-D
│   ├── ACTING
│   ├── GEO 空间锁定
│   ├── Style Prefix
│   ├── SCALE LAW
│   ├── AI 导演方法论
│   └── 失败诊断 33 码
│
└── 12 门控路由系统
    ├── 门控 0-0A: 预生产
    ├── 门控 1-6: 标准流程
    ├── 门控 7: 提示词构建
    ├── 门控 7A: 台词容量预检
    ├── 门控 7B: 分组与密度
    └── 门控 8: 质量检查
```

---

## 📈 统计信息

| 指标 | v6.0.0 | v7.0.0 | 变化 |
|------|--------|--------|------|
| 参考文档数量 | 26 | 31 | +5 |
| 门控系统数量 | 12 | 12 | - |
| 核心模块数量 | 8 | 13 | +5 |
| 新增参考文档大小 | - | ~15KB | - |
| SKILL.md 大小 | ~41KB | ~45KB | +4KB |

---

## 🔗 整合来源

### shotlist-builder
- 场景原型路由系统
- 摄影机-情绪同步
- 表演微节拍目录
- 光源规则系统

### seedance-director (skill_cn.md)
- JSON API 输出模式
- 反垃圾词汇表

### hellgrind 地狱磨砺
- ACTING SKILL（表演系统增强）
- CINEDANCE（分镜系统增强）
- LIRA（图像系统增强）

---

## 🚀 升级指南

### 从 v6.0.0 升级

无需额外操作，新系统自动激活。

### 使用新功能

#### 场景原型路由
无需手动配置，系统自动识别场景类型。

#### 摄影机-情绪同步
自动生效，无需额外配置。

#### 表演微节拍
自动应用到角色表演描述。

#### 光源规则
自动应用 practicals-only 规则。

#### JSON API 输出
如需 JSON 输出，指定 `output_mode: json`。

---

## 📝 致谢

感谢以下开源项目的贡献：

- **shotlist-builder** - 场景路由 + 摄影机情绪 + 表演微节拍 + 光源规则
- **seedance-director** - JSON API 模式 + 反垃圾词表
- **hellgrind 地狱磨砺** - ACTING + CINEDANCE + LIRA 增强
- **Elio_AIGC** - 五大硬门系统（v6.0.0）
- **chaoge-assets-trial** - P0-P2 预生产管线（v5.0.0）
- **ifeihong/aigc-film-studio** - CINEDANCE + LIRA + ACTING + GEO + Style Prefix（v4.1.0）

完整归属声明见 [LICENSE](LICENSE)。

---

## 🔗 链接

- **GitHub**: https://github.com/taosiuman/seedancer
- **ClawHub**: https://clawhub.ai/skills/seedancer
- **问题反馈**: https://github.com/taosiuman/seedancer/issues

---

**🎬 Seedancer v7.0.0 — 从剧本到成片的端到端智能制片管线**
