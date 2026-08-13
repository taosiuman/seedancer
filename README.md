# Seedancer — AIGC 影视导演操作系统

> 从一句话到成片的完整制片管线。**不是提示词工具，是导演操作系统。**

[![ClawHub](https://img.shields.io/badge/ClawHub-seedancer-blue)](https://clawhub.ai/taosiuman/seedancer)
[![License: MIT-0](https://img.shields.io/badge/License-MIT--0-green)](./LICENSE)
[![Version](https://img.shields.io/badge/version-4.1.0-orange)](https://github.com/taosiuman/seedancer/releases/tag/v4.1.0)

## 概览

Seedancer 是一个面向 AI 影视创作者的完整导演操作系统，覆盖从单镜头提示词到多镜头序列项目到完整制片管线的全流程。

基于 **Seedance 2.5** / **Kling 3.0** / **Veo 3** 模型机制设计，支持：

- 🎬 **30 秒直出** — 完整情绪弧线一次生成
- 🖼️ **原生 4K** — 商业级交付品质
- 📦 **50 个参考素材** — 30 图 + 10 视频 + 10 音频
- ✂️ **局部编辑** — 时间戳精准控制
- 🧊 **3D 白模参考** — Maya/Blender 工业管线
- 🟩 **绿幕参考** — 主体合成 + 光影重渲染

## 核心系统

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

## 多模型支持

| 模型 | 类型 | 适用场景 |
|------|------|---------|
| **Seedance 2.5** | 视频 | 主力模型，30s/4K/局部编辑/白模/绿幕 |
| **Kling 3.0** | 视频 | 备选，运动幅度大 |
| **Veo 3** | 视频 | 备选，电影质感 |
| **GPT Image 2** | 图像 | 概念图 / 参考图 |
| **Seedream** | 图像 | 风格化图像 |

## 体裁适配

| 体裁 | 画幅 | 集长 | 特点 |
|------|------|------|------|
| 横屏电影 | 16:9 / 2.35:1 | 60-120min | 标准电影语法 |
| 短剧 | 9:16 / 16:9 | 2-5min/集 | 高密度反转 |
| 漫剧 | 9:16 | 1-3min/集 | 二次元风格 |
| 竖屏短视频 | 9:16 | 15-60s | 社交传播 |

## 快速开始

### 安装（OpenClaw）

```bash
# 通过 ClawHub 安装
clawhub install seedancer
```

### 使用

安装后，在 OpenClaw agent 中直接使用触发词：

> "帮我拍一个赛博朋克风格的雨夜街道镜头"

Seedancer 会自动激活导演操作系统，引导你完成：
1. 意图理解 → 画面翻译
2. 模型选择 → 模式路由
3. 参考素材 → 提示词生成
4. 参数输出 → 交付物标准化

## 参考文档

| 文档 | 说明 |
|------|------|
| [`references/cinedance-video-prompt.md`](references/cinedance-video-prompt.md) | CINEDANCE 视频提示词导演系统 |
| [`references/lira-image-prompt.md`](references/lira-image-prompt.md) | LIRA 图像提示词优化系统 |
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

## 五条黄金规则

1. **先听懂，再翻译** — 用户说感受，你输出工艺
2. **先路由，再生成** — 模式/模型/体裁决定一切
3. **先参考，再提示** — 没有参考素材的提示词是空中楼阁
4. **先失败诊断，再重试** — 33 个错误码直接定位修复
5. **先交付物，再收工** — 每次输出必须是标准化交付物

## 版本历史

| 版本 | 日期 | 亮点 |
|------|------|------|
| **v4.1.0** | 2026-08-13 | 整合 AIGC Film Studio 体系（CINEDANCE/LIRA/ACTING/GEO/Style Prefix） |
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

完整归属声明见 [LICENSE](LICENSE)。

## License

[MIT-0](LICENSE) — 无需归属，自由使用。
