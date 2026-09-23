#!/usr/bin/env bash
# Seedancer — workspace scaffold helper
# Creates a minimal directory structure for organizing video prompt drafts.
# This is a simple folder creation utility, NOT the full Seedancer pipeline.
# For full functionality, load SKILL.md in your agent runtime.
#
# Usage:
#   bash scripts/setup_seedance_prompt_workspace.sh [dir]

set -euo pipefail

OUT_DIR="${1:-seedance2-workspace}"
mkdir -p "$OUT_DIR"/{prompts,assets,outputs}

cat > "$OUT_DIR/README.txt" <<'EOF'
Seedance prompt workspace (basic folder scaffold)

Note: This scaffold is for organizing prompt files only.
For the full Seedancer video prompt generation pipeline,
load SKILL.md in your agent runtime.

folders:
- prompts/ : saved prompt drafts
- assets/  : reference media names for @asset mapping
- outputs/ : generated results notes
EOF

echo "Created: $OUT_DIR"
