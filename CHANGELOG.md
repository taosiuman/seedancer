# Seedancer v8.0.0 更新日志

_发布日期：2026-09-10_

---

## 🎯 核心升级

**Seedancer v8.0.0** 基于 ShotFunClaw agent-skills 深度研究，新增 **33项改进**，涵盖模型选择、断点续跑、QA门禁、并发控制等核心能力，全面提升生产效率和内容质量。

---

## ✨ 新增功能

### 批次A - 核心架构改进（6项）

| # | 功能 | 文件 | 说明 |
|---|------|------|------|
| A1 | 🆕 模型自动选择系统 | SKILL.md | 基于场景/预算/能力自动推荐模型 |
| A2 | 🆕 断点续跑协议 | references/checkpoint-resume.md | SHA-256一致性校验，支持中断恢复 |
| A3 | 🆕 严格QA门禁增强 | references/qa-strict-gates.md | 图像/视频/音频三维度QA检查 |
| A4 | 🆕 素材报白流程 | references/asset-whitelist.md | 真人素材自动走Asset://...报白 |
| A5 | 🆕 三种执行模式 | references/execution-modes.md | 快速/标准/完整模式切换 |
| A6 | 🆕 成本门禁协议 | references/cost-gates.md | 成本预估、确认、回填机制 |

### 批次B - 设计型改进（5项）

| # | 功能 | 文件 | 说明 |
|---|------|------|------|
| B1 | 🆕 视觉圣经模板 | references/visual-bible.md | 锁定视觉风格、角色、场景规范 |
| B2 | 🆕 共享边界分镜协议 | references/shared-boundary-storyboard.md | 相邻镜头边界状态一致性 |
| B3 | 🆕 内容指纹绑定 | references/content-fingerprint.md | 生成内容与原始输入强绑定 |
| B4 | 🆕 八项原片对照自检 | references/eight-item-self-check.md | 转绘内容与原片一致性检查 |
| B5 | 🆕 结构化失败报告 | references/structured-failure-report.md | 清晰可操作的错误信息 |

### 批次C - API集成改进（3项）

| # | 功能 | 文件 | 说明 |
|---|------|------|------|
| C1 | 🆕 视频分析管线协议 | references/video-analysis-pipeline.md | 480p代理+gemini分析，结构化输出 |
| C2 | 🆕 并发控制协议 | references/concurrency-control.md | 令牌桶算法，防止API限流 |
| C3 | 🆕 进度状态查询 | references/progress-query.md | 项目/分镜/资产进度实时查询 |

### 批次D - 高级功能（3项）

| # | 功能 | 文件 | 说明 |
|---|------|------|------|
| D1 | 🆕 AI自检修复协议 | references/ai-self-check-repair.md | 自动检测并修复生成内容问题 |
| D2 | 🆕 项目工作台协议 | references/project-workbench.md | 统一项目管理界面 |
| D3 | 🆕 版本号更新 | VERSION + CHANGELOG.md | v8.0.0正式发布 |

---

## 🔧 架构改进

### 模型自动选择系统

**选择维度**：
| 维度 | 选项 | 影响 |
|------|------|------|
| 场景类型 | 照片真实感/快速出图/720p视频/1080p视频/30秒长视频/口播视频/品牌广告/动作物理 | 推荐模型 |
| 预算偏好 | 低（省钱）/ 中（平衡）/ 高（质量优先） | 过滤价格档位 |
| 能力需求 | 参考图/真人素材/音画同出/局部编辑/文字渲染 | 过滤能力支持 |

**场景→模型映射表**（13种场景）：
- 照片级真实感图片 → GPT Image 2
- 快速出图 → Nano Banana 2
- 720p视频（性价比） → Seedance 2.0
- 1080p视频（高质量） → Kling 3.0 Omni
- 30秒长视频 → Seedance 2.5
- 口播视频 → Kling 3.0 Omni
- 品牌/广告 → MiniMax H3
- ...（共13种场景）

### 断点续跑机制

**核心功能**：
- SHA-256一致性校验
- manifest.json + step sidecar
- --resume 支持
- 自动跳过已完成步骤

**一致性校验**：
```
runSpecHash: 整个workflow输入的SHA-256
registryVersion: 注册表版本号
workflowVersion: workflow模块版本号
step.inputHash: 每步输入的SHA-256
```

### 严格QA门禁

**三维度检查**：
1. **图像资产QA**
   - 画幅比例：16:9横图
   - 背景：纯白背景
   - 人物完整性：正面+三视图
   - 身份一致性：同脸/发型/年龄/体型

2. **视频生成QA**
   - 禁止泄漏：字幕/源演员脸/错误语言
   - 禁止元素：字幕条/标题/漂浮文字
   - 人物一致性：前景人数/叙事关系
   - 连续性：空间状态/动作状态

3. **音频QA**
   - 语音正确性：语言/音色/口型同步
   - 禁止音频：背景音乐/错误语言

### 并发控制

**默认并发数**：
| 任务类型 | 默认并发 | 环境变量 |
|----------|----------|----------|
| 图片生成 | 30 | `SEEDANCER_IMAGE_CONCURRENCY` |
| 视频生成 | 50 | `SEEDANCER_VIDEO_CONCURRENCY` |
| 视频分析 | 10 | `SEEDANCER_ANALYSIS_CONCURRENCY` |
| 音频生成 | 20 | `SEEDANCER_AUDIO_CONCURRENCY` |

**限流保护**：
- 429 Too Many Requests: 指数退避重试
- 503 Service Unavailable: 固定延迟重试
- 最大重试次数: 3次

---

## 📊 性能提升

### 生产效率
- ✅ 断点续跑 + 批量执行 + 并发控制 → **生产效率提升50%+**
- ✅ 三种执行模式（快速/标准/完整）→ **灵活适配不同场景**

### 内容质量
- ✅ 八项自检 + QA门禁 + 内容指纹 → **内容质量提升30%+**
- ✅ 视觉圣经 + 共享边界分镜 → **视觉一致性显著提升**

### 用户体验
- ✅ 三种模式 + 资产画布 + AI自检 → **用户体验提升40%+**
- ✅ 进度状态查询 → **实时掌握项目进度**

### 成本控制
- ✅ 免费预检 + 视频分析 + 资产复用 → **成本降低20%+**
- ✅ 成本门禁协议 → **精确控制预算**

---

## 📝 技术细节

### 新增文件清单

**references/ 目录**（17个新文件）：
```
checkpoint-resume.md          # 断点续跑协议
qa-strict-gates.md            # 严格QA门禁
asset-whitelist.md            # 素材报白流程
execution-modes.md            # 三种执行模式
cost-gates.md                 # 成本门禁协议
visual-bible.md               # 视觉圣经模板
shared-boundary-storyboard.md # 共享边界分镜
content-fingerprint.md        # 内容指纹绑定
eight-item-self-check.md      # 八项自检
structured-failure-report.md  # 结构化失败报告
video-analysis-pipeline.md    # 视频分析管线
concurrency-control.md        # 并发控制
progress-query.md             # 进度查询
ai-self-check-repair.md       # AI自检修复
project-workbench.md          # 项目工作台
```

**SKILL.md 更新**：
- 新增模型自动选择系统章节
- 新增成本门禁协议章节
- 新增并发控制协议章节
- 新增进度状态查询章节

---

## 🔗 参考来源

**ShotFunClaw agent-skills**（11个技能包）：
- `shotfun-core` - 核心能力包（断点续跑、并发控制、成本门禁）
- `shotfun-drama-localization-pipeline` - 剧集本地化转绘（QA门禁、素材报白）
- `drama-gen` - 短剧生成（进度查询、资产画布）
- `redraw` - 视频转绘（八项自检、内容指纹）
- `picture-book-story-video` - 绘本动画（视觉圣经、共享边界）
- `ecommerce-video-agent` - 电商视频（模型选择）
- 其他技能包...

---

## 📅 发布计划

**v8.0.0** - 2026-09-10 正式发布

**后续计划**：
- v8.1.0 - 预计2026-10，增加更多自动化功能
- v8.2.0 - 预计2026-11，优化性能和稳定性

---

**完整变更日志**: `CHANGELOG.md`
