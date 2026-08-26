# Seedancer v7.0.0 — AI Film Director Operating System

<p align="center">
  <a href="README.md"><b>English</b></a> · <a href="docs/README-cn.md">中文</a>
</p>

<div align="center">

**From Script to Screen — End-to-End AI Film Production Pipeline**

[![Version](https://img.shields.io/badge/version-7.0.0-blue.svg)](https://github.com/taosiuman/seedancer/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![ClawHub](https://img.shields.io/badge/ClawHub-seedancer-orange.svg)](https://clawhub.ai/skills/seedancer)
[![Seedance](https://img.shields.io/badge/Seedance-2.5-purple.svg)](https://seedance.ai)

**[Quick Start](#quick-start)** · **[Core Modules](#core-modules)** · **[Examples](#examples)** · **[Changelog](CHANGELOG.md)**

</div>

---

## 🎬 Overview

**Seedancer** is not a prompt generator. It is a **director-grade AI film production operating system** — a complete workflow engine that transforms scripts into production-ready video prompts through **12 quality gates**, **10 core modules**, and **30+ reference documents**.

### ✨ What's New in v7.0.0

Five advanced director systems built on three integrated open-source skills:

| System | Capability |
|--------|-----------|
| 🎭 **Scene Prototype Router** | 9 scene archetypes auto-detected via decision tree |
| 📷 **Camera-Emotion Sync** | 6 emotions → camera type automatic mapping |
| 🎬 **Performance Micro-Beat Catalog** | Emotions decomposed into muscle/breath/eye movement |
| 💡 **Lighting Rules Engine** | Practicals-only doctrine + 60:30:10 color rule |
| 📋 **JSON API Output Mode** | Structured bilingual output for automation pipelines |

---

##  Core Modules

### Pre-Production Pipeline (P0–P2)

| Phase | Output |
|-------|--------|
| **P0** Project Intake | Project baseline card |
| **P0A** 10-Point Script Analysis | World bible + character bios + emotion curve |
| **P1** Creative Baseline | Camera/color/sound bible |
| **P2a** Character Assets | 9:16 confirmation + 16:9 concept board |
| **P2b** Key Props | 3:4 prop master template |

### Five Hard Gates (v6.0.0)

Rigorous constraints ensuring prompt executability:

- **Dialogue Capacity Check** — Speaking rate × punctuation pauses × reaction beats
- **Group Hard Gate** — Model duration cap + continuity equation + scene-end stability
- **Shot Density Gates (×4)** — Smin / Bmin / new feedback / Gmax thresholds
- **Camera Design System** — Narrative function table + 3-element camera axis
- **Output Format Gate** — Natural paragraph style + pronoun ban + media translation table

### Five Director Systems (v7.0.0)

####  Scene Prototype Router

Auto-classifies scenes into 9 archetypes with independent camera focus and spatial dynamics:

- **Action**: Chase → Confrontation → Impact
- **General**: Journey → Atmosphere → Revelation  
- **Dialogue**: Standoff → Interrogation → Negotiation

#### 📷 Camera-Emotion Sync

The camera is the emotional avatar of the focal character:

| Emotion | Camera Type | Effect |
|---------|-------------|--------|
| Anger / Tension | Handheld, unstable | Visible breathing drift |
| Calm / Control | Handheld, smooth | Minimal rhythmic micro-movement |
| Sadness / Vulnerability | Handheld, slow low-angle | Slowed breathing, slight descent |
| Shock / Revelation | Locked + slow push/pull | Strict stillness → 0.5s delay → imperceptible move |
| Action | 60fps 180° shutter | Fluid motion, motion blur within shutter angle |
| Final Shot | Overhead freeze-frame | Strict top-down, 0.3–0.5s freeze |

#### 🎬 Performance Micro-Beat Catalog

**Doctrine**: Abstract emotion = bad prompt. Specific muscle/breath/eye = good prompt.

| Emotion | Micro-Beats |
|---------|-------------|
| Anger | Masseter pulsing, carotid pulse, nostril flare, pupil constriction |
| Anxiety | Laryngeal swallow, short pre-line breath, lip moistening |
| Sadness | Outer eye corner droop, moisture band with catch light, no tears |
| Shock | 0.3–0.5s body freeze, pupil dilation, delayed sharp nasal inhale |

Every line: pre-beat (swallow/inhale) + mid emphasis + post-beat (0.5s gaze hold).

#### 💡 Lighting Rules

**Practicals-only doctrine** — only light sources physically present in the scene:

- Camera always on the character's shadow side
- 60:30:10 color ratio — primary / secondary / accent
- Atmospheric haze throughout; no god rays
- Scene-specific clauses: night / underground / day-ext / night-ext / warm interior

#### 📋 JSON API Output Mode

Structured bilingual JSON for automation:

```json
[
  {"lang": "en", "prompt": "Style & Mood: ...\nNarrative: ...\nDynamic: ...\nStatic: ...\nAudio: ..."},
  {"lang": "zh", "prompt": "风格与氛围：...\n叙事：...\n动态：...\n静态：...\n音频：..."}
]
```

Chinese prompt hard cap: 1800 chars. Full anti-junk vocabulary included.

### Supported Models

| Model | Type | Max Duration | Best For |
|-------|------|-------------|----------|
| Seedance 2.5 | Video | 30s | Complex action + long dialogue |
| Seedance 2.0 | Video | 15s | Cost-effective general use |
| Kling 3.0 | Video | 15s | Action + physics interaction |
| Veo 3 | Video | 8s | Short atmosphere shots |
| GPT Image 2 | Image | — | Photorealistic quality |
| Seedream 5.0 Pro | Image | — | Layer separation + commercial |

### 12-Gate Quality Routing

```
Gate 0  Pre-production detect
Gate 0A Pre-production phase
Gate 1  Intake
Gate 2  Source verification
Gate 3  Mode selection
Gate 4  Capability check
Gate 5  Reference mapping
Gate 6  Safety gate
Gate 7  Prompt construction
Gate 7A Dialogue capacity check
Gate 7B Group + density gates
Gate 8  Quality inspection
```

---

## 🚀 Quick Start

### Install

```bash
clawhub install seedancer
```

### Full Production Flow

```
User: Read my script and run the full pipeline from script analysis to storyboard.

System:
1. P0  Project intake → baseline card
2. P0A 10-point script analysis → world + characters + emotion curve
3. P1  Creative baseline → camera/color/sound bible
4. P2a Character assets → 9:16 + 16:9 boards
5. P2b Key props → 3:4 master template
6. Production pipeline → 12 gates → storyboard generation
```

### Single Shot (Skip Pre-Production)

```
User: Shoot a cyberpunk rain-night street, 15s, 16:9.

System: Skip P0-P2 → Gate 1 → Scene router (Atmosphere)
        → Camera-Emotion Sync (Melancholy → Handheld slow low-angle)
        → Bilingual prompt output
```

### JSON API Automation

```bash
curl -X POST https://api.clawhub.ai/v1/skills/seedancer/execute \
  -H "Content-Type: application/json" \
  -d '{"input": "Rain night, cyberpunk street, protagonist melancholic",
        "options": {"output_mode": "json", "duration": 15, "aspect_ratio": "16:9"}}'
```

---

## 📁 Reference Documents (30+)

```
references/
├── scene-prototypes.md          # Scene prototype router (v7)
├── camera-emotion-sync.md       # Camera-emotion sync (v7)
── performance-micro-beats.md   # Performance micro-beat catalog (v7)
├── json-api-mode.md             # JSON API output mode (v7)
├── lighting-rules.md            # Lighting rules engine (v7)
├── dialogue-capacity.md         # Dialogue capacity check
├── grouping-density.md          # Group hard gate + shot density
├── camera-design.md             # Camera design system
├── output-format.md             # Output format gate
├── story-analysis.md            # P0A 10-point script analysis
├── emotion-curve.md             # Emotion curve visualization
├── creative-baseline.md         # Creative baseline
── character-assets.md          # Character assets
├── prop-assets.md               # Key props
├── cinedance-video-prompt.md    # CINEDANCE 16-block
├── lira-image-prompt.md         # LIRA 4-D
├── acting-performance.md        # ACTING performance system
├── geo-spatial-layout.md        # GEO spatial lock
├── style-prefix.md              # Style prefix
├── ai-director.md               # AI director methodology
├── failure-codes.md             # Failure diagnostics (6 types, 33 codes)
└── ...
```

---

## 📜 Changelog Highlights

| Version | Date | Highlights |
|---------|------|-----------|
| **v7.0.0** | 2026-08-24 | 5 director systems: scene router, camera-emotion sync, micro-beats, lighting rules, JSON API |
| **v6.0.0** | 2026-08-24 | 5 hard gates: dialogue capacity, grouping, shot density, camera design, output format |
| **v5.0.0** | 2026-08-14 | P0-P2 pre-production pipeline |
| **v4.1.0** | 2026-08-13 | CINEDANCE / LIRA / ACTING / GEO / Style Prefix integration |
| **v4.0.0** | 2026-08-09 | Seedance 2.5 full adaptation |
| **v3.0.0** | 2026-06-22 | Architecture-level refactoring |

---

##  Acknowledgments

- **shotlist-builder** — Scene prototype router + Camera-emotion sync + Performance micro-beats
- **seedance-director** — JSON API output mode
- **hellgrind** — ACTING / CINEDANCE / LIRA
- **ifeihong/aigc-film-studio** — CINEDANCE / LIRA / ACTING / GEO / Style Prefix
- **chaoge-assets-trial** — P0-P2 pre-production pipeline
- **Elio_AIGC** — Five hard gate systems
- **Emily2040/seedance-2.0** — Model mechanics + anti-junk vocabulary

Full attribution: [LICENSE](LICENSE)

---

## 🔗 Links

**GitHub** · [taosiuman/seedancer](https://github.com/taosiuman/seedancer)  
**ClawHub** · [seedancer](https://clawhub.ai/skills/seedancer)  
**Issues** · [Report a bug](https://github.com/taosiuman/seedancer/issues)

---

<div align="center">

**🎬 Seedancer v7.0.0 — Where Scripts Become Frames**

*Made with ❤️ for AI filmmakers*

</div>
