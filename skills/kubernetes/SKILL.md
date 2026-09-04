---
name: kubernetes
description: Kubernetes skill. Load when working with Deployment, Service, Ingress, Helm, kustomize, or *.yaml that is a k8s manifest. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# Kubernetes

## Rules

- Resource requests/limits missing on a new workload.
- `latest` image tag on a Deployment this change adds.
- Privileged / `hostNetwork` / hostPath without a reason.
- Secret in a ConfigMap or in plain env from a literal.
- Probe that hits a path the app does not serve, or no
  probe on a long-starting process.
- Service selector that does not match pod labels.
- HPA without requests (cannot scale).
- `cluster-admin` RoleBinding for an app ServiceAccount.

## Do not

- Demand Helm when the repo is plain manifests.
