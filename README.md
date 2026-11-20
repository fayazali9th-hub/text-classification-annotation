# Text Classification Annotation Project

## Project overview
A small, manually labeled example dataset demonstrating four-way text classification. The records are illustrative examples created for this portfolio project; they are not customer records or production data.

## Objective
Assign one primary label to each text sample using the annotation rules in `annotation_guidelines.md`.

## Label set
- **Positive** — expresses satisfaction, praise, or a favorable experience.
- **Negative** — expresses an unfavorable opinion or dissatisfaction without making a specific request to resolve an identifiable service/product issue.
- **Neutral** — provides information or asks a factual question without clear positive/negative sentiment or a service-resolution request.
- **Complaint** — reports a specific problem and/or requests investigation, correction, replacement, refund, or other resolution.

## Dataset
- 50 illustrative text samples
- CSV format
- Columns: `ID`, `Text`, `Label`
- 4 labels, 12–13 examples per label

## Repository contents
| File | Description |
|---|---|
| `dataset.csv` | Labeled text samples |
| `annotation_guidelines.md` | Label definitions and decision rules |
| `evaluation_report.md` | Dataset summary and quality checks |
| `error_analysis.md` | Ambiguity notes and likely edge cases |

## Quality-control approach
The dataset is checked for required columns, unique IDs, missing values, allowed labels, and label counts. Ambiguous cases are discussed in `error_analysis.md`. These checks validate structure and consistency; they do not constitute independent inter-annotator agreement or expert certification.

## Limitations
This is a small, synthetic demonstration dataset. It does not establish professional annotation experience, model performance, or real-world generalization. A production project would require multiple annotators, adjudication, and agreement metrics.

## Skills demonstrated
Text classification, applying annotation guidelines, structured CSV preparation, label consistency checks, and basic dataset quality assurance.
