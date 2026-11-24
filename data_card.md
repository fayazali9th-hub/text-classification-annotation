# Data Card

## Dataset Identity
- Project: Text Classification Annotation Portfolio
- Main file: `dataset.csv`
- Challenge file: `challenge_cases.csv`
- Task: Assign one primary label to each English text message.
- Labels: Positive, Negative, Neutral, Complaint.

## Provenance
The main dataset and challenge cases are synthetic examples authored for this portfolio. They were not collected from customers, scraped from social media, or imported from a public benchmark. No personal data is intentionally included.

## Intended Use
- Demonstrating a documented annotation taxonomy.
- Practicing single-label text classification.
- Demonstrating CSV preparation and structural validation.
- Illustrating edge-case reasoning and an independent-review workflow.

## Out-of-Scope Uses
- Estimating real customer sentiment or complaint prevalence.
- Training or benchmarking a production classifier without further curation.
- Claiming externally validated annotation accuracy.
- Representing the examples as real customer feedback.

## Labeling Method
One label is assigned according to `annotation_guidelines.md`. Complaint takes precedence when an unresolved issue requires intervention. This is a project-specific rule; other tasks may separate sentiment and issue intent into distinct fields.

## Known Limitations
- Synthetic language may be cleaner and less diverse than naturally occurring text.
- The main dataset is deliberately close to class-balanced.
- English-only examples do not establish multilingual performance.
- Labels have not been independently double-annotated or adjudicated.
- Structural validation does not verify semantic correctness.
- No model training or predictive-performance evaluation is included.

## Maintenance
Any future data addition should record its provenance, license or permission basis, collection date, transformations, labeling method, and review status. Do not add external data unless its license and permitted use have been checked and documented.
