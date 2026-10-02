---
id: SRC-20261001-HZ4Q-2
---

# Source: Standing commit-attribution rule for agents

## Human direction

The human directed that Spiral Developer carry a standing commit-attribution rule, so that every agent working under the process attributes its commits the same way. The direction arrived as a conversational message rather than a written specification, and the human marked the substantive points as settled, not open to relitigation.

The rule and its stated reasoning:

- An agent's work is credited with a `Co-Authored-By` trailer.
- The human remains the author and the committer, so the commit remains signed and attributable to a verified account. An agent never goes in the author or committer field: Git binds a signature to the committer, so that placement gains nothing and forfeits the verified attribution.
- The trailer takes the form `Co-Authored-By: <Model Name> <ai+<model-slug>@muze.nl>`.
- `<Model Name>` is the model's published display name, used however the catalogue renders it. Many catalogues prefix `Vendor: ` and many deliberately omit it; follow the catalogue for the model in hand rather than imposing a form.
- `<model-slug>` is the model part of a catalogue identifier: after the vendor namespace, before any `:variant` suffix. For example `somevendor/space-bunny-alpha` yields `space-bunny-alpha`. The namespace is dropped because it is routing metadata rather than part of the model's name, and because it is redundant: no catalogue slug is shared by two vendors.
- A model's own vendor no-reply address is never used, however publicly it is documented. It asserts a vendor relationship in permanent history, on an address we neither control nor can have verified, and which the vendor may change or retire. The address belongs to whoever did the work.
- The address is subaddressed deliberately, so that creating `ai@muze.nl` as a catch-all later requires no change to any existing history.
- The model is identified from what the agent's own tooling reports for the session, rather than by assumption. How to obtain that is tool-specific.

## The variant question

The human initially held one element explicitly open, directing that it not be decided: how to treat a `:variant` suffix. The human asked that the analysis informing it be recorded, so that the gap was reasoned rather than merely noted.

The analysis supplied was that the variants which exist are serving modes rather than different models, keeping the same weights and the same context length while differing in price and turnaround. Anything that genuinely changes model identity is already a separate catalogue entry, and is therefore credited separately by construction. The likely rule was to collapse the variant and credit the base model, since a co-author line records which model wrote the code rather than how it was served. This was to be presented as a recommendation awaiting confirmation, not as a rule.

## Confirmation

Asked directly, the human confirmed: **collapse the variant and credit the base model**, and land the change as a proper Spiral cycle rather than a direct commit to the authoritative branch.

## Provenance note

This direction originated in an interactive session. The primary conversational evidence is not retained in the repository; this record is the retained capture of it. Where this record paraphrases the human's reasoning, the reasoning is preserved in substance rather than verbatim.