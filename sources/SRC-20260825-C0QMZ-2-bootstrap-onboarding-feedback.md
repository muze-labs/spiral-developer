---
id: SRC-20260825-C0QMZ-2
---

# Source: Bootstrap Onboarding Feedback

**Audience:** Internal review feedback from human and AI perspectives
**Type:** Composite feedback document
**Origin:** Human review + AI analysis of Spiral Developer project

## Legend

- 🤖 = AI or Automated Agent
- ❗ = Concern / Problem
- 🧑 = Human Agent
- 💭 = Idea / Thought
- 🧑💻 = Software Agent (either human or AI)
- 💡 = Suggested Solution
- ❓ = Question
- ➡ = Already mentioned in the original brief review

## Generic Questions

- ❓ Is the project understandable for human and AI agents?
- ❓ Are there optimizations that make the project easier to use by an AI agent?
- ❓ What is missing when trying to use / understand the project?
- ❓ Speaking as a wizard: Where is the boundary?
- ❓ Why do none of the documents contain a table of content (ToC)?
- ❓ Why do a lot of the documents not contain a header beyond h2?

## Ideas

- 💭 Idea: A tutorial or onboarding-specific agent might be in order
- 💭 Idea: Add `audience` as frontmatter to all documents
- 💭 Idea: I am not convinced having the prose (Markdown files) and machine-readable (Turtle files) in the same directory is a good idea.

### Code Quality

- - ❓🧑💻 Question: The Python script is only used by the Node.js script to parse TTL files. Is there a reason everything isn't either Python or Node.js?
- - ➡ ❗🧑💻 Concern: For a project that contains a lot of prose and structured data, I would expect (at the very least) CI/CD for spelling, grammar, and formatting.
  - 💡 Suggested solution: Add tools linting prose (ReMark, Markdownlint, etc.) and data, and run them as part of the CI/CD pipeline.

### Project Structure

- - ❗🤖🧑 Concern: The repo is both verbose (many files in the project) and too indistinct (to many folders in the project root) for an agent to easily comprehend. The risk is that either a human or AI agent will have to read/parse too many resources to understand the project.
  - 💡 Suggested solution: Creat clear (i.e. domain distinguishable) directories and move current directories into those as subdirectories.
- - ❗🤖🧑 Concern: None of the directories have a `README.md` file. This means that an agent, when entering a directory, does not have a clear starting point.
  - 💡 Suggested solution: Add a `README.md` file to every directory (or at least to those of human interest).
    Specifically, as that means having to parse multiple locations to get a complete picture, and that makes it harder to move all the TTL files to a different source (for instance, a different repository or Solid POD).
- - ❗🧑💻 Concern: Besides prose, the project contains source code (`requirements.txt`, `bin/`).
  - 💡 Suggested solution: As that code only seems to be needed by the GitHub Actions, I would advise to move it to a separate directory.
- - ❗🤖🧑 Concern: The project seems to have invented its own jargon instead of using naming already present in the work field.
  - 💡 Suggested solution: Rename (or relate) current naming to existing AI naming conventions: `AGENTS.md`, `BOOT.md`, `BOOTSTRAP.md`, `CONTEXT.md`, `DESIGN.md`, `IDENTITY.md`, `MEMORY.md` and `memory/YYYY-MM-DD.md`, `PLANS.md`, `SOUL.md`, `USER.md`, `skills/` and `skills/{skill-name}/SKILL.md`, etc. Or describe why things DO NOT fulfill the mentioned file functions.

### AGENTS.md

- - ❗🤖 Concern: The `AGENTS.md` file is more than 300 lines. This suggests that the file tries to contain too much information.
  - 💡 Suggested solution: Split the `AGENTS.md` file into multiple files, getting more detailed when going deeper into the directory structure.
- - ❗🤖 Concern: The `AGENTS.md` does not appear to have been written with an AI in mind. It lacks structure and logical progression. (i.e. hodgepodge writing).
  - 💡 Suggested solution: Add a section at the beginning of the file that describes how the file is organized, how edits/changes should be made, and which structure is followed.

### README.md

- - ➡ ❗🧑 Concern: The `README.md` does not appear to have been written with a human in mind.
    1. There is no clear high-level summary
    2. The prose goes into too many details too fast
    3. There is no possibility to drill-down / zoom-in
    4. The "Working model" section is just a wall of text.
    5. The "Who should read what" section only contains two lines of who should read what.
       The rest is an index of the `docs/` directory.
    6. ➡ The "Repository structure" section is useless. It lists content but adds no details for the listed files/folders.
  - 💡 Suggested Solution: Rewrite the `README.md` to be more human-friendly.
- - ❗🤖 Concern: The `README.md` does not appear to have been written with an AI in mind.
  - Place a warning / message at the top of the file that non-human agents should read the `AGENTS.md` instead

- - ❗🤖🧑 Concern: The "Who should read what" section only appears after 40 lines of prose.
  - 💡 Suggested Solutions: Move the section further up the document.

### package.json

- - ❓ Question: Not sure why this file is in the project. Is this project meant to be used as a Node.js package?
     Should probably be in the .github folder?
- - ❗🧑💻 Concern: contains `node --test` but there are no tests.
  - 💡 Suggested Solution: Remove
- - ❗🧑💻 Concern: There is no `dist/`, `coverage/`, `.env`, `*.log`.
  - 💡 Suggested Solution: Remove

### CONTRIBUTING.md

- - ❗🧑 Concern: human collaborator's operational guide does not easily read for humans.
  - 💡 Suggested Solutions: Rewrite the guide to be more human-friendly. (See various points from the README.md feedback).


- - ❓ Question: "Contributing _with_ Spiral Developer" or "Contributing _to_ Spiral Developer"
- - ❓ Question: Contains a section "Starting a brownfield project" and a section "Existing projects". Are those not the same?

### quickstart.md

- - ❗🤖🧑 Concern: It unclear whether this file is meant for a human agent, or AI, or both. Based on the name I would expect it to be for a human agent.
  - 💡 Suggested Solutions: Rewrite the quickstart to be human-only, add a `BOOTSTRAP.md` for robots.
    - See https://docs.openclaw.ai/reference/templates/BOOTSTRAP

- - ❓ Question: "Use Spiral Developer on one bounded real cycle" WTF is a bounded real cycle?
- - ❗🧑 Concern: It is common for the first paragraph in a document to be some sort of summary or starting point.
     "Do not bootstrap a heavyweight process first." does not appear to make sense in either direction.
- - ❓ Question: "Do not create empty artifacts for completeness." Does this mean it _will_ create empty directories?

### prompts/

- - ❗🧑 Concern: Not sure who this is for or how it should be used
  - 💡 Suggested Solution: See Project Structure


<!--

## Comparison with AI Review (@REVIEW.md)

### 🧑 Found by Human only

- **Tutorial/onboarding agent idea:** A dedicated agent for tutorials/onboarding is suggested; the AI review does not propose this.
- **Add `audience` frontmatter:** Suggested for all documents; not mentioned by the AI.
- **CI/CD for prose quality:** Expectation of spelling, grammar, and formatting linting for prose and structured data; the AI recommends general linting but not specifically for prose quality.
- **Mixed Markdown/Turtle in same directory:** Concern that combining prose and machine-readable files makes it harder to get a complete picture or migrate TTL files elsewhere; not flagged by the AI.
- **Source code mixed with prose:** `bin/` and `requirements.txt` should be moved to a separate directory; the AI does not raise this.
- **AGENTS.md length and structure:** >300 lines, lacks structure and logical progression for AI consumption; the AI does not specifically critique AGENTS.md.
- **README.md human-unfriendliness:** No high-level summary, details too fast, no drill-down, "Working model" wall of text, "Who should read what" incomplete, "Repository structure" useless.
- **README.md AI-unfriendliness:** No warning that non-human agents should read AGENTS.md instead.
- **README.md section ordering:** "Who should read what" appears after 40 lines of prose.
- **package.json oddities:** Purpose unclear; contains `node --test` but no tests exist; missing standard artifacts (`dist/`, `coverage/`, `.env`, `*.log`).
- **CONTRIBUTING.md:** Title ambiguity ("Contributing _with_ Spiral Developer" vs "_to_"); duplicate sections ("Starting a brownfield project" vs "Existing projects"); not human-friendly.
- **quickstart.md specific confusing phrases:** "bounded real cycle", "Do not bootstrap a heavyweight process first", "Do not create empty artifacts for completeness".
- **prompts/ directory:** Unclear purpose and audience.
- **"Where is the boundary?":** The "wizard" question about project boundaries; not addressed by the AI.
- **Lack of ToC / shallow headers:** Questions about why documents lack a table of contents and why many stop at h2; the AI notes documentation volume but not these specific structural gaps.

### 🤖 Found by AI only

- **No local enforcement:** No pre-commit hook, no `spiral check` command; CI only detects malformed causal commits after they enter branch history.
- **Git version requirement:** `git merge-tree --write-tree` requires Git 2.38+; undocumented and unchecked at runtime.
- **Monolithic CLI:** `bin/spiral.mjs` is a single 410-line file with no internal modules or unit tests.
- **SHACL shapes never executed:** `ontology/spiral-developer-shapes.ttl` exists but `spiral-rdf.py` does not load/run SHACL validation.
- **Allocation lock fragility:** 30-second stale threshold allows race conditions if allocation exceeds threshold.
- **Discourse-commitment-execution collaboration tax:** The framing-challenge requirement may be experienced as ceremonial or burdensome; recommendation for trust calibration.
- **Implementation lineage cost:** No materiality thresholds; routine bugfixes burdened with same provenance work as semantic changes.
- **Progressive-development hypothesis untested:** No empirical evidence that causal context accumulation reduces agent context load; recommendation to instrument dogfooding.
- **CI example duplication:** `examples/ci/github-spiral-integration.yml` is identical to `.github/workflows/spiral-integration.yml`.
- **Open questions (5):** Adoption target (Muze-only vs. general), process-vs-tool boundary, causal graph read/write ratio, 6-month failure mode, agent compatibility beyond the creating agent.
- **Positive assessment (6 strengths):** Conceptual model coherence, honest trust model, real dogfooding, forward-looking RDF choice, elegant culture/warning-profile separation, testable progressive-development hypothesis.
- **Specific high-priority recommendation table:** 11 prioritized recommendations from High to Low.

### 🤖🧑 Found by both

- **Dual runtime:** Human questions why Python and Node.js are both used (Python only parses TTL for Node); AI flags the fragility of requiring both runtimes for every consumer.
- **Documentation is overwhelming/voluminous:** Human questions about understandability, what is missing, and lack of ToC/headers imply the documentation is overwhelming and repetitive; AI quantifies ~2,500 lines across 19 files, core concepts repeated 3–5 times, and recommends a hub-and-spoke model.
- **quickstart.md is problematic:** Human notes unclear audience and confusing terminology ("bounded real cycle", "Do not bootstrap a heavyweight process first", "Do not create empty artifacts for completeness"); AI notes it references 15+ other files before the user creates their first artifact and contradicts its stated goal of not requiring the user to "study the whole methodology."
- **Documentation needs better human-friendly structure:** Both flag README, CONTRIBUTING, and quickstart as needing rewrites that are easier for humans to read and navigate.
- **Brownfield intake has issues:** Human notes "Starting a brownfield project" and "Existing projects" appear to be duplicate sections; AI notes the 11-topic intake is structurally heavy for teams evaluating adoption and recommends a lightweight vs. deep two-phase approach.
- **Process has invented jargon / too many concepts:** Human notes the project uses its own naming instead of established AI conventions; AI notes the enumeration of 19+ artifact types, 14+ relations, 6 statuses, etc. normalizes creation beyond a useful minimal core.
- **Project structure needs clearer hierarchy:** Human recommends clear domain-distinguishable directories with README.md and AGENTS.md per directory; AI recommends reducing the initial documentation surface and consolidating or stabilizing the runtime boundary.


-->