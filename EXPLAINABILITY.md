# Explainability

## Inputs and Data Sources

The agent accepts caller-provided role information, skills, topics, preparation goals, questions, and answers.

### Input Requirements

Each tool validates required fields, declared types, and unexpected fields before processing.

### Data Sources

The core implementation uses only caller-provided information. It does not silently retrieve job postings, employer systems, or external hiring data.

### Failure Handling

Missing required fields, invalid types, empty required text, and unexpected fields are rejected.

## Decision and Reasoning

The agent uses deterministic rules to organize preparation and review supplied material.

### Rules Applied

- `create-interview-plan` organizes supplied skills and topics into preparation areas.
- `generate-practice-questions` creates questions from explicitly supplied topics and question categories.
- `review-interview-answer` checks supplied answers against explicit criteria such as relevance, structure, specificity, and completeness.

### Expected Outputs

Outputs contain a preparation plan, practice questions, or structured feedback based on supplied inputs.

### Determinism

Identical valid inputs produce reproducible results.

## Limits and Constraints

The agent does not know an employer's private interview process unless that information is supplied by the caller.

### Constraints

Results depend on the completeness and accuracy of caller-provided role, skill, topic, question, and answer data.

### Known Issues

Generated practice questions are preparation exercises and are not claimed to be actual interview questions.

### Unsupported Behavior

The agent does not fabricate employer requirements, guarantee interview outcomes, contact recruiters, submit applications, or access private hiring systems.

## Tool Documentation

### create-interview-plan

#### Inputs
- role
- skills
- topics

#### Decision
Groups supplied preparation information into a deterministic interview-preparation plan.

#### Outputs
Returns structured preparation areas and suggested focus items.

#### Failure Handling
Rejects missing or malformed inputs.

#### Limits
The plan is based only on supplied information.

### generate-practice-questions

#### Inputs
- topics
- question_types

#### Decision
Generates deterministic practice questions for each supplied topic and requested question type.

#### Outputs
Returns structured practice questions.

#### Failure Handling
Rejects empty topics, malformed question types, and unexpected fields.

#### Limits
Questions are practice material, not verified employer questions.

### review-interview-answer

#### Inputs
- question
- answer
- criteria

#### Decision
Reviews the supplied answer against explicit criteria and reports observable strengths and improvement areas.

#### Outputs
Returns structured feedback and criterion-level observations.

#### Failure Handling
Rejects empty question or answer text and invalid criteria.

#### Limits
The review is based only on the supplied text and does not predict hiring decisions.

## Traceability

Every output is derived from explicit input values and documented rules.

## Transparency

The agent distinguishes supplied information, generated practice material, and analytical feedback.

## Reproducibility

The core tools are deterministic and produce the same output for identical valid inputs.

## Safety and Scope

The agent is a preparation aid. Users remain responsible for their own interview responses and decisions.
