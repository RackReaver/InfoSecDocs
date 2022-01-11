# Git for Document Management

How to manage documents using git (and GitHub which is my remote repo of choice).

| Document Version | Status      | Published Date | Last Reviewed | Next Review |
| ---------------- | ----------- | -------------- | ------------- | ----------- |
| 0.0.1            | In Progress | N/A            | N/A           | N/A         |

## Point of Contact Table

| Role                  | PoC                                         |
| --------------------- | ------------------------------------------- |
| Document Owner        | [RackReaver](https://github.com/RackReaver) |
| Document Controller   | [RackReaver](https://github.com/RackReaver) |
| Document Creator      | [RackReaver](https://github.com/RackReaver) |
| Subject Matter Expert | [RackReaver](https://github.com/RackReaver) |

## Table of Contents

- [Creating commits](#creating-commits)
  - [Example commits](#example-commits)
- [Creating and managing branches](#creating-and-managing-branches)
  - [Example branches](#example-branches)

## Creating commits

This becomes difficult because all of the standards (i.e. conventional commits) revolves around software development and not document management. A new standard had to be created to allow for documents and are layed out as follows:

| type   | description                                             |
| ------ | ------------------------------------------------------- |
| new    | When a document is being added to the repo for tracking |
| add    | When new text is added to an existing document          |
| update | When text is changed in an existing document            |
| style  | No text is changed only formatting                      |
| chore  | Changes not affecting documents                         |

### Example commits

- new: Create incident response process document
- add: Add point of contact table to incident response process
- update: Change document owner to john doe
- style: Change location of table of contents
- chore: Move incident response plan to incident response folder

## Creating and managing branches

Branches follow the same methodology that is used in software development. If a document needs to be added or altered a branch is created and all changes are made before making a pull request to update the main production documents.

### Example branches

- new/incident-response-process
- add/add-point-of-contacts-to-incident-response-process
- update/change-incident-response-process-document-owner
- style/change-incident-response-process-table-of-contents-location
- chore/move-incident-response-plan-to-incident-response-folder
