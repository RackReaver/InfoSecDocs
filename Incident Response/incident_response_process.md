# Incident Response Process

When an event is determined to be an incident this process should be followed.

| Document Version | Status    | Published Date | Last Reviewed | Next Review |
| ---------------- | --------- | -------------- | ------------- | ----------- |
| 0.1.0            | Published | 2022/01/11     | 2022/01/11    | N/A         |

## Point of Contact Table

|                       |                                             |
| --------------------- | ------------------------------------------- |
| Document Owner        | [RackReaver](https://github.com/RackReaver) |
| Document Controller   | [RackReaver](https://github.com/RackReaver) |
| Document Creator      | [RackReaver](https://github.com/RackReaver) |
| Subject Matter Expert | [RackReaver](https://github.com/RackReaver) |

## Table of Contents

- [Incident Naming Convention](#incident-naming-convention)
- [Starting an Incident Steps](#starting-an-incident-steps)

## Incident Naming Convention

```
YYYYMMDD-X
 |   | | |
 |   | | +-- [X] Increment when multiple incident occur in a single day
 |   | |
 |   | +-- [DD] Day
 |   |
 |   +-- [MM] Month
 |
 +-- [YYYY] Year
```

## Starting an Incident Steps

1. Create a PRIVATE slack channel using the [incident naming convention](#incident-naming-convention).

2. Paste the following into the slack channel and pin it:

   > :warning: THIS IS STRICTLY CONFIDENTIAL AND SHOULD NOT BE SHARED OUTSIDE THIS CSIRT TEAM :warning:

3. Generate a folder using the [incident naming convention](#incident-naming-convention) inside of the incidents folder
   .

<!-- TODO: Add Incident Log Template to repo and link it below -->

4. Add the Incident Log Template to the new incident folder

5. Link new Incident Log to the slack channel and pin it
