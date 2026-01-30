---
paths:
  - "**/playbooks/**"
  - "**/roles/**"
  - "**/inventory/**"
  - "**/group_vars/**"
  - "**/host_vars/**"
---

# Standards Ansible

## Principes fondamentaux

- **Idempotence obligatoire** : chaque run produit le même état
- **Declaratif** : décrire l'état souhaité, pas les étapes
- Variables dans `host_vars/` et `group_vars/`, jamais hardcodées
- Secrets dans Ansible Vault, jamais en clair

## Structure projet

```
ansible/
├── ansible.cfg
├── inventory/
│   ├── production/
│   │   ├── hosts.yml
│   │   ├── group_vars/
│   │   └── host_vars/
│   └── staging/
├── playbooks/
│   ├── site.yml
│   ├── webservers.yml
│   └── databases.yml
├── roles/
│   └── <role-name>/
│       ├── tasks/main.yml
│       ├── handlers/main.yml
│       ├── templates/
│       ├── files/
│       ├── vars/main.yml
│       ├── defaults/main.yml
│       └── meta/main.yml
└── group_vars/
    ├── all.yml
    └── webservers.yml
```

## FQCN obligatoire

```yaml
# ❌ MAUVAIS
- name: Install package
  apt:
    name: nginx

# ✅ BON
- name: Install nginx web server
  ansible.builtin.apt:
    name: nginx
    state: present
    update_cache: true
```

## Nommage des tasks

```yaml
# ❌ MAUVAIS
- name: copy config
  ansible.builtin.copy:

# ✅ BON - Descriptif, commence par verbe
- name: Deploy nginx configuration file
  ansible.builtin.template:
```

## Permissions explicites

```yaml
- name: Deploy application configuration
  ansible.builtin.template:
    src: app_config.j2
    dest: /etc/app/config.yml
    owner: app
    group: app
    mode: "0640"
  notify: Restart application service
```

## Handlers

```yaml
# handlers/main.yml
- name: Restart application service
  ansible.builtin.systemd:
    name: myapp
    state: restarted
    daemon_reload: true
```

## Variables avec defaults

```yaml
# defaults/main.yml - valeurs par défaut documentées
---
app_port: 8080
app_user: app
app_group: app
app_log_level: info

# Limites
app_max_connections: 100
app_timeout_seconds: 30
```

## Vault pour secrets

```bash
# Créer un secret
ansible-vault create group_vars/all/vault.yml

# Éditer
ansible-vault edit group_vars/all/vault.yml

# Utilisation dans playbook
ansible-playbook site.yml --ask-vault-pass
```

```yaml
# group_vars/all/vault.yml (chiffré)
vault_db_password: "supersecret"

# group_vars/all/vars.yml (référence)
db_password: "{{ vault_db_password }}"
```

## Tags pour granularité

```yaml
- name: Configure web server
  ansible.builtin.import_role:
    name: nginx
  tags:
    - nginx
    - webserver
    - configuration
```

```bash
# Exécuter seulement certains tags
ansible-playbook site.yml --tags "nginx,configuration"

# Exclure des tags
ansible-playbook site.yml --skip-tags "slow"
```

## Check mode

```yaml
# Supporter le mode check (dry-run)
- name: Get current version
  ansible.builtin.command: app --version
  register: current_version
  changed_when: false
  check_mode: false
```
