# Error Analysis and Ambiguity Notes

## Common confusion: Negative vs Complaint
- **Negative:** "The battery life is disappointing." This expresses dissatisfaction but does not ask for a remedy.
- **Complaint:** "The battery stopped working. Please replace it." This reports a specific issue and requests action.

## Common confusion: Neutral vs Complaint
- **Neutral:** "The package was delivered to reception." This is a factual statement.
- **Complaint:** "The package was delivered to the wrong address. Please recover it." This reports a problem and requests resolution.

## Mixed sentiment
A sentence can include praise and a problem. If it contains a specific unresolved issue and asks for action, label it Complaint. Otherwise, use the dominant sentiment.

## Review candidates
The following samples are useful for discussion during a portfolio review:
- ID 41: Mixed positive/negative wording; labeled Negative because the main point is an unfavorable product limitation and no remedy is requested.
- ID 42: Reports a missing item and requests that it be sent; labeled Complaint.
- ID 48: Describes a successful replacement and satisfaction; labeled Positive.

## Improvement plan
For a larger or client-facing dataset:
1. Have a second annotator label the same samples independently.
2. Compare disagreements and adjudicate them using the guidelines.
3. Calculate an agreement measure such as Cohen's kappa for two annotators.
4. Revise unclear rules and re-annotate affected records.
5. Keep an audit trail of guideline versions and adjudication decisions.
