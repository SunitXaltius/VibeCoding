# MiniMart Prompt Log

This file records important AI prompts and the changes that the learner accepts.

## Milestone 1 — 2026-08-19

### Prompt summary

Create the MiniMart beginner e-commerce application as a sequence of small, explained milestones. Begin only with the project plan and a Flask home page connected to a Bootstrap template. Use the specified Flask, SQLite, security, testing, logging, and deployment tools, and stop after the first milestone for learner review.

### Proposed change

- Add one Flask route for the home page.
- Add a reusable HTML base template that loads Bootstrap 5.
- Add a home-page template that extends the base template.
- Pin Flask as the only dependency needed for this milestone.
- Add beginner setup, planning, risk, and testing guidance to `README.md`.

### Acceptance status

Accepted when the learner replied “continue.”

## Milestone 2 — 2026-08-19

### Prompt summary

Continue to the next published milestone after the Flask home page: introduce the SQLite data structure and a small public product catalogue while keeping the change suitable for a beginner.

### Problem and risk reviewed

MiniMart cannot store or list products yet. Invalid table rules could permit bad data, and unsafe search SQL could allow injection.

### Accepted change

- Add all four planned SQLite tables with basic data checks and foreign keys.
- Add a database connection helper and an idempotent example-data script.
- Add a public catalogue route with parameterised product search.
- Add a Bootstrap catalogue template and navigation link.
- Ignore the generated database and other local files in Git.

The learner's “continue” approved starting the next milestone already listed in the course plan.
