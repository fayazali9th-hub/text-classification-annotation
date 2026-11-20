# Annotation Guidelines

## 1. Objective
Assign exactly one primary label to each text sample.

## 2. Labels

### Positive
Use when the text expresses satisfaction, praise, gratitude, or a favorable experience.
Examples: "The support team solved my issue quickly." / "I love this product."

### Negative
Use when the text expresses an unfavorable opinion, disappointment, or dissatisfaction, but does not request a specific remedy for a reported issue.
Examples: "The battery life is disappointing." / "The website is confusing."

### Neutral
Use when the text is factual, descriptive, or logistical and does not express clear sentiment or request resolution.
Examples: "The meeting is at 3 PM." / "The package contains two notebooks."

### Complaint
Use when the text reports a specific service/product/account/payment problem, especially when it requests help, correction, investigation, replacement, refund, or another remedy.
Examples: "I was charged twice. Please refund the extra payment." / "My order has not arrived; please locate it."

## 3. Decision procedure
1. Read the complete text.
2. Does it report a specific problem and request action or resolution? If yes, choose **Complaint**.
3. Otherwise, does it express a favorable opinion or satisfaction? Choose **Positive**.
4. Otherwise, does it express an unfavorable opinion or dissatisfaction? Choose **Negative**.
5. Otherwise, choose **Neutral**.

## 4. Important distinctions
- A negative opinion alone is **Negative**, not automatically a Complaint.
- A specific problem plus a request for action is **Complaint**.
- A factual statement about an order or product is **Neutral** unless it reports a problem.
- If a text contains mixed sentiment, prioritize an explicit unresolved problem/request for action as **Complaint**. If there is no such request, use the dominant sentiment.

## 5. Annotation requirements
- Assign one label only.
- Do not infer facts that are not stated.
- Preserve the original text.
- If a sample cannot be labeled confidently, flag it for review rather than inventing context. (This demonstration dataset contains assigned labels for all rows.)

## 6. Scope
These guidelines are designed for this illustrative portfolio dataset. A real annotation task must follow the client's task-specific taxonomy and adjudication rules.
