# 🎬 Seedancer — Seedance 2.0 Prompt Engineering Skill

> 将文学剧本、粗略想法或参考素材转化为极具可执行性的 Seedance 2.0（即梦）视频生成提示词。

## 特性

- **五维度分镜标准** — 镜头语言/物理交互/情感节拍/光影特效/节奏锚点
- **多轮导演交互** — 生成前先与导演确认视觉基调
- **全参考模式支持** — 文本/首帧/全参考/视频延长/视频编辑
- **IP 安全策略** — 内置版权回避与渐进式降级
- **即用型配方** — 电商/短剧/奇幻/武侠/科普/MV/一镜到底

## 安装

### ClawHub
```bash
clawhub install seedancer
```

### OpenClaw Skills
```bash
# Clone into your skills directory
git clone https://github.com/taosiuman/seedancer.git ~/.openclaw/skills/seedancer
```

## 使用

激活技能后，直接描述你的视频需求：
```
"帮我生成一个 10 秒 9:16 的仙侠打斗提示词，首帧用 @image1"
```

技能会先与你确认视觉基调，再生成结构化的五维度分镜提示词。

## 文件结构

```
SKILL.md                          # 主技能文件
LICENSE                           # MIT-0 许可证
SKILL.sh                          # 命令行测试助手
references/
  recipes.md                      # 即用型提示词配方
  modes-and-recipes.md            # 模式说明与交互笔记
  camera-and-styles.md            # 镜头语言与视觉风格词汇表
scripts/
  setup_seedance_prompt_workspace.sh  # 工作区脚手架
```

## 许可证

MIT-0 — 无保留地使用、复制、修改、分发。

基于 [kn78900pfs4x1dyejyd8vj121s804aea](https://clawhub.ai/user/kn78900pfs4x1dyejyd8vj121s804aea) 的 `seedance-2-prompt-engineering-skill` 汉化重制。

## 作者

**taosiuman** — 中文本地化与 V2.0 全面升级
