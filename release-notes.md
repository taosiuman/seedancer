# Seedancer 更新日志

## v6.0.0 (2026-08-24) — 新增五大硬门系统 🎬

### 🚀 核心升级

整合 Elio_AIGC Seedance 2.0 Prompts V2.3（SKILL制作者：B站/抖音：Elio_AIGC）的五大硬门系统，从"分镜也能写"进化为"写出来就能用"。

### ✨ 新增五大硬门系统

| 新增硬门 | 说明 | 参考文档 |
|---|---|---|
| **台词容量预检** | 语速四档 + 标点停顿 + 反应留白 → 先算时长再分组，禁止语速作弊 | `dialogue-capacity.md` |
| **分组硬门** | 模型适配时长上限（Seedance 2.5=30s/2.0=15s/Veo=8s）+ 承接等式 + 组尾稳定态 | `grouping-density.md` |
| **镜头密度四道门** | Smin/Bmin/新反馈/Gmax + 短漫剧三档（ordinary/action_reversal/fight） | `grouping-density.md` |
| **运镜设计系统** | 10种运镜叙事功能表 + 三要素（起始观察点+运动轨迹+停止结果）+ 每场运镜主轴 | `camera-design.md` |
| **输出格式/指代硬门** | 自然段写法 + 四项事实 + 禁止代词 + 禁止模糊方位 + 视听术语双语 + 媒介翻译表 | `output-format.md` |

### 🆕 新增参考文档（4 个）

- ✅ `references/dialogue-capacity.md` — 台词容量预检：最低时长公式 + 语速四档 + 视觉读取锚点 + 拆段规则
- ✅ `references/grouping-density.md` — 分组硬门 + 镜头密度四道门 + 隐藏切镜检测 + 打戏拆出规则
- ✅ `references/camera-design.md` — 运镜设计：10种运镜功能表 + 三要素 + 狭窄空间限制 + 叙事信号选型
- ✅ `references/output-format.md` — 输出格式硬门 + 空间措辞硬门 + 人物指代硬门 + 媒介翻译表 + 体量控制

### 🏗️ 架构升级

- ✅ **12 门控路由**（原 10 门控 + 新增门控 7A 台词容量预检 + 门控 7B 分组与密度门控）
- ✅ **黄金规则 5条 → 9条**（新增：台词先算再写 / 组尾必须稳定 / 密度必须达标 / 禁止代词和模糊方位）
- ✅ **矛盾检测 4层 → 6层**（新增：台词容量检测 + 密度与承接检测）
- ✅ **门控 8 质量检查新增 5 项硬门检查**（代词/方位/四项事实/运镜三要素/时间码）
- ✅ **失败现象对照表新增 5 个错误码**（F-DIALOGUE-CAPACITY / F-GROUP-CONTINUITY / F-DENSITY / F-HIDDEN-CUT / F-SPATIAL-VAGUE）
- ✅ **阶段五 分镜写作全面硬门化**

### 📊 文件变更

- 6 个文件（1 个修改 SKILL.md + 1 个修改 README.md + 4 个新增 reference）
- 新增约 15KB 参考文档
- SKILL.md 升级至 v6.0.0
- README.md 更新版本号、核心系统、参考文档、黄金规则、版本历史、致谢
- release-notes.md 新增 v6.0.0 条目

### 📝 整合策略

保留 Seedancer v5.0.0 全部功能（P0-P2 预生产管线 + CINEDANCE/LIRA/ACTING/GEO/Style Prefix/SCALE LAW/AI 导演/失败诊断/交付物/多模型支持），在分镜写作阶段新增五大硬门系统。硬门系统确保视频提示词的可执行性与一致性，与原有制片管线无缝衔接。

### 🔗 冲突解决

| 冲突点 | 解决方式 |
|--------|----------|
| 15秒 vs 30秒 | 按模型适配：Seedance 2.0=15秒，2.5=30秒，Veo=8秒 |
| 密度表缩放 | 30秒组密度 = 15秒组 × 2 |
| 输出格式 | CINEDANCE 16-block 作为内部架构，Elio 格式作为输出模板 |

---
## v5.0.0 (2026-08-14) — 新增 P0-P2 预生产管线 🎬

### 🚀 核心升级

整合 [chaoge-assets-trial](https://github.com/taosiuman/chaoge-assets-trial) v1.3.0 的完整预生产体系，从"分镜生成工具"进化为"从剧本到成片的端到端制片操作系统"。

### ✨ 新增 5 大预生产阶段

| 新增阶段 | 说明 | 参考文档 |
|---|---|---|
| **P0 项目接收** | 自动输出项目基准卡（不询问确认） | `story-analysis.md` |
| **P0A 十项剧本解析** | 世界观/人物小传/状态链/空间链 + 情绪曲线自动可视化（8-14节点/16:9黑图） | `story-analysis.md` + `emotion-curve.md` |
| **P1 创作基准** | 摄影系统/风格锁定/环境色彩策略/声音圣经 → 直接注入 Style Prefix + CINEDANCE | `creative-baseline.md` |
| **P2a 角色资产** | 依赖图 → 生产清单 → 9:16确认稿（批次生产）→ 16:9设定板（一次性整批） | `character-assets.md` |
| **P2b 关键道具** | 候选清单 → 3:4 产品档案照母板 → descriptor 逐字注入 | `prop-assets.md` |

### 🆕 新增参考文档（5 个）

- ✅ `references/story-analysis.md` — 十项剧本解析 + 事实等级 + 人物小传规范 + 制作风险扫描 + 门禁规则
- ✅ `references/emotion-curve.md` — 情绪曲线自动可视化（触发条件/曲线计算/图像生成规格/分镜映射）
- ✅ `references/creative-baseline.md` — P1 摄影/色彩/声音创作基准 + Style Prefix/CINEDANCE 衔接规则
- ✅ `references/character-assets.md` — 角色依赖图 + 批次生产 + 9:16提示词模板 + 16:9设定板模板 + 变异门禁 + 验收规则
- ✅ `references/prop-assets.md` — 关键道具母板模板 + 3:4竖构图规则 + LIRA 路由 + CINEDANCE/GEO 衔接

### 🏗️ 架构升级

- ✅ **10 门控路由**（原 8 门控 + 新增门控 0 预生产检测 + 门控 0A 预生产阶段）
- ✅ **预生产 → 制片管线无缝衔接**：
  - P1 风格锁定 → Style Prefix 核心内容
  - P1 摄影参数 → CINEDANCE OPTICS/LIGHTING 全局默认值
  - P1 声音原则 → CINEDANCE AUDIO 全局约束
  - P2a 角色 descriptor → CINEDANCE ACTIVE REFERENCES 逐字注入
  - P2a 状态链 → 跨镜头 descriptor 版本管理
  - P2b 道具 descriptor → CINEDANCE/GEO/SCALE LAW 锚点
  - 情绪曲线节点 → 分镜段落映射 + CINEDANCE 参数选择
- ✅ **快速路径**：单镜头/已有资产可跳过 P0-P2 直接进入制片管线
- ✅ **确认门禁系统**：每个阶段有固定确认/过渡话术
- ✅ **事实等级制度**：剧本事实/强推断/导演提案/待定冲突 四级分明

### 📊 文件变更

- 7 个文件（1 个修改 SKILL.md + 5 个新增 reference + 1 个新增 VERSION）
- 新增约 22KB 参考文档
- SKILL.md 升级至 v5.0.0
- _meta.json 升级至 v5.0.0
- release-notes.md 新增 v5.0.0 条目
- LICENSE 新增 chaoge-assets-trial 归属

### 📝 整合策略

保留 Seedancer v4.1.0 全部功能（CINEDANCE/LIRA/ACTING/GEO/Style Prefix/SCALE LAW/AI 导演/失败诊断/交付物/多模型支持），在上游新增 P0-P2 预生产管线。预生产输出直接注入生产管线的各个 block，形成无缝数据流。

---

## v4.1.0 (2026-08-13) — 整合 AIGC Film Studio 体系 🎬

### 🚀 核心升级

整合 [ifeihong/aigc-film-studio](https://github.com/ifeihong/aigc-film-studio) v3.2.0 的核心体系，从"Seedance 专用提示词工具"进化为"多模型影视导演操作系统"。

### ✨ 新增 8 大系统

| 新增系统 | 说明 | 参考文档 |
|---|---|---|
| **CINEDANCE 16-block** | 视频提示词导演系统（4-D 方法论 + 镜头决策树 + FOV 光学控制） | `cinedance-video-prompt.md` (29KB) |
| **LIRA 4-D** | 图像提示词优化系统（模型路由 + 手术式编辑 + 10 条防失败规则） | `lira-image-prompt.md` (17KB) |
| **ACTING** | 角色表演系统（5 大支柱 + 眼生命 + 主档案 + 坏表演图鉴） | `acting-performance.md` (16KB) |
| **GEO 空间锁定** | 180° 轴线 + frame-left/right 坐标 + 地标锚定 | `geo-spatial-layout.md` (7KB) |
| **Style Prefix** | 逐字粘贴风格前缀（三条根条款：Skin/Acting/Continuity） | `style-prefix.md` (11KB) |
| **AI 导演方法论** | L1/L2/L3 三级输入 + 体裁适配 + 语言路由 | `ai-director.md` (13KB) |
| **失败诊断** | 6 类 33 码 — 从失败现象直接定位修复方案 | `failure-codes.md` (11KB) |
| **交付物系统** | 5 类标准化交付物 | `deliverable-system.md` (16KB) |

### 🎯 多模型支持

- **视频**：Seedance 2.5 / Kling 3.0 / Veo 3
- **图像**：GPT Image 2 / Seedream

### 📊 体裁适配

横屏电影 / 短剧 / 漫剧 / 竖屏短视频 — 四种体裁自动路由。

### 📦 文件变更

- 11 个文件（3 个修改 + 8 个新增）
- 新增约 120KB 参考文档
- SKILL.md 升级至 v4.1.0
- 新增 README.md

---

## v4.0.0 (2026-08-09) — Seedance 2.5 全面适配 🎬

### 🚀 核心升级

Seedance 2.5 模型大版本升级，视频生成从"能生成"走向"可修改、可迭代、可交付"。

### 📊 参数对比（2.0 → 2.5）

| 维度 | v3 (Seedance 2.0) | **v4 (Seedance 2.5)** | 变化 |
|------|-------------------|----------------------|------|
| 单次生成时长 | 15秒 | **30秒** | 🆙 翻倍 |
| 参考素材上限 | 12个 | **50个** | 🆙 4倍+ |
| 输出分辨率 | 最高2K | **原生4K** | 🆙 翻倍 |
| 局部编辑 | ❌ | ✅ 时间戳精准控制 | 🆕 全新 |
| 3D白模参考 | ❌ | ✅ Maya/Blender | 🆕 全新 |
| 绿幕参考 | ❌ | ✅ 光影重渲染 | 🆕 全新 |

---

## v3.0.0 (2026-06-22) — 架构级重构

从提示词工具进化为导演操作系统。新增 8 门控路由 + 重拍协议 + 序列项目管理 + 续接交接协议。

## v2.2.2 (2026-06-20) — 时间片模式

新增时间片分镜模式，支持单镜头内情绪复杂递进。

## v2.0.0 (2026-06-14) — Seedance 2.0 适配

全面适配 Seedance 2.0 模型能力。

---

**🎬 Seedancer v5.0.0 — 从剧本到成片的端到端制片操作系统。**
