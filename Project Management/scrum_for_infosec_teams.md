# SCRUM for Information Security Teams

| Document Version | Status    | Published Date | Last Reviewed | Next Review |
| ---------------- | --------- | -------------- | ------------- | ----------- |
| 0.1.0            | Published | 2022-02-17     | 2022-02-17    | Q1 2023     |

## Point of Contact Table

| Role                  | PoC                                         |
| --------------------- | ------------------------------------------- |
| Document Owner        | [RackReaver](https://github.com/RackReaver) |
| Document Controller   | [RackReaver](https://github.com/RackReaver) |
| Document Creator      | [RackReaver](https://github.com/RackReaver) |
| Subject Matter Expert | [RackReaver](https://github.com/RackReaver) |

## Table of Contents

- [Implementation Checklist](#implementation-checklist)
- [Schedule](#schedule)
- [Roles](#roles)
- [User Stories](#user-stories)
  - [Examples](#examples)
- [Product Backlog](#product-backlog)
  - [Start with the two "R"s](#start-with-the-two-"r"s)
- [Sprint](#sprint)
  - [Sprint Planning](#sprint-planning)
  - [Daily Scrum (standup)](#daily-scrum-standup)
  - [Sprint Review](#sprint-review)
  - [Sprint Retrospective](#sprint-retrospective)

## Implementation

### Checklist

1. Determine the teams product(s) that must be supported
2. Schedule [sprint planning](#sprint-planning) meetings
3. Schedule [daily scrum (standup)](#daily-scrum-standup) meetings
4. Schedule [sprint review](#sprint-review) meetings
5. Schedule [sprint retrospective](#sprint-retrospective) meetings

## Schedule

```
┌──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
│1.                    │2.                    │3.                    │4.                    │5.                    │
│                      │                      │                      │                      │                      │
│  - Daily Scrum       │  - Daily Scrum       │  - Daily Scrum       │  - Daily Scrum       │  - Daily Scrum       │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
├──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│6.                    │7.                    │8.                    │9.                    │10.                   │
│                      │                      │                      │                      │                      │
│  - Daily Scrum       │  - Daily Scrum       │  - Daily Scrum       │  - Daily Scrum       │  - Daily Scrum       │
│                      │                      │                      │                      │                      │
│                      │  - Backlog Grooming  │                      │                      │  - Sprint Review     │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │  - Sprint Retro      │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
│                      │                      │                      │                      │                      │
└──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┘
```

---

## Roles

- Product Owner (key stakeholder)
  - Manages and prioritizes the product backlog
- Scrum Master
  - Manages daily scrum and ensures backlog follows the teams standards
- Security Team
  - Commit to work pre-sprint that is achievable 98% of the time

## User Stories

Capture a description of a problem from a user's perspective. For security professionals our users are usually the companies employees or management, user stories should be outlined from their perspective. When writing user stories they should **NOT** be about how to achieve the desired functionality, they should only outline the users pain point.

### Examples

- Submitting phishing emails to security takes to long
- Send email logs to SIEM for incident response
- Alert operations whenever a service account gets locked out
- Provide management with 2022 PCI Attestation of Compliance

## Product Backlog

> **Ensure you have a well-groomed backlog with your priorities and dependencies in order. This can be a big challenge that could derail the process if it’s not properly managed.**

A prioritized, descriptive list of all documents, processes, features, functions, requirements, changes and fixes that are needed to produce and maintain the teams product(s). Product backlog items are usually based on user stories and should include clear tests that determine completion. The product backlog serves as the connection between the key stakeholder and the security team.

### Start with the two "R"s

A team's roadmap and requirements provide the foundation for the product backlog. Roadmap initiatives break down into several epics, and each epic will have several requirements and user stories.

## Sprint

Fixed length time-boxed period of one month or less during which one or more objectives of the overall project are accomplished.

### Sprint Planning

|          |                                            |
| -------- | ------------------------------------------ |
| Required | Security team, scrum master, product owner |
| When     | Beginning of a sprint                      |
| Duration | 1-4 hours                                  |

> **Be sure the team understands the sprint goal and how success will be measured.**

A collaborative event where the team answers two basic questions: What work can get done in this sprint and how will the chosen work get done?

1. The [product owner](#roles) discusses the objective that the sprint should achieve and the [product backlog](#product-backlog) items that, upon completion, would achieve the sprint goal.
2. Create a plan for how the team will build the backlog items and get them “Done” before the end of the sprint. The work items chosen and the plan for how to get them done is called the sprint backlog. By the end of sprint planning the team is ready to start work on the sprint backlog, taking items from the backlog, to “In-progress,” and “Done."

### Daily Scrum (standup)

|          |                                            |
| -------- | ------------------------------------------ |
| Required | Security team, scrum master, product owner |
| When     | Once per day, typically in the morning     |
| Duration | No more than 15 minutes                    |

The goal of this meeting is to surface any blockers and challenges that would impact the teams ability to deliver the sprint goal.

### Sprint Review

|          |                                            |
| -------- | ------------------------------------------ |
| Required | Security team, scrum master, product owner |
| Optional | Project stakeholders                       |
| When     | At the end of a sprint or milestone        |
| Duration | 1-2 hours                                  |

Team demonstrates what they’ve completed. This is your team’s opportunity to showcase their work to stakeholders and teammates and when documentation becomes published.

### Sprint Retrospective

|          |                                            |
| -------- | ------------------------------------------ |
| Required | Security team, scrum master, product owner |
| Optional | Project stakeholders                       |
| When     | At the end of an iteration                 |
| Duration | 45-90 minutes                              |

The teams opportunity to identify areas of improvement for the next sprint. Examples include: standardizing story descriptions, less/more daily scrum time, better scrum strategies, etc.
