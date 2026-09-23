#!/usr/bin/env bash
# Seedancer — 视频提示词导演系统测试脚本
# 功能：测试视频提示词生成的基本模板输出
# 注意：完整功能见 SKILL.md 和 references/ 目录
#
# 用法：
#   ./SKILL.sh "你的视频描述"
# 示例：
#   ./SKILL.sh "10s 9:16 cyberpunk rain night street"

set -euo pipefail

REQ="${1:-10s 9:16 cinematic prompt using @image1 as first frame}"

echo "Seedancer Prompt Helper (Basic Test)"
echo "Request: $REQ"
echo ""
echo "Template output (for testing only):"
echo ""
cat <<'EOF'
---
Mode: Basic Template (完整功能请加载 SKILL.md)
Assets Mapping:
- @image1: first frame reference (optional)
- @video1: camera reference (optional)

Basic Prompt Structure:
[aspect_ratio], [duration], [style], [scene], [action], [camera]

Example:
9:16, 10s, cinematic, physically plausible motion.
0-3s: setup shot + subject intro.
3-7s: core action + controlled camera movement.
7-10s: climax/reveal + clean landing frame.

Negative Constraints:
no watermark, no logo, no subtitles, no on-screen text.
---
EOF

echo ""
echo "⚠️  This is a basic test script. For full functionality:"
echo "   - Load SKILL.md in your agent"
echo "   - Check references/ directory for 30+ module docs"
