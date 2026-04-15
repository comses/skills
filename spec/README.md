# Agent Skills Specification & COMSES Guidance

This directory documents the Agent Skills specification and COMSES-specific conventions for skill development.

## Agent Skills Specification

The Agent Skills standard defines how AI agents discover, load, and use reusable procedural knowledge. Skills are:

- **Discoverable:** Listed on [agentskills.io](https://agentskills.io) and discoverable via `npx skills` CLI
- **Self-contained:** Each skill is a folder with a `SKILL.md` file + optional bundled resources
- **Composable:** Skills can reference and build on outputs of other skills
- **Versionable:** Skills evolve via git tags and repository updates

### Key References

- **Official spec:** [agentskills.io](https://agentskills.io) — The authoritative definition of skill structure, metadata, and publishing requirements
- **Anthropic skills repo:** [github.com/anthropics/skills](https://github.com/anthropics/skills) — Reference implementations and patterns for complex skills
- **Skills CLI:** [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) — The open-source discovery and installation tool

### SKILL.md Format

Every skill must have a `SKILL.md` file with:

1. **YAML frontmatter** (required):
   ```yaml
   ---
   name: skill-name
   description: When and why to use this skill
   ---
   ```

2. **Markdown body** (required): Instructions that the coding agent will follow when the skill triggers

3. **Bundled resources** (optional): Scripts, reference docs, templates in `scripts/`, `references/`, `assets/` subdirectories

See [../template/SKILL.md](../template/SKILL.md) for a template and [../CONTRIBUTING.md](../CONTRIBUTING.md) for authoring guidelines.

## COMSES-Specific Conventions

### Scope: Computational Modeling Focus

Skills in this repository target challenges unique to computational modelers (ABMs, systems dynamics, PDEs, etc.):

- **Documentation:** Following the ODD+2 protocol for model narrative
- **Publication:** FAIR4RS compliance, metadata, archival readiness
- **Execution:** Running on OSPool, HPC clusters, and cloud environments at scale
- **Reproducibility:** Environment capture, containerization, verification
- **Analysis:** Parameter surveys, sensitivity analysis, validation

### Governance

1. **Naming:** Skill names are `kebab-case` and folder names must match the `name:` field
| **Triggers:** | Description field should explicitly list when the coding agent should use the skill (avoid overly generic triggers) |
3. **Documentation quality:** Frontmatter should be concrete and unambiguous; body instructions should be imperative and include gotchas
4. **Testing requirement:** All skills must include an evaluation strategy (see CONTRIBUTING.md)
5. **License:** Default to MIT; other licenses require explicit declaration in frontmatter

### Quality Gates

Before merging a new skill:

- [ ] Valid YAML frontmatter with matching folder name
- [ ] Description is specific to computational modeling domain (not generic)
- [ ] Tested against should-trigger and should-not-trigger prompts
- [ ] Bundled resources follow naming conventions (scripts/X.py, references/TOPIC.md, assets/template.X)
- [ ] No hardcoded paths, API keys, or user-specific settings
- [ ] MIT license (or alternative justified in PR)

### Skill Maturity Levels

Metadata.maturity field should indicate:

- **alpha:** Proof-of-concept, limited testing, expect breaking changes
- **beta:** Core functionality stable, bundled resources present, tested in multiple scenarios
- **stable:** Published, documented, backward-compatible, proven in production use

## COMSES Modeling Domains

Skills should clearly indicate their target audience and domain:

### Domains

- **computational-modeling:** General modeling tasks (documentation, validation, reproducibility)
- **publication:** FAIR metadata, citation, archival
- **execution:** Infrastructure and scaling (HPC, cloud, OSPool)
- **analysis:** Data analysis, visualization, sensitivity studies

### Audiences

- **modelers:** Researchers building computational models
- **researchers:** Broader academic users (students, postdocs, faculty)
- **data-scientists:** ML practitioners using models as components
- **operators:** Infrastructure/DevOps professionals supporting modelers

## Interchange Standards

Skills should produce outputs in portable, standard formats:

- **Configuration:** YAML or JSON (not INI or custom DSLs)
- **Data lineage:** DVC-compatible or W3C PROV-compatible formats
- **Environments:** standard requirements.txt, poetry.lock, renv.lock, or Dockerfile
- **Metadata:** CITATION.cff, JSON-LD, or Dublin Core when applicable
- **Checkpoints:** Markdown, CSV, or Parquet (not proprietary formats)

## Roadmap & Future Domains

See [../docs/roadmap.md](../docs/roadmap.md) for planned skill expansions into reproducibility, data lineage, advanced analysis, and integrations.

---

**Questions?** Open an issue in the repository or contact the COMSES Network.
