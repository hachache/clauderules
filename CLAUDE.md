# Standards de Développement

Instructions globales pour tous les projets dans ce répertoire.

## Langue & Communication

- Répondre en **français** sauf si code/commentaires en anglais
- Messages de commit en **anglais** (Conventional Commits)
- Documentation technique : suivre la langue du projet

## Comportement obligatoire

1. **Lire avant modifier** : toujours lire le fichier existant
2. **Respecter les patterns** : identifier et suivre le style en place
3. **Proposer des refactorings** si le code viole les standards
4. **Jamais de secrets** hardcodés (utiliser env vars, vault, secrets manager)

## Structure du projet

```
.claude/
├── CLAUDE.md           # Ce fichier - instructions globales
├── settings.json       # Hooks et configuration
├── agents/             # Agents spécialisés
│   ├── devops-expert.md
│   ├── terraform-specialist.md
│   ├── security-auditor.md
│   └── monitoring-specialist.md
├── hooks/              # Hooks d'automatisation
│   └── conventional-commits.py
└── rules/              # Standards par langage
    ├── global-standards.md
    ├── shell-standards.md
    ├── python-standards.md
    ├── typescript-standards.md
    ├── vue3-standards.md
    ├── ansible-standards.md
    ├── terraform-standards.md
    └── git-commits.md
```

## Agents disponibles

| Agent | Usage |
|-------|-------|
| `devops-expert` | Cycle DevOps complet, DORA metrics, CI/CD |
| `terraform-specialist` | Modules TF, state management, IaC |
| `security-auditor` | Audit OWASP, auth, vulnérabilités |
| `monitoring-specialist` | Observabilité, alerting, SLO/SLA |

## Hooks actifs

- **conventional-commits** : Valide format des commits avant exécution

## Règles conditionnelles

Les règles dans `rules/` s'appliquent selon les paths :
- `**/*.sh` → shell-standards.md
- `**/*.py` → python-standards.md
- `**/*.{ts,tsx}` → typescript-standards.md
- `**/*.vue` → vue3-standards.md
- `**/*.tf` → terraform-standards.md
- `**/playbooks/**`, `**/roles/**` → ansible-standards.md

## Sécurité - Rappels critiques

```
❌ JAMAIS                          ✅ TOUJOURS
─────────────────────────────────────────────────
API_KEY = "sk-xxx"                 process.env.API_KEY
password: "secret"                 vault_password (Ansible)
aws_access_key = "AKIA..."         data.aws_secretsmanager
```

## Qualité du code

- **Noms explicites** : pas d'abréviations (sauf standards)
- **Fonctions courtes** : une seule responsabilité
- **Early returns** : éviter le nesting profond
- **Erreurs contextuelles** : jamais silencieuses
