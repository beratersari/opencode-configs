---
name: spring
description: Spring / Spring Boot skill. Load when the diff changes files that import org.springframework, application.yml, or spring-boot starters.
license: MIT
compatibility: opencode
---

# Spring

Project rules still win. Honor the Boot / Java version.

## Look for

- `@Transactional` on a private / self-invoked method
  (proxy not applied).
- Field `@Autowired` in a class the project otherwise
  constructor-injects.
- Open entity / lazy load after the session closes
  (this change added a getter used outside the tx).
- Endpoint without the security matcher this app uses
  for sibling routes.
- `application.yml` secret committed; use the project's
  env / vault pattern.
- Actuator exposed without auth if this change enables it.

## Do not flag

- XML config in a legacy module that already uses it.
- Suggesting WebFlux in a servlet app.
