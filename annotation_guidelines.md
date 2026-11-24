# Annotation Guidelines

## 1. Task Definition

Assign exactly one primary label to each complete message:

- `Positive`
- `Negative`
- `Neutral`
- `Complaint`

Use only information present in the message. Do not infer facts, intent, urgency, or customer history that the text does not support.

This is a portfolio-specific taxonomy. A client-provided taxonomy always takes precedence in real annotation work.

## 2. Label Definitions

### Positive
Use when the message expresses satisfaction, praise, gratitude, or a favorable experience, with no unresolved issue requiring action.

Examples:
- "The support team solved my issue quickly."
- "The replacement arrived and works perfectly. Thank you."

### Negative
Use when the message expresses dissatisfaction, disappointment, criticism, or an unfavorable opinion, but does not describe an active problem requiring intervention.

Examples:
- "The battery life is disappointing."
- "The website is confusing and difficult to navigate."

### Neutral
Use for factual, descriptive, logistical, or straightforward informational content without clear positive/negative sentiment or an unresolved issue requiring action.

Examples:
- "The appointment is scheduled for Thursday at 3 PM."
- "Does this laptop support an external monitor?"

### Complaint
Use when a message reports a specific unresolved product, service, delivery, billing, subscription, or access problem that needs assistance or another resolution. A direct request is not required when the need for intervention is clear.

Examples:
- "I was charged twice. Please refund the extra payment."
- "My order has not arrived. Can you locate it?"
- "The account is locked and I cannot access my paid subscription."

## 3. Decision Procedure

Apply this order consistently:

1. **Is there a specific unresolved problem that needs intervention?** If yes, choose Complaint.
2. **If not, does the message express satisfaction or a favorable experience?** If yes, choose Positive.
3. **If not, does it express dissatisfaction or criticism?** If yes, choose Negative.
4. **Otherwise**, choose Neutral.

The key boundary is not whether the wording sounds angry. It is whether the message describes an unresolved issue requiring action.

## 4. Edge-Case Rules

| Situation | Rule |
|---|---|
| Negative opinion, no active issue | Negative |
| Specific unresolved problem, remedy requested | Complaint |
| Specific unresolved problem, remedy implied | Complaint |
| Factual status update, no issue | Neutral |
| Issue explicitly resolved and satisfaction expressed | Positive |
| Praise plus unresolved issue requiring action | Complaint |
| Praise plus criticism, no action needed | Use dominant overall sentiment |
| Strong or angry wording without a resolvable issue | Negative |
| Factual question | Neutral |
| Question asking for help with a specific failure | Complaint |
| Missing context | Do not guess; flag for review if the workflow supports it |

## 5. Annotation Procedure

For every record:

1. Read the entire message.
2. Identify the main communicative purpose.
3. Check for an unresolved issue that requires intervention.
4. Apply the decision procedure.
5. Assign one approved label only.
6. Preserve the original text exactly.
7. Flag ambiguous cases rather than inventing context.
8. Keep a note when a decision depends on a non-obvious boundary.

## 6. Quality-Control Rules

Before submitting a batch, verify:

- Every record has exactly one approved label.
- The full message was considered.
- Complaint is not used for every negative opinion.
- Neutral is not used for clear sentiment or an active problem.
- Resolved issues are not treated as active complaints.
- No unsupported context or intent was inferred.
- Ambiguous records are flagged for review.
- Any guideline change is versioned and communicated to all annotators.

## 7. Escalation and Adjudication

When two annotators disagree:

1. Preserve both original labels.
2. Record the exact guideline rule each annotator applied.
3. Identify whether the disagreement concerns text interpretation or an unclear guideline.
4. Have a designated reviewer make an adjudicated decision.
5. Record the final label and a concise rationale.
6. Update the guide only when the disagreement exposes a reusable rule.

Never overwrite independent labels with the adjudicated label; retain all three fields for auditability.

## 8. Scope

These definitions are specific to this portfolio exercise. Production annotation projects may define sentiment, complaint, urgency, intent, and escalation differently. Follow the task-specific instructions and escalation policy supplied for each real project.