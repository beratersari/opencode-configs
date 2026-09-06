---
name: aws
description: AWS skill. Load when the diff changes files that import boto3 / aws-sdk, *.tf AWS resources, SAM/CDK, or IAM policy JSON.
license: MIT
compatibility: opencode
---

# AWS

Project rules still win. Do not invent account IDs or keys.

## Look for

- Hardcoded access key / secret / account id.
- IAM `*` Action or Resource this change added when a
  sibling statement is already scoped.
- Public S3 / world-readable ACL on a bucket that holds
  non-public data.
- Lambda timeout / memory copy-pasted without matching
  the new I/O this change added.
- Missing retry / idempotency on a write that can be
  invoked twice (SQS / API Gateway).
- `0.0.0.0/0` ingress this change opened.

## Do not flag

- Multi-cloud rewrite.
- Suggesting a new AWS service when the repo already
  wraps the same need.
