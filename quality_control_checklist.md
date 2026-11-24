# Quality Control Checklist

## Before Annotation
- [ ] Confirm the current task taxonomy and version.
- [ ] Read all label definitions and precedence rules.
- [ ] Review positive, negative, neutral, and complaint examples.
- [ ] Confirm the expected output schema and allowed values.
- [ ] Ask for clarification when task instructions conflict.

## For Each Record
- [ ] Read the complete message.
- [ ] Identify the primary communicative purpose.
- [ ] Check whether an unresolved issue requires intervention.
- [ ] Apply the decision order in `annotation_guidelines.md`.
- [ ] Use only evidence in the text.
- [ ] Assign exactly one permitted label.
- [ ] Flag genuinely ambiguous cases instead of guessing.

## Before Batch Submission
- [ ] Run `python3 validate_dataset.py`.
- [ ] Confirm record counts and label distribution.
- [ ] Check duplicate IDs and duplicate text.
- [ ] Review a sample of records for label-boundary errors.
- [ ] Confirm that no records were silently dropped or altered.
- [ ] Record the dataset and guideline version used.

## Independent Review
- [ ] Hide original labels from the second annotator.
- [ ] Select a documented sample.
- [ ] Preserve independent labels before discussion.
- [ ] Record disagreements in `annotation_audit_template.csv`.
- [ ] Adjudicate disagreements with written reasons.
- [ ] Report sample size, raw agreement, and an appropriate agreement statistic.
- [ ] Do not claim independent review or agreement until it has happened.

## Important
A structurally valid CSV is not necessarily a semantically accurate dataset. Automated checks and human review address different quality risks.
