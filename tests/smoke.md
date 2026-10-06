# 冒烟测试（seedancer）

```bash
# 一致性检查器（零依赖，v3 = 16 项断言）
python scripts/check_consistency.py
exit=0  # v9.0.2 实测：16 项全绿（0 FAIL / 0 WARN）
```

```bash
# 提示词助手（模板输出，仅验证可执行）
bash SKILL.sh "10s 9:16 cyberpunk rain night street"
exit=0
```

记录：见父仓库 `generated/seedancer_consistency_s*.out`。
