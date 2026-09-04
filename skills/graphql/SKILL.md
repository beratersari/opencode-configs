---
name: graphql
description: GraphQL skill. Load when working with *.graphql, schema.gql, resolvers, Apollo, or gqlgen. Use for implement, debug, or review.
license: MIT
compatibility: opencode
---

# GraphQL

## Rules

- N+1 in a resolver (field that queries per parent).
  DataLoader / batch when the project has it.
- Breaking schema: removed field, non-null added, type
  change. Prefer deprecate.
- Authz on the type/field, not only the HTTP layer.
- Mutations that are not idempotent and have no client
  mutation id when the API already uses one.
- Introspection left on in production if the project
  disables it elsewhere.
- Circular types without a pagination / depth limit on
  a new connection.

## Do not

- Demand Relay if the schema is not Relay.
