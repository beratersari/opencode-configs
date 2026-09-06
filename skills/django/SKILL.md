---
name: django
description: Django skill. Load when the diff changes manage.py, settings.py, urls.py, models.py, or files that import django.
license: MIT
compatibility: opencode
---

# Django

Project rules still win. Honor `USE_TZ`, auth, and the project's Django major.

## Look for

- Query with string-interpolated SQL; use the ORM / params.
- Missing `select_related` / `prefetch_related` only when this
  change obviously N+1s in a loop it added.
- `Model.objects.get` without handling `DoesNotExist` on a
  request path.
- Form / serializer that does not validate a field this view
  now writes.
- CSRF exempt on a cookie-auth POST.
- `DEBUG` or secret key read from a committed settings module.
- Migration that drops a column without a prior code deploy
  that stopped reading it (expand/contract).

## Do not flag

- DRF vs vanilla views as a rewrite.
- Suggesting async views if the project is sync.
