# Seedancer README 自动同步指南

## 规则

当 seedancer 技能有**任何代码更新**（SKILL.md / references/ 修改）时，
必须**同步更新** README.md（英文）和 docs/README-cn.md（中文）。

## 同步步骤

1. 更新 `README.md`（英文）
2. 更新 `docs/README-cn.md`（中文）
3. 两个文件顶部都保留语言切换栏
4. `git add && git commit && git push origin master`

## 语言切换栏（两个文件都必须有）

### README.md（英文）
```
<p align="center">
  <a href="README.md"><b>English</b></a> · <a href="docs/README-cn.md">中文</a>
</p>
```

### docs/README-cn.md（中文）
```
<p align="center">
  <a href="../README.md"><b>English</b></a> · <a href="README-cn.md">中文</a>
</p>
```

## 分支规则

- **唯一推送分支**：`master`
- 禁止推送到 `main` 或其他分支
- git 配置：`push.default = current`
