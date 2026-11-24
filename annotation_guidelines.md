# Annotation Guidelines

## 1. Task

Assign **one primary label** to each text sample. Read the complete message before choosing a label. Use only information stated in the text; do not guess the writer's intention or add missing context.

This project uses a four-label, mutually exclusive taxonomy. **Complaint takes priority** when a message reports an active problem and seeks a remedy. Otherwise, classify the message by its expressed sentiment or informational content.

## 2. Label Definitions

### Positive
Use when the message expresses satisfaction, praise, gratitude, or a favorable experience, and does not contain an unresolved issue that requires action.

Examples:
- "The support team solved my issue quickly."
- "I am happy with the quality of this purchase."

### Negative
Use when the message expresses dissatisfaction, disappointment, criticism, or an unfavorable experience, but does not ask for a specific remedy or action on an active problem.

Examples:
- "The battery life is disappointing."
- "The website is confusing and difficult to navigate."

### Neutral
Use when the message is factual, descriptive, logistical, or a straightforward question without clear positive or negative sentiment and without an active complaint.

Examples:
- "The appointment is scheduled for Thursday at 3 PM."
- "Does this laptop support an external monitor?"

### Complaint
Use when the message reports a specific product, service, delivery, billing, account, or access problem and requests help or another form of resolution. Also use Complaint when an active issue clearly requires intervention, even if the request is implied rather than phrased as a question.

Examples:
- "I was charged twice. Please refund the extra payment."
- "My order has not arrived. Can you locate it?"
- "The account is locked and I cannot access my paid subscription."

## 3. Decision Order

Apply these steps in order:

1. **Is there a specific, active problem that needs intervention or resolution?** If yes, label **Complaint**.
2. If not, **does the message express a favorable experience or satisfaction?** If yes, label **Positive**.
3. If not, **does it express dissatisfaction or an unfavorable opinion?** If yes, label **Negative**.
4. If none of the above apply, label **Neutral**.

The order matters. A message can sound negative and still be a Complaint. When it reports an active problem requiring action, Complaint is the primary label.

## 4. Edge-Case Rules

- **Negative opinion without a remedy request:** Negative. Example: "The screen is too dim outdoors."
- **Problem plus request for action:** Complaint. Example: "The screen stopped working. Please arrange a repair."
- **Factual status update:** Neutral unless it reports an unresolved problem that needs intervention.
- **Resolved issue with satisfaction:** Positive. Example: "The replacement arrived and works perfectly. Thank you."
- **Mixed praise and active complaint:** Complaint if an unresolved issue still requires action.
- **Mixed praise and criticism without an action request:** Use the dominant overall sentiment.
- **Rhetorical or indirect wording:** Label the meaning conveyed by the full message, not a single word.
- **Unclear context:** Do not invent missing details. Flag the sample for review if the workflow allows it.

## 5. Annotation Procedure

For each row:

1. Read the full text once for overall meaning.
2. Identify whether it describes an active issue requiring action.
3. Apply the decision order above.
4. Enter exactly one approved label.
5. Preserve the original text; do not rewrite or normalize it during labeling.
6. Flag genuinely ambiguous samples for review rather than guessing.

## 6. Quality-Control Checklist

Before submitting a batch, check that:

- Every record has one label.
- Every label matches the approved spelling and capitalization.
- The full message was considered.
- Complaint was not used for every negative opinion.
- Neutral was not used when the text clearly expresses sentiment or requests resolution.
- No facts or intentions were inferred beyond the text.
- Ambiguous cases are recorded for review.

## 7. Scope

These rules define the taxonomy for this portfolio exercise only. Client projects may use different label definitions, precedence rules, or escalation procedures. Always follow the task-specific instructions supplied for an actual annotation job.
