---
paths:
  - "**/*.sh"
---

# Standards Shell

## En-tête obligatoire

```bash
#!/usr/bin/env bash
set -euo pipefail
```

## Conventions

| Élément | Convention | Exemple |
|---------|------------|---------|
| Variables | Quoted | `"${variable}"` |
| Constantes | SCREAMING_SNAKE_CASE | `readonly MAX_RETRIES=3` |
| Fonctions | snake_case | `validate_input()` |
| Fichiers | kebab-case | `deploy-app.sh` |

## Gestion des erreurs

```bash
set -e          # Arrêt sur erreur
set -u          # Erreur sur variable non définie
set -o pipefail # Propager erreurs dans pipes
```

## Template de script

```bash
#!/usr/bin/env bash
set -euo pipefail

# Constants
readonly SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Logging
log_info()  { echo "[INFO]  $*"; }
log_warn()  { echo "[WARN]  $*" >&2; }
log_error() { echo "[ERROR] $*" >&2; }
die()       { log_error "$*"; exit 1; }

# Usage
usage() {
    cat << EOF
Usage: ${SCRIPT_NAME} [options] <argument>

Options:
    -h, --help      Show this help
    -v, --verbose   Verbose output
EOF
}

# Argument parsing
parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help) usage; exit 0 ;;
            -v|--verbose) VERBOSE=true; shift ;;
            *) break ;;
        esac
    done
}

# Cleanup trap
cleanup() {
    # Remove temp files, restore state
    :
}
trap cleanup EXIT

# Main
main() {
    parse_args "$@"
    # Script logic here
}

main "$@"
```

## Bonnes pratiques

```bash
# ❌ MAUVAIS
cd $dir
rm -rf *
if [ $status == "ok" ]; then

# ✅ BON
readonly TARGET_DIR="${1:?Usage: $0 <directory>}"
cd "${TARGET_DIR}" || die "Cannot cd to ${TARGET_DIR}"
find . -maxdepth 1 -type f -delete
if [[ "${status}" == "ok" ]]; then
```

## Validation input

```bash
# Argument requis avec message
readonly INPUT="${1:?Usage: $0 <input_file>}"

# Vérifier fichier existe
[[ -f "${INPUT}" ]] || die "File not found: ${INPUT}"

# Vérifier commande disponible
command -v jq &>/dev/null || die "jq is required but not installed"
```

## Codes de sortie

| Code | Signification |
|------|--------------|
| 0 | Succès |
| 1 | Erreur générale |
| 2 | Mauvais usage (arguments) |
| 126 | Permission denied |
| 127 | Command not found |
