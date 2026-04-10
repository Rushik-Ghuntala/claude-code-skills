#!/usr/bin/env bash
set -euo pipefail

# Claude Code Skills Installer
# https://github.com/Rushik-Ghuntala/claude-code-skills

REPO_URL="https://github.com/Rushik-Ghuntala/claude-code-skills.git"
INSTALL_DIR="${HOME}/.local/share/claude-code-skills"
CLAUDE_DIR="${HOME}/.claude"
SKILLS_DIR="${CLAUDE_DIR}/skills"
COMMANDS_DIR="${CLAUDE_DIR}/commands"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

print_header() {
    echo ""
    echo -e "${CYAN}${BOLD}Claude Code Skills Installer${NC}"
    echo -e "${CYAN}═══════════════════════════════${NC}"
    echo ""
}

print_success() { echo -e "  ${GREEN}✓${NC} $1"; }
print_warning() { echo -e "  ${YELLOW}!${NC} $1"; }
print_error() { echo -e "  ${RED}✗${NC} $1"; }
print_info() { echo -e "  ${BLUE}→${NC} $1"; }

usage() {
    echo "Usage: install.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --skill <name>    Install a single skill (e.g., --skill viral-hook-generator)"
    echo "  --plugin          Install as a Claude Code plugin"
    echo "  --no-commands     Skip installing slash commands"
    echo "  --help            Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./install.sh                              # Install all skills and commands"
    echo "  ./install.sh --skill mvp-idea-generator   # Install only the MVP idea generator"
    echo "  ./install.sh --plugin                     # Install as a plugin"
}

# Parse arguments
SINGLE_SKILL=""
PLUGIN_MODE=false
INSTALL_COMMANDS=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --skill)
            SINGLE_SKILL="$2"
            shift 2
            ;;
        --plugin)
            PLUGIN_MODE=true
            shift
            ;;
        --no-commands)
            INSTALL_COMMANDS=false
            shift
            ;;
        --help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Determine source directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "${SCRIPT_DIR}/plugin.json" ]]; then
    # Running from cloned repo
    SOURCE_DIR="${SCRIPT_DIR}"
    print_info "Installing from local directory: ${SOURCE_DIR}"
else
    # Running via curl — clone the repo
    print_info "Cloning claude-code-skills..."
    if [[ -d "${INSTALL_DIR}" ]]; then
        cd "${INSTALL_DIR}" && git pull --quiet
        print_info "Updated existing clone"
    else
        git clone --quiet "${REPO_URL}" "${INSTALL_DIR}"
        print_info "Cloned to ${INSTALL_DIR}"
    fi
    SOURCE_DIR="${INSTALL_DIR}"
fi

print_header

# Ensure Claude directories exist
mkdir -p "${SKILLS_DIR}" "${COMMANDS_DIR}"

# Track counts
SKILLS_INSTALLED=0
COMMANDS_INSTALLED=0
SKILLS_SKIPPED=0

install_skill() {
    local skill_name="$1"
    local source_path="${SOURCE_DIR}/skills/${skill_name}"
    local target_path="${SKILLS_DIR}/${skill_name}"

    if [[ ! -d "${source_path}" ]]; then
        print_error "Skill not found: ${skill_name}"
        return 1
    fi

    if [[ -e "${target_path}" ]]; then
        if [[ -L "${target_path}" ]]; then
            # Existing symlink — update it
            rm "${target_path}"
        else
            # Existing directory (not a symlink) — warn
            print_warning "Skipping ${skill_name} (directory exists and is not a symlink)"
            SKILLS_SKIPPED=$((SKILLS_SKIPPED + 1))
            return 0
        fi
    fi

    ln -s "${source_path}" "${target_path}"
    print_success "Installed skill: ${skill_name}"
    SKILLS_INSTALLED=$((SKILLS_INSTALLED + 1))
}

install_command() {
    local cmd_file="$1"
    local cmd_name="$(basename "${cmd_file}")"
    local target_path="${COMMANDS_DIR}/${cmd_name}"

    if [[ -f "${target_path}" ]]; then
        # Overwrite existing command files
        print_warning "Overwriting command: ${cmd_name}"
    fi

    cp "${cmd_file}" "${target_path}"
    COMMANDS_INSTALLED=$((COMMANDS_INSTALLED + 1))
}

# Plugin mode
if [[ "${PLUGIN_MODE}" = true ]]; then
    PLUGIN_DIR="${CLAUDE_DIR}/plugins/claude-code-skills"
    if [[ -e "${PLUGIN_DIR}" ]]; then
        print_warning "Plugin directory already exists: ${PLUGIN_DIR}"
        print_info "Updating..."
        rm -rf "${PLUGIN_DIR}"
    fi
    mkdir -p "${CLAUDE_DIR}/plugins"
    ln -s "${SOURCE_DIR}" "${PLUGIN_DIR}"
    print_success "Installed as plugin at ${PLUGIN_DIR}"
    echo ""
    echo -e "${GREEN}${BOLD}Plugin installed successfully!${NC}"
    echo -e "  All 11 skills, 10 commands, and 3 agents are now available."
    exit 0
fi

# Install skills
echo -e "${BOLD}Installing skills...${NC}"
if [[ -n "${SINGLE_SKILL}" ]]; then
    install_skill "${SINGLE_SKILL}"
else
    for skill_dir in "${SOURCE_DIR}/skills"/*/; do
        skill_name="$(basename "${skill_dir}")"
        install_skill "${skill_name}"
    done
fi

# Install commands
if [[ "${INSTALL_COMMANDS}" = true ]]; then
    echo ""
    echo -e "${BOLD}Installing commands...${NC}"
    if [[ -n "${SINGLE_SKILL}" ]]; then
        # Find the matching command for this skill
        for cmd_file in "${SOURCE_DIR}/commands"/*.md; do
            if grep -q "skill: ${SINGLE_SKILL}" "${cmd_file}" 2>/dev/null; then
                install_command "${cmd_file}"
                print_success "Installed command: $(basename "${cmd_file}")"
            fi
        done
    else
        for cmd_file in "${SOURCE_DIR}/commands"/*.md; do
            install_command "${cmd_file}"
        done
        print_success "Installed ${COMMANDS_INSTALLED} commands"
    fi
fi

# Summary
echo ""
echo -e "${CYAN}═══════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}Installation complete!${NC}"
echo ""
echo -e "  Skills installed:  ${BOLD}${SKILLS_INSTALLED}${NC}"
if [[ ${SKILLS_SKIPPED} -gt 0 ]]; then
echo -e "  Skills skipped:    ${BOLD}${SKILLS_SKIPPED}${NC} (existing directories)"
fi
echo -e "  Commands installed: ${BOLD}${COMMANDS_INSTALLED}${NC}"
echo ""
echo -e "${BOLD}Available commands:${NC}"
echo "  /x-post [topic]           Create ready-to-publish tweets"
echo "  /x-thread [topic]         Compose multi-tweet threads"
echo "  /x-hook [topic]           Generate scroll-stopping hooks"
echo "  /x-optimize [draft]       Optimize tweets for algorithm"
echo "  /x-score [draft]          Score engagement potential"
echo "  /x-schedule [type]        Get optimal posting times"
echo "  /x-calendar [niche]       Generate weekly content plan"
echo "  /x-article [topic]        Write long-form articles"
echo "  /x-trends [niche]         Discover trending topics"
echo "  /mvp-ideas [count] [niche] Research MVP opportunities"
echo ""
echo -e "  Run any command in Claude Code to get started!"
echo ""
