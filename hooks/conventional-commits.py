#!/usr/bin/env python3
"""
Hook: Validate conventional commit messages
Triggers on: git commit commands
"""
import json
import sys
import re

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
command = tool_input.get("command", "")

# Only validate git commit commands
if tool_name != "Bash" or "git commit" not in command:
    sys.exit(0)

# Extract commit message from -m flag
match = re.search(r'git commit.*?-m\s+["\']([^"\']+)["\']', command)
if not match:
    # Try heredoc format
    heredoc_match = re.search(
        r'git commit.*?-m\s+"?\$\(cat\s+<<["\']?EOF["\']?\s*\n(.+?)\nEOF',
        command,
        re.DOTALL
    )
    if heredoc_match:
        commit_msg = heredoc_match.group(1).strip().split('\n')[0]
    else:
        sys.exit(0)
else:
    commit_msg = match.group(1)

# Conventional Commits pattern
VALID_TYPES = ['feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test', 'chore', 'ci', 'build', 'revert']
conventional_pattern = rf'^({"|".join(VALID_TYPES)})(\(.+\))?!?:\s.+'

if not re.match(conventional_pattern, commit_msg):
    reason = f"""❌ Message de commit invalide

Ton message: {commit_msg}

Format requis (Conventional Commits):
  type(scope): description

Types autorisés:
  feat     → Nouvelle fonctionnalité
  fix      → Correction de bug
  docs     → Documentation
  style    → Formatage
  refactor → Refactoring
  perf     → Performance
  test     → Tests
  chore    → Maintenance
  ci       → CI/CD
  build    → Build system

Exemples valides:
  ✅ feat(auth): add JWT token refresh
  ✅ fix(api): handle null response
  ✅ chore(deps): upgrade ansible to 2.15

Invalides:
  ❌ Added feature (pas de type)
  ❌ feat:no space (espace manquant)"""

    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason
        }
    }
    print(json.dumps(output))
    sys.exit(0)

sys.exit(0)
