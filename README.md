# Seedancer v7.0.0 — AIGC 影视导演操作系统

<div align="center">

**从剧本到成片的端到端智能制片管线**

[![Version](https://img.shields.io/badge/version-7.0.0-blue.svg)](https://github.com/taosiuman/seedancer/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![ClawHub](https://img.shields.io/badge/ClawHub-seedancer-orange.svg)](https://clawhub.ai/skills/seedancer)
[![Seedance](https://img.shields.io/badge/Seedance-2.5-purple.svg)](https://seedance.ai)

**[开始使用](#快速开始)** • **[文档](#核心功能)** • **[示例](#使用示例)** • **[更新日志](CHANGELOG.md)**

</div>

---

## 📖 简介

**Seedancer** 是一个面向 AI 影视创作者的端到端制片操作系统，不是简单的提示词生成器，而是完整的导演工作流引擎。

它将剧本自动转化为生产级视频提示词，整合了 **12 大门控系统**、**10 大核心模块**、**30+ 参考文档**，支持从项目预生产到最终交付的全流程自动化。

### ✨ v7.0.0 新增

整合三大开源技能，新增 **5 大导演系统**：

- 🎭 **场景原型路由** — 9 种场景原型自动识别，决策树驱动
- 📷 **摄影机-情绪同步** — 6 种情绪 → 摄影机类型自动映射
- 🎬 **表演微节拍目录** — 情绪分解为具体肌肉/呼吸/眼神运动
- 📋 **JSON API 输出模式** — 结构化双语输出，可自动化
- 💡 **光源规则系统** — practicals-only 铁律 + 60:30:10 色彩规则

---

## 🎯 核心功能

### 1. 预生产管线 (P0-P2)

自动化项目预生产流程，从剧本解析到资产准备：

| 阶段 | 功能 | 产出 |
|------|------|------|
| **P0** | 项目接收 | 项目基准卡 |
| **P0A** | 十项剧本解析 | 世界观 + 人物小传 + 情绪曲线图 |
| **P1** | 创作基准 | 摄影/色彩/声音圣经 |
| **P2a** | 角色资产 | 9:16 确认稿 + 16:9 设定板 |
| **P2b** | 关键道具 | 3:4 道具母板 |

### 2. 五大硬门系统 (v6.0.0)

确保提示词可执行性和一致性的硬性约束：

- ✅ **台词容量预检** — 语速四档 + 标点停顿 + 反应留白
- ✅ **分组硬门** — 模型时长上限 + 承接等式 + 组尾稳定态
- ✅ **镜头密度四道门** — Smin/Bmin/新反馈/Gmax
- ✅ **运镜设计系统** — 叙事功能表 + 三要素 + 运镜主轴
- ✅ **输出格式硬门** — 自然段写法 + 禁止代词 + 媒介翻译表

### 3. 五大导演系统 (v7.0.0) 🆕

整合三大开源技能的高级导演能力：

#### 🎭 场景原型路由

自动识别 9 种场景原型，决策树驱动：

**动作类**：追逐 → 对决 → 冲击  
**通用类**：旅程 → 氛围 → 揭示  
**对话类**：对峙 → 审讯 → 谈判

每种原型有独立的摄影机焦点、空间动态和决策逻辑。

#### 📷 摄影机-情绪同步

摄影机是焦点角色的情绪分身：

| 情绪 | 摄影机类型 | 效果 |
|------|-----------|------|
| 愤怒/紧张 | 手持呼吸，不稳定 | 画面有明显呼吸式漂移 |
| 平静/控制 | 手持呼吸，平滑 | 极细微规律的呼吸式微动 |
| 悲伤/脆弱 | 手持，缓慢低位 | 呼吸节奏放慢，轻微下沉感 |
| 震惊/揭示 | 静止 + 慢推/慢拉 | 开始严格静止，0.5s 后极缓慢移动 |
| 动作 | 60fps 180° 快门 | 流畅运动，快门范围内运动模糊 |
| 终拍/判词 | 俯拍定格 | 严格正上方俯拍，0.3-0.5s freeze |

#### 🎬 表演微节拍目录

**铁律**：泛化情绪 → 坏提示词；具体肌肉/呼吸/眼神 → 好提示词

每种情绪分解为具体的肌肉运动：

- **愤怒**：咬肌搏动、颈动脉脉搏、鼻翼扩张、瞳孔收缩
- **焦虑**：喉结吞咽、台词前短促浅吸气、舔润下唇
- **悲伤**：眼角外缘下垂、湿润带眼神光但不流泪
- **震惊**：身体冻结 0.3-0.5s、瞳孔扩张、延迟急促鼻吸气

每句台词有前节拍（吞咽/吸气）+ 中 emphasis + 后节拍（0.5s 凝视）。

#### 💡 光源规则系统

**practicals-only 铁律**：严格仅使用场景内实际存在的光源

- 摄影机始终在人物的阴影侧（shadow side）拍摄
- 色彩 60:30:10 — 主色/辅色/点缀色
- 全程大气薄雾 haze，禁止可见光束（god rays）
- 场景变体：夜景/地下基地/日外/夜外/暖室内各有独立灯光条款

#### 📋 JSON API 输出模式

可选输出模式，返回结构化 JSON：

```json
[
  {"lang": "en", "prompt": "..."},
  {"lang": "zh", "prompt": "..."}
]
```

提示词内嵌 5 个分节标签：
1. Style & Mood
2. Narrative Summary
3. Dynamic Description
4. Static Description
5. Audio

中文硬上限 1800 字符，含完整反垃圾词汇表。

### 4. 核心制片模块

| 模块 | 功能 |
|------|------|
| **CINEDANCE 16-block** | 视频提示词导演系统 |
| **LIRA 4-D** | 图像提示词优化系统 |
| **ACTING** | 角色表演系统 |
| **GEO 空间锁定** | 180° 轴线 + frame-left/right 坐标 |
| **Style Prefix** | 逐字粘贴风格前缀 |
| **SCALE LAW** | 尺度锁定法 |
| **AI 导演方法论** | L1/L2/L3 三级输入 |
| **失败诊断** | 6 类 33 码错误诊断 |

### 5. 12 门控路由系统

确保每个请求经过严格的质量控制：

1. **门控 0** - 预生产检测
2. **门控 0A** - 预生产阶段
3. **门控 1** - 接收
4. **门控 2** - 来源核查
5. **门控 3** - 模式选择
6. **门控 4** - 能力检查
7. **门控 5** - 参考映射
8. **门控 6** - 安全门控
9. **门控 7** - 提示词构建
10. **门控 7A** - 台词容量预检
11. **门控 7B** - 分组与密度门控
12. **门控 8** - 质量检查

---

## 🚀 快速开始

### 安装

```bash
clawhub install seedancer
```

### 基本使用

#### 完整项目流程

```
用户：读取我的剧本，帮我完成从剧本解析到角色资产到分镜的全流程

系统：
1. P0 项目接收 → 输出项目基准卡
2. P0A 十项剧本解析 → 世界观 + 人物小传 + 情绪曲线图
3. P1 创作基准 → 摄影/色彩/声音圣经
4. P2a 角色资产 → 9:16 确认稿 + 16:9 设定板
5. P2b 关键道具 → 3:4 道具母板
6. 进入制片管线 → 12 门控路由 → 分镜生成
```

#### 单镜头快速生成

```
用户：帮我拍一个赛博朋克风格的雨夜街道镜头

系统：跳过 P0-P2，直接进入门控 1 → 生成单镜头提示词
```

#### 已有资产继续制作

```
用户：我已经有角色设定板了，帮我生成分镜视频提示词

系统：跳过 P0-P2，继承已有资产，进入制片管线
```

### 输出示例

**输入**：
```
场景：雨夜，赛博朋克城市街道，女主角站在霓虹灯下，表情悲伤
时长：15秒
画幅：16:9
```

**输出**（JSON API 模式）：
```json
[
  {
    "lang": "en",
    "prompt": "Style & Mood: Cyberpunk noir, neon-lit rain, melancholic atmosphere...\nNarrative Summary: Female protagonist stands under neon lights in rainy cyberpunk street...\nDynamic Description: [Camera: handheld, slow breathing, slight downward drift]...\nStatic Description: Wet pavement reflecting neon, steam rising from grates...\nAudio: Rain sounds, distant traffic, no music"
  },
  {
    "lang": "zh",
    "prompt": "风格与氛围：赛博朋克黑色电影，霓虹灯雨夜，忧郁氛围...\n叙事概要：女主角站在霓虹灯下的雨夜赛博朋克街道...\n动态描述：[摄影机：手持，缓慢呼吸，轻微下沉感]...\n静态描述：湿润路面反射霓虹，蒸汽从井盖升起...\n音频：雨声，远处交通，无音乐"
  }
]
```

---

## 📊 支持模型

| 模型 | 类型 | 最大时长 | 适用场景 |
|------|------|---------|---------|
| **Seedance 2.5** | 视频 | 30s | 复杂动作与长对白 |
| **Seedance 2.0** | 视频 | 15s | 性价比高 |
| **Kling 3.0** | 视频 | 15s | 动作与物理交互 |
| **Veo 3** | 视频 | 8s | 短氛围镜 |
| **GPT Image 2** | 图像 | - | 极致照片真实感 |
| **Nano Banana Pro** | 图像 | - | 帧编辑、文字渲染 |
| **Seedream 5.0 Pro** | 图像 | - | 图层分离、商业视觉 |

---

## 📁 参考文档结构

```
references/
├── dialogue-capacity.md        # 台词容量预检
├── grouping-density.md         # 分组硬门 + 镜头密度
├── camera-design.md            # 运镜设计系统
├── output-format.md            # 输出格式硬门
├── scene-prototypes.md         # 场景原型路由 (v7.0.0)
├── camera-emotion-sync.md      # 摄影机-情绪同步 (v7.0.0)
├── performance-micro-beats.md  # 表演微节拍目录 (v7.0.0)
├── json-api-mode.md            # JSON API 输出模式 (v7.0.0)
├── lighting-rules.md           # 光源规则系统 (v7.0.0)
├── story-analysis.md           # P0A 十项剧本解析
├── emotion-curve.md            # 情绪曲线可视化
├── creative-baseline.md        # 创作基准
├── character-assets.md         # 角色资产
├── prop-assets.md              # 关键道具
├── cinedance-video-prompt.md   # CINEDANCE 16-block
├── lira-image-prompt.md        # LIRA 4-D
├── acting-performance.md       # ACTING 表演系统
├── geo-spatial-layout.md       # GEO 空间锁定
├── style-prefix.md             # Style Prefix
├── ai-director.md              # AI 导演方法论
├── failure-codes.md            # 失败诊断
├── deliverable-system.md       # 交付物系统
├── model-mechanics.md          # 模型机制
└── ... (30+ 文档)
```

---

## 📝 使用示例

### 示例 1：完整短片项目

```markdown
用户：我有一个 3 分钟的科幻短片剧本，需要完整的预生产和分镜

系统：
1. P0-P2 预生产管线
   - 解析剧本 → 世界观 + 人物小传
   - 生成情绪曲线图
   - 建立摄影/色彩/声音圣经
   - 生产角色资产和道具母板

2. 制片管线
   - 12 门控路由
   - 分场景生成提示词
   - 输出完整分镜文档
```

### 示例 2：单镜头快速生成

```markdown
用户：帮我生成一个赛博朋克雨夜街道的镜头，15秒，16:9

系统：
- 跳过 P0-P2
- 直接进入门控 1
- 应用场景原型路由（氛围类）
- 应用摄影机-情绪同步（忧郁 → 手持缓慢低位）
- 生成双语提示词
```

### 示例 3：JSON API 自动化

```bash
curl -X POST https://api.clawhub.ai/v1/skills/seedancer/execute \
  -H "Content-Type: application/json" \
  -d '{
    "input": "雨夜，赛博朋克街道，女主角悲伤",
    "options": {
      "output_mode": "json",
      "duration": 15,
      "aspect_ratio": "16:9"
    }
  }'
```

---

## 🔄 版本历史

### v7.0.0 (2026-08-24)

**新增 5 大导演系统**，整合三大开源技能：

- 🎭 场景原型路由（9 种原型 + 决策树）
- 📷 摄影机-情绪同步（6 种情绪映射）
- 🎬 表演微节拍目录（情绪分解为肌肉运动）
- 💡 光源规则系统（practicals-only + 60:30:10）
- 📋 JSON API 输出模式（结构化双语输出）

详见 [CHANGELOG.md](CHANGELOG.md)

### v6.0.0 (2026-08-24)

**新增 5 大硬门系统**，整合 Elio V2.3：

- 台词容量预检
- 分组硬门
- 镜头密度四道门
- 运镜设计系统
- 输出格式/指代硬门

### v5.0.0 (2026-08-14)

**新增 P0-P2 预生产管线**，整合 chaoge-assets-trial

### v4.1.0 (2026-08-13)

整合 AIGC Film Studio 体系（CINEDANCE/LIRA/ACTING/GEO/Style Prefix）

### v4.0.0 (2026-08-09)

Seedance 2.5 全面适配

### v3.0.0 (2026-06-22)

架构级重构

---

## 🤝 致谢

本技能整合了以下开源项目的成果：

- **shotlist-builder** — 场景原型路由 + 摄影机-情绪同步 + 表演微节拍
- **seedance-director (skill_cn.md)** — JSON API 输出模式
- **hellgrind 地狱磨砺** — ACTING SKILL + CINEDANCE + LIRA
- **seedance-2-prompt-engineering-skill** — 基础提示词工程
- **Emily2040/seedance-2.0** — 模型机制 + 反空洞词典
- **ifeihong/aigc-film-studio** — CINEDANCE + LIRA + ACTING + GEO + Style Prefix
- **chaoge-assets-trial** — P0-P2 预生产管线
- **Elio_AIGC (B站/抖音)** — 五大硬门系统

完整归属声明见 [LICENSE](LICENSE)。

---

## 📄 许可证

[MIT License](LICENSE) — 无需归属，自由使用。

---

## 🔗 链接

- **GitHub**: https://github.com/taosiuman/seedancer
- **ClawHub**: https://clawhub.ai/skills/seedancer
- **更新日志**: [CHANGELOG.md](CHANGELOG.md)
- **问题反馈**: https://github.com/taosiuman/seedancer/issues

---

<div align="center">

**🎬 Seedancer v7.0.0 — 从剧本到成片的端到端智能制片管线**

*Made with ❤️ for AI filmmakers*

</div>
