#!/usr/bin/env bash
set -euo pipefail

# Claude Code Skills Uninstaller
# https://github.com/Rushik-Ghuntala/claude-code-skills

CLAUDE_DIR="${HOME}/.claude"
SKILLS_DIR="${CLAUDE_DIR}/skills"
COMMANDS_DIR="${CLAUDE_DIR}/commands"
INSTALL_DIR="${HOME}/.local/share/claude-code-skills"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'
BOLD='\033[1m'

print_success() { echo -e "  ${GREEN}✓${NC} $1"; }
print_warning() { echo -e "  ${YELLOW}!${NC} $1"; }

SKILLS=(
    "viral-hook-generator"
    "post-creator"
    "tweet-optimizer"
    "thread-composer"
    "article-generator"
    "engagement-prediction"
    "content-calendar"
    "posting-schedule"
    "trend-discovery"
    "mvp-idea-generator"
)

COMMANDS=(
    "x-post.md"
    "x-thread.md"
    "x-hook.md"
    "x-optimize.md"
    "x-score.md"
    "x-calendar.md"
    "x-schedule.md"
    "x-trends.md"
    "x-article.md"
    "mvp-ideas.md"
)

echo ""
echo -e "${CYAN}${BOLD}Claude Code Skills Uninstaller${NC}"
echo -e "${CYAN}════════════════════════════════${NC}"
echo ""

REMOVED=0

# Remove skill symlinks
echo -e "${BOLD}Removing skills...${NC}"
for skill in "${SKILLS[@]}"; do
    target="${SKILLS_DIR}/${skill}"
    if [[ -L "${target}" ]]; then
        rm "${target}"
        print_success "Removed skill: ${skill}"
        REMOVED=$((REMOVED + 1))
    elif [[ -d "${target}" ]]; then
        print_warning "Skipping ${skill} (not a symlink — may be user-modified)"
    fi
done

# Remove command files
echo ""
echo -e "${BOLD}Removing commands...${NC}"
for cmd in "${COMMANDS[@]}"; do
    target="${COMMANDS_DIR}/${cmd}"
    if [[ -f "${target}" ]]; then
        rm "${target}"
        print_success "Removed command: ${cmd}"
        REMOVED=$((REMOVED + 1))
    fi
done

# Remove plugin symlink if exists
PLUGIN_DIR="${CLAUDE_DIR}/plugins/claude-code-skills"
if [[ -L "${PLUGIN_DIR}" ]]; then
    rm "${PLUGIN_DIR}"
    print_success "Removed plugin symlink"
    REMOVED=$((REMOVED + 1))
fi

# Remove cloned repo if installed via curl
if [[ -d "${INSTALL_DIR}" ]]; then
    echo ""
    read -p "  Remove cached repo at ${INSTALL_DIR}? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "${INSTALL_DIR}"
        print_success "Removed cached repo"
    fi
fi

echo ""
echo -e "${GREEN}${BOLD}Uninstall complete!${NC} Removed ${REMOVED} items."
echo ""
