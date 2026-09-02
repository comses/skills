# Installing OMF Skills

## Quick Start

Agent Skills can be installed for a specific project or globally on your user account. Here's what that usually looks
like:

```text
Project-local                         Global

my-model/                             ~/
├── .agents/                          ├── .agents/
│   └── skills/                       │   └── skills/
│       ├── omfa/                     │       ├── omfa/
│       ├── omfb/                     │       ├── omfb/
│       └── ...                       │       └── ...
├── omf-artifacts/                    └── projects/
└── src/                                  └── my-model/
```

where `~` is your home directory.

For most users of these skills, global installation is best because these skills depend on each other and it makes it
easy to update your skills as they evolve which will be frequent.

Please remember to cite the specific repository release and revision of these skills used in your research (see
CITATION.cff). For material changes under `omf-artifacts/`, record the producing skill revision, inputs, decisions,
review status, and the coding agent or model version when observable in `omf-artifacts/fair/provenance-manifest.json`.

## Prerequisites

- A coding-capable AI agent
- Node.js LTS

This guide will primarily cover how to install Node.js so you can run

`npx skills add https://github.com/openmodelingfoundation/skills`

## Install Node.js LTS with nvm (WSL, macOS, Linux)

After you have access to a coding agent you'll want to set up Node.js on your system to use the standard `npx skills ...` to manage your skills collections. Agent skills are simply a set of files installed into a local directory managed by `npx skills` (either globally for use across all of your projects or into a specific project).

We recommend using the node version manager `nvm` to flexibly install and manage Node versions.

1. Install prerequisites

   WSL / Linux:

   ```bash
   sudo apt update
   sudo apt install -y curl ca-certificates git
   ```

   macOS (with Homebrew):

   ```bash
   brew install curl ca-certificates git
   ```

1. Install `nvm` from an official tagged release

   Choose the latest release tag from: <https://github.com/nvm-sh/nvm/releases>

   ```bash
   export NVM_VERSION="v0.40.6" # change to latest release
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/${NVM_VERSION}/install.sh | bash
   ```

1. Load `nvm` in your current shell or close and restart your shell

   The following commands should be auto-appended to your shell profile (.bashrc / .zshrc / etc) but in case they aren't, make sure they are present:

   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
   [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
   ```

   If needed, restart your terminal so your shell profile changes take effect.

1. Install and use the latest Node LTS

   ```bash
   nvm install --lts
   nvm alias default 'lts/*'
   nvm use --lts
   ```

1. Verify toolchain

   ```bash
   node -v
   npm -v
   npx -v
   ```

1. Continue with skills installation

   ```bash
   npx skills add openmodelingfoundation/skills
   # or install from github url
   npx skills add https://github.com/openmodelingfoundation/skills
   ```

1. Keep Node LTS current (maintenance)

   ```bash
   nvm install --lts --reinstall-packages-from=current --latest-npm
   nvm use --lts
   ```

## Manual installation without npx

If you can't run Node.js/npx in your environment, you can install the skills directly with git or by copying skill directories manually to `~/.agents/skills`. `~/.agents/skills` expects one flat directory per skill, so we clone the repo elsewhere and symlink each skill to `~/.agents/skills`.

```bash
# 1. Clone the collection somewhere out of the way
mkdir -p ~/.cache/omf-skills
git clone https://github.com/openmodelingfoundation/skills.git ~/.cache/omf-skills

# 2. (Optional) Pin to a release/tag
cd ~/.cache/omf-skills && git checkout v2026.08

# 3. Symlink each skill into ~/.agents/skills
mkdir -p ~/.agents/skills
for d in ~/.cache/omf-skills/*/; do
  [ -f "$d/SKILL.md" ] && ln -s "${d%/}" ~/.agents/skills/"$(basename "$d")"
done
```

You may need to restart your agent session to pick up the new skills.

Update all: `cd ~/.cache/omf-skills && git pull (symlinks stay in sync automatically)`
Update to a specific version: `git -C ~/.cache/omf-skills fetch --tags && git -C ~/.cache/omf-skills checkout v3000.c0c0`
Remove one: `rm ~/.agents/skills/<skill-name>`
Remove all: `rm ~/.cache/omf-skills/*/ -exec rm ~/.agents/skills/{} \;` or simpler, rm each symlink individually and then `rm -rf ~/.cache/omf-skills`
