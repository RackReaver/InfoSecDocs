# Security Organization Methodologies and Naming Standards

This markdown file contains all of my personal organization methodologies and naming standards for managing an information security program.

The goal is to streamline running a security team.

| Document Version | Status | Published Date | Last Reviewed | Next Review |
| ---------------- | ------ | -------------- | ------------- | ----------- |
| 0.0.0            | Draft  | TBA            | 2022-06-02    | Q2 2023     |

## Table of Contents

- [Folder Structures](#folder-structures)
- [Document Naming Standard](#document-naming-standard)
  - [Policies/Processes/Procedures](#policiesprocessesprocedures)
  - [Meeting Minutes/Notes](#meeting-minutesnotes)
- [Security Workflows/Processes](#security-workflowsprocesses)
  - [Ticket Workflow](#ticket-workflow)
  - [Weekly Information Security Engineer To-Do's](#weekly-information-security-engineer-to-dos)

---

## Folder Structures

Folder organization structure for file management.

```
/
+-- Information Security (Company Confidential)
+-- Information Security Team
|  |
|  +-- 1 - Team File Cabinet
|  |  |
|  |  +-- 1 - Inbox (uncategorized)
|  |  +-- Business Continuity
|  |  +-- Compliance
|  |  +-- Disaster Recovery
|  |  +-- Incident Response
|  |  +-- Phishing Management
|  |  +-- Risk Assessments
|  |  +-- Security Information and Event Management (SIEM)
|  |  +-- Vendors
|  |  +-- Vulnerability Management
|  |
|  +-- 2 - Policy/Process/Procedure Documents
|  |  |
|  |  +-- 0 - Templates
|  |  +-- 1 - Proposed
|  |  +-- 2 - Draft
|  |  +-- 3 - Awaiting Approval
|  |  +-- 4 - Approved
|  |  +-- 5 - Published
|  |  +-- 6 - Depreciated
|  |
|  +-- 3 - Data Lake
|  +-- 4 - Shared Documents
```

## Document Naming Standard

Current naming convention for files inside of my folder organization structure.

### Policies/Processes/Procedures

```
ISMS:<control mapping> - v1.0.0 - Document Name
 |    |                   | | |    |
 |    |                   | | |    +-- Name of document (ex. Incident Response Plan)
 |    |                   | | |
 |    |                   | | +-- Revision: Spelling fixes and formatting.
 |    |                   | |
 |    |                   | +-- Minor update: Non-Approved changes, review is needed before publishing.
 |    |                   |
 |    |                   +-- Major update: Reflects published policy change.
 |    |
 |    +-- Not required, used for linking to NIST, CIS, PCI, SOC or whatever control stack is needed.
 |
 +-- aka. Information Security Management System - Identifies the document as a policy, process or procedure.
```

### Meeting Minutes/Notes

```
YYYY-MM-DD - Meeting Name
 |    |  |    |
 |    |  |    +-- Name of meeting or calendar invite
 |    |  |
 |    |  +-- Day
 |    +-- Month
 +-- Year
```

## Security Workflows/Processes

Standardized workflows and processes.

### Ticket Workflow

When a ticketing methodology is not already used by the organization this is a good baseline to increase productivity and automated metrics.

```
                                     ┌──────────────────────┐
                                     ▼                      │
┌─────────┐   ┌──────┐   ┌─────────────┐     ┌─────────┐    │
│ Backlog ├──►│ ToDo ├──►│ In Progress ├────►│ Pending │    │
└─────────┘   └─┬────┘   └──┬──┬─┬─────┘     └────┬────┘    │
     ▲          │ ▲         │  │ │ ▲              │         │
     └──────────┘ └─────────┘  │ │ └──────────────┘         │
                               │ │                          │
              ┌──────┐         │ │    ┌──────────────────┐  │
              │ Done │◄────────┘ └───►│ Managers Approval│  │
              └──────┘                └─────────┬─┬──────┘  │
                  ▲                             │ │         │
                  └─────────────────────────────┘ └─────────┘
                             Approved               Denied
```

```
             ┌───────────────────────────────────────────────────────────────────┐
             │                                                                   │
             │                                                                   │
             │                                                                   │
             │                                                                   │
             │    ┌───────────┐     ┌────────────┐     ┌──────┐                  │
PROJECT/GOAL │    │ OBJECTIVE ├────►│ KEY RESULT ├────►│ EPIC │                  │
             │    └───────────┘     └────────────┘     └───┬──┘                  │
             │                                             │                     │
             │                                             │                     │
             │                                             │                     │
             │                                             │                     │
             ├─────────────────────────────────────────────┼─────────────────────┤
             │                                             │                     │
             │                                             │                     │
             │                                             │        ┌───────┐    │
             │                                             ├───────►│ STORY │    │
             │                                             │        └───────┘    │
 WORK/TASKS  │                                             │                     │
             │                                             │        ┌──────┐     │
             │                                             └───────►│ TASK │     │
             │                                                      └──────┘     │
             │                                                                   │
             │                                                                   │
             └───────────────────────────────────────────────────────────────────┘
```

### Weekly Information Security Engineer To-Do's

Root ticket and sub-tasks for tracking time.

```
  Weekly Information Security Engineer To-Do's
  |
  +-- Business Meetings
  +-- Admin Tasks
  +-- Threat/Vunerability Management
  +-- Log/Records Management
  +-- Incidents/Events
  +-- Automantion/Scripting
```
