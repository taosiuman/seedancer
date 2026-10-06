## Description: <br>
Turns scripts into structured shot plans and generation prompts for AI video and image production (Seedance/Kling/Veo/Wan for video; GPT Image/Seedream for asset stills). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[taosiuman](https://clawhub.ai/user/taosiuman) <br>

### License/Terms of Use: <br>
MIT-0 <br>

## Use Case: <br>
Filmmakers and creative teams use this Chinese-first workflow to analyze scripts, plan shots and assets, and prepare prompts for external AI video and image tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional shell helpers create local files and directories when run. <br>
Mitigation: Review helper scripts before running them and execute them only in a dedicated workspace directory. <br>
Risk: Scripts, storyboards, and client assets may be exposed when shared with external media providers. <br>
Mitigation: Confirm the receiving service, what data it retains, and how deletion or withdrawal works before sharing any material. <br>
Risk: Using real people's faces or voices without consent can violate their rights or expectations. <br>
Mitigation: Confirm consent and permitted uses before uploading likeness or voice material; obtain explicit authorization for sensitive or third-party assets (see `references/asset-whitelist.md` §0). <br>
Risk: Prompts referencing recognizable franchises, brands, or realistic faces may be rejected by the target platform. <br>
Mitigation: Use original names, generic visual descriptions, explicit negative constraints, and IP-safe prompt variants as described by the skill. <br>

## Reference(s): <br>
- [Seedancer on ClawHub](https://clawhub.ai/taosiuman/skills/seedancer) <br>
- [Output format](references/output-format.md) <br>
- [JSON API output mode](references/json-api-mode.md) <br>
- [Asset consent and usage rules](references/asset-whitelist.md) <br>
- [Camera language & visual styles vocabulary](references/camera-and-styles.md) <br>

## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown prompts and plans, with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-first; supports bilingual prompt output; produces mode selection, asset mapping, timecoded prompt beats, negative constraints, and generation settings.] <br>

## Skill Version(s): <br>
10.0.0（本目录所载版本；上游来源版本见 LICENSE） (source: frontmatter, VERSION, ClawHub release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
