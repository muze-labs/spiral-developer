# Complexity, Abstraction, and Boundary Signals

Muze treats complexity as an economic cost for humans and AI.

## Core questions

> **Did this change make the system cheaper or more expensive to change next time?**

> **Does this abstraction make everything built on top of it simpler?**

> **What decision does this boundary protect us from changing later?**

## Warning signs

- special cases multiply;
- adapters repeat;
- vocabulary feels forced or proliferates;
- dependent code becomes longer/more conditional;
- schemas fight common use cases;
- simple tasks require heavy setup;
- dependencies leak into core concepts;
- change radius grows;
- tests require large fixtures/context;
- agents need progressively more repository context for local changes;
- generated code volume grows much faster than capability;
- a framework begins defining domain architecture;
- unrelated refactoring appears in ordinary changes.

## Positive signs

- common examples become shorter;
- concepts and names become clearer;
- special cases disappear;
- boundaries stabilize;
- data structures become more natural;
- components can be replaced independently;
- tests become smaller and more behavioral;
- new changes touch fewer unrelated areas;
- agents can work effectively with a small causal/context neighborhood.

## Common useful boundaries

- domain vs UI;
- domain vs persistence;
- storage adapter;
- transport/auth/retry boundary;
- application composition vs reusable components;
- external service adapter;
- query vs storage representation;
- command/change intent vs persistence detail.

Do not create a boundary merely because one appears in this catalog. A useful boundary pays for itself by reducing coupling or protecting a likely change.

## Abstraction probes

When the correct abstraction is uncertain and AI makes experimentation cheap, generate two or more deliberately small competing implementations. Compare them by dependent-code simplicity, vocabulary, boundary clarity, dependency shape, and ease of later change. Do not select the largest or most complete candidate by default.
