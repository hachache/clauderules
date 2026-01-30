---
paths:
  - "**/*.tf"
  - "**/*.tfvars"
---

# Standards Terraform / Infrastructure as Code

## Principes fondamentaux

- Tout versionné, testé, revu
- Idempotence non négociable
- Safe to rerun, safe to fail, safe to rollback
- **State files are sacred** : toujours backup

## Workflow

```
terraform init → terraform validate → terraform plan → terraform apply
```

**Règle d'or** : `plan` avant `apply`, reviewer tous les changements.

## Structure projet

```
terraform/
├── modules/
│   └── <module-name>/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── README.md
├── environments/
│   ├── dev/
│   ├── staging/
│   └── prod/
├── main.tf
├── variables.tf
├── outputs.tf
├── providers.tf
├── versions.tf
└── backend.tf
```

## Variables avec validation

```hcl
variable "environment" {
  type        = string
  description = "Environment name"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}
```

## Tags obligatoires

```hcl
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "terraform"
    Owner       = var.owner
  }
}

resource "aws_instance" "app" {
  # ...
  tags = merge(local.common_tags, {
    Name = "${var.environment}-app-server"
    Role = "application"
  })
}
```

## Outputs explicites

```hcl
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app.id
}

output "instance_public_ip" {
  description = "Public IP address"
  value       = aws_instance.app.public_ip
  sensitive   = false
}
```

## Backend remote state

```hcl
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "project/env/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

## Sécurité

- **Jamais** de secrets dans le code
- Utiliser data sources ou secrets manager
- State remote avec chiffrement
- Activer state locking (DynamoDB, Azure Blob)

```hcl
# ❌ MAUVAIS
resource "aws_db_instance" "db" {
  password = "mysecretpassword"
}

# ✅ BON
data "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}

resource "aws_db_instance" "db" {
  password = data.aws_secretsmanager_secret_version.db.secret_string
}
```

## Versioning

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```
