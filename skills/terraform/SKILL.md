---
name: terraform
description: Terraform / OpenTofu / IaC skill. Load when working with *.tf, *.tfvars, terragrunt, or OpenTofu. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Terraform

## Rules

- State: no secrets in `terraform.tfvars` committed to git.
- `force_destroy` on a bucket / DB this change adds.
- Security group `0.0.0.0/0` on a data plane port.
- Missing `prevent_destroy` on irreplaceable data stores
  when the project already uses lifecycle.
- `count` / `for_each` keyed on a list that reorders
  (destroys resources). Prefer a map key.
- Provider version unpinned on a new required_providers.
- `local-exec` with credentials on the command line.

## Do not

- Rewrite working `count` to `for_each` as a style nit.
