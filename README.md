# Text Classification Annotation Portfolio

A documented text-annotation project demonstrating a four-label classification workflow, explicit decision rules, edge-case handling, dataset validation, and a reproducible quality-review process.

> **Data disclosure:** The main dataset and challenge cases are synthetic examples created for this portfolio. They are not customer records, a licensed public benchmark, or evidence of production annotation work.

## Project at a Glance

| Item | Details |
|---|---|
| Task | Single-label text classification |
| Labels | Positive, Negative, Neutral, Complaint |
| Main dataset | 250 synthetic records |
| Challenge set | 30 synthetic edge cases with rationales |
| Data format | CSV |
| Validation | Python standard-library script |
| QA documentation | Annotation guide, error analysis, QC checklist, audit template, evaluation report |

## Label Taxonomy

| Label | Definition |
|---|---|
| **Positive** | Satisfaction, praise, gratitude, or a favorable experience without an unresolved issue requiring action. |
| **Negative** | Dissatisfaction or criticism without a specific active issue requiring intervention. |
| **Neutral** | Factual or informational content without clear sentiment or an active complaint. |
| **Complaint** | A specific unresolved problem that needs help, correction, investigation, replacement, refund, or another resolution. |

**Precedence rule:** Complaint takes priority when an unresolved issue requires intervention. Otherwise, classify the expressed sentiment or informational content. Apply the full decision guide in `annotation_guidelines.md`.

## Repository Contents

| File | Purpose |
|---|---|
| `dataset.csv` | 250 synthetic main-dataset records |
| `challenge_cases.csv` | 30 separate edge cases with expected labels and decision rationales |
| `annotation_guidelines.md` | Label definitions, decision tree, and annotation procedure |
| `error_analysis.md` | Common confusion pairs and edge-case decisions |
| `evaluation_report.md` | Dataset profile, validation scope, limitations, and next QA steps |
| `data_card.md` | Dataset provenance, intended use, risks, and limitations |
| `quality_control_checklist.md` | Batch-level and record-level review checklist |
| `annotation_audit_template.csv` | Blank template for independent review and adjudication |
| `validate_dataset.py` | Structural validation for both CSV datasets |

## Run Validation

Requires Python 3; no third-party packages are needed.

```bash
python3 validate_dataset.py
```

The validator checks required columns, malformed or empty fields, duplicate IDs, duplicate text, approved labels, and label distribution. It also validates the challenge-set schema and rationale fields.

**Important:** Passing validation means the files meet defined structural rules. It does not prove that a human-assigned label is semantically correct.

## Suggested Independent QA Workflow

1. Give a reviewer the annotation guidelines and a copy of the main dataset with the existing `Label` column hidden.
2. Ask the reviewer to label a randomly selected sample independently.
3. Record their decisions in `annotation_audit_template.csv`.
4. Compare the independent labels with the original labels.
5. Document disagreements and adjudicated outcomes with reasons.
6. For two annotators and nominal labels, calculate Cohen's kappa alongside raw agreement; interpret both in context.
7. Revise the guidelines if recurring disagreement reveals unclear rules.

Do not report agreement, accuracy, or adjudication results until this process has actually been completed.

## What This Demonstrates

- Applying a written classification taxonomy
- Distinguishing sentiment from action-requiring complaints
- Handling ambiguous and mixed-sentiment examples
- Preparing and inspecting structured CSV datasets
- Writing Python checks for data integrity
- Documenting limitations and a repeatable QA process

## Limitations

The datasets are synthetic and deliberately close to balanced. They do not represent real customer-message prevalence or establish performance on naturally occurring language. The current labels have not been independently double-annotated or adjudicated. No model training, benchmark performance, production-scale work, or inter-annotator agreement is claimed.

See `data_card.md` and `evaluation_report.md` for the full scope and limitations.