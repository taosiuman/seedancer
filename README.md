# Seedancer — AIGC 影视导演操作系统

> 从剧本到成片的端到端制片管线。**不是提示词工具，是导演操作系统。**

[![ClawHub](https://img.shields.io/badge/ClawHub-seedancer-blue)](https://clawhub.ai/taosiuman/seedancer)
[![License: MIT-0](https://img.shields.io/badge/License-MIT--0-green)](./LICENSE)
[![Version](https://img.shields.io/badge/version-6.0.0-orange)](https://github.com/taosiuman/seedancer/releases/tag/v6.0.0)

## 概览

Seedancer 是一个面向 AI 影视创作者的端到端制片操作系统，覆盖从剧本解析到预生产资产到分镜生成到成片交付的全流程。

基于 **Seedance 2.5** / **Kling 3.0** / **Veo 3** 模型机制设计，支持：

- 🚪 **五大硬门系统** — 台词容量预检 + 分组硬门 + 密度四道门 + 运镜设计 + 输出格式硬门
- 📝 **P0-P2 预生产管线** — 十项剧本解析 + 情绪曲线 + 创作基准 + 角色资产 + 道具母板
- 🎬 **30 秒直出** — 完整情绪弧线一次生成
- 🖼️ **原生 4K** — 商业级交付品质
- 📦 **50 个参考素材** — 30 图 + 10 视频 + 10 音频
- ✂️ **局部编辑** — 时间戳精准控制
- 🧊 **3D 白模参考** — Maya/Blender 工业管线
- 🟩 **绿幕参考** — 主体合成 + 光影重渲染

## 核心系统

### 五大硬门系统（v6.0.0 新增）

整合自 Elio_AIGC Seedance 2.0 Prompts V2.3，确保视频提示词的可执行性与一致性：

| 硬门 | 作用 | 参考文档 |
|------|------|----------|
| **台词容量预检** | 语速四档 + 标点停顿 + 反应留白 → 先算时长再分组 | `dialogue-capacity.md` |
| **分组硬门** | 15/30秒硬上限 + 承接等式 + 组尾稳定态 | `grouping-density.md` |
| **镜头密度四道门** | Smin/Bmin/新反馈/Gmax → 短漫剧必过 | `grouping-density.md` |
| **运镜设计系统** | 叙事功能表 + 三要素 + 每场运镜主轴 | `camera-design.md` |
| **输出格式/指代硬门** | 自然段写法 + 禁止代词 + 禁止模糊方位 + 媒介翻译表 | `output-format.md` |

### 预生产管线（v5.0.0）

| 阶段 | 系统 | 说明 |
|------|------|------|
| **P0** | 项目接收 | 自动输出项目基准卡 |
| **P0A** | 十项剧本解析 | 世界观 + 人物小传 + 状态链 + 情绪曲线自动可视化 |
| **P1** | 创作基准 | 摄影系统 + 风格锁定 + 环境色彩 + 声音圣经 |
| **P2a** | 角色资产 | 依赖图 + 批次生产 + 9:16确认稿 + 16:9设定板 |
| **P2b** | 关键道具 | 候选清单 + 3:4产品档案照母板 |

### 制片管线

| 系统 | 说明 |
|------|------|
| **CINEDANCE 16-block** | 视频提示词导演系统 — 4-D 方法论 + 镜头决策树 + FOV 光学控制 |
| **LIRA 4-D** | 图像提示词优化系统 — 模型路由 + 手术式编辑 + 10 条防失败规则 |
| **ACTING** | 角色表演系统 — 5 大支柱 + 眼生命 + 主档案 + 坏表演图鉴 |
| **GEO 空间锁定** | 180° 轴线 + frame-left/right 坐标 + 地标锚定 |
| **Style Prefix** | 逐字粘贴风格前缀 — 三条根条款（Skin / Acting / Continuity）|
| **SCALE LAW** | 尺度锁定法 — 尺寸对比 + 人形参照物双锚 |
| **AI 导演方法论** | L1/L2/L3 三级输入 + 体裁适配 + 语言路由 |
| **失败诊断** | 6 类 33 码 — 从失败现象直接定位修复方案 |
| **交付物系统** | 5 类标准化交付物 — 提示词 / 参数卡 / 分镜表 / 项目档案 / 制作报告 |

## 全流程架构

```text
P0 项目接收
→ P0A 十项剧本解析 + 情绪曲线图
→ P1 摄影/色彩/声音创作基准
→ P2a 角色资产（依赖图 → 批次生产 → 9:16 → 16:9）
→ P2b 关键道具母板
→ 12 门控路由（含门控 7A 台词容量 + 7B 密度硬门）→ 6 阶段制片流程 → 交付物输出
```

## 多模型支持

| 模型 | 类型 | 适用场景 |
|------|------|---------|
| **Seedance 2.5** | 视频 | 主力模型，30s/4K/局部编辑/白模/绿幕 |
| **Kling 3.0** | 视频 | 备选，运动幅度大 |
| **Veo 3** | 视频 | 备选，电影质感 |
| **GPT Image 2** | 图像 | 概念图 / 参考图 / 角色确认稿 |
| **NBP** | 图像 | 帧编辑 / 文字渲染 / 道具母板 |
| **Seedream** | 图像 | 风格化图像 / Seedance 生态配合 |

## 体裁适配

| 体裁 | 画幅 | 特点 |
|------|------|------|
| 横屏电影 | 16:9 / 2.35:1 | 标准电影语法 |
| 短剧 | 9:16 / 16:9 | 高密度反转 |
| 漫剧 | 9:16 | 二次元风格 |
| 竖屏短视频 | 9:16 | 社交传播 |

## 快速开始

### 安装（OpenClaw）

```bash
clawhub install seedancer
```

### 使用

**完整项目（P0-P2 预生产 + 制片）**：
> "读取我的剧本，帮我完成从剧本解析到角色资产到分镜的全流程"

**单镜头快速生成**：
> "帮我拍一个赛博朋克风格的雨夜街道镜头"

**已有资产继续制作**：
> "我已经有角色设定板了，帮我生成分镜视频提示词"

## 参考文档

| 文档 | 说明 |
|------|------|
| [`references/dialogue-capacity.md`](references/dialogue-capacity.md) | 🆕 台词容量预检系统 |
| [`references/grouping-density.md`](references/grouping-density.md) | 🆕 分组硬门 + 镜头密度四道门 |
| [`references/camera-design.md`](references/camera-design.md) | 🆕 运镜设计系统 |
| [`references/output-format.md`](references/output-format.md) | 🆕 输出格式 + 空间/指代硬门 + 媒介翻译表 |
| [`references/story-analysis.md`](references/story-analysis.md) | P0A 十项剧本解析 |
| [`references/emotion-curve.md`](references/emotion-curve.md) | 情绪曲线自动可视化 |
| [`references/creative-baseline.md`](references/creative-baseline.md) | P1 摄影/色彩/声音基准 |
| [`references/character-assets.md`](references/character-assets.md) | 角色资产依赖图与批次生产 |
| [`references/prop-assets.md`](references/prop-assets.md) | 关键道具母板 |
| [`references/cinedance-video-prompt.md`](references/cinedance-video-prompt.md) | CINEDANCE 视频提示词系统 |
| [`references/lira-image-prompt.md`](references/lira-image-prompt.md) | LIRA 图像提示词系统 |
| [`references/acting-performance.md`](references/acting-performance.md) | ACTING 角色表演系统 |
| [`references/geo-spatial-layout.md`](references/geo-spatial-layout.md) | GEO 空间锁定 |
| [`references/style-prefix.md`](references/style-prefix.md) | Style Prefix 风格前缀 |
| [`references/ai-director.md`](references/ai-director.md) | AI 导演方法论 |
| [`references/failure-codes.md`](references/failure-codes.md) | 失败诊断错误码 |
| [`references/deliverable-system.md`](references/deliverable-system.md) | 交付物系统 |
| [`references/model-mechanics.md`](references/model-mechanics.md) | 模型机制详解 |
| [`references/modes-and-recipes.md`](references/modes-and-recipes.md) | 模式与工作流 |
| [`references/recipes.md`](references/recipes.md) | 提示词配方 |
| [`references/camera-and-styles.md`](references/camera-and-styles.md) | 摄影机语言与视觉风格 |
| [`references/reference-role-map.md`](references/reference-role-map.md) | 参考素材角色映射 |
| [`references/retake-protocol.md`](references/retake-protocol.md) | 重拍协议 |
| [`references/sequence-project-state.md`](references/sequence-project-state.md) | 序列项目状态管理 |
| [`references/continuation-handoff.md`](references/continuation-handoff.md) | 续接交接协议 |
| [`references/anti-slop-lexicon.md`](references/anti-slop-lexicon.md) | 反油腻词典 |

## 九条黄金规则

1. **先听懂，再翻译** — 用户说感受，你输出工艺
2. **先路由，再生成** — 模式/模型/体裁决定一切
3. **先参考，再提示** — 没有参考素材的提示词是空中楼阁
4. **先失败诊断，再重试** — 33 个错误码直接定位修复
5. **先交付物，再收工** — 每次输出必须是标准化交付物
6. **台词先算再写** — 台词容量预检不过，不进入分镜
7. **组尾必须稳定** — 承接等式不成立，不进入下一组
8. **密度必须达标** — 四道门不过，不交付
9. **禁止代词和模糊方位** — 正文出现代词或模糊方位，立即修正

## 版本历史

| 版本 | 日期 | 亮点 |
|------|------|------|
| **v6.0.0** | 2026-08-24 | 五大硬门系统（台词容量预检 + 分组硬门 + 密度四道门 + 运镜设计 + 输出格式硬门）+ 12 门控路由 |
| v5.0.0 | 2026-08-14 | P0-P2 预生产管线 + 10 门控路由 + 端到端制片 |
| v4.1.0 | 2026-08-13 | 整合 AIGC Film Studio（CINEDANCE/LIRA/ACTING/GEO/Style Prefix） |
| v4.0.0 | 2026-08-09 | Seedance 2.5 全面适配（30s/4K/50 素材/局部编辑/白模/绿幕） |
| v3.0.0 | 2026-06-22 | 架构级重构 — 8 门控路由 + 重拍协议 + 序列项目管理 |
| v2.2.2 | 2026-06-20 | 时间片分镜模式 |
| v2.0.0 | 2026-06-14 | Seedance 2.0 适配 |

详细更新日志 → [release-notes.md](release-notes.md)

## 致谢

本技能整合了以下开源项目的成果：

- [seedance-2-prompt-engineering-skill](https://clawhub.ai/dandysuper/seedance-2-prompt-engineering-skill) by dandysuper (MIT-0)
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) by Iamemily2050 (MIT)
- [ifeihong/aigc-film-studio](https://github.com/ifeihong/aigc-film-studio) v3.2.0 by Feihong (MIT)
- chaoge-assets-trial v1.3.0 by taosiuman (MIT-0)
- [seedance20-video-prompts](https://clawhub.ai/Elio_AIGC/seedance20-video-prompts) V2.3 by Elio_AIGC（B站/抖音：Elio_AIGC）

完整归属声明见 [LICENSE](LICENSE)。

## License

[MIT-0](LICENSE) — 无需归属，自由使用。
