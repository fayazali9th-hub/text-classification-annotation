# Error Analysis and Label-Boundary Cases

## Purpose

This guide documents recurring confusion points in the four-label taxonomy. The examples are illustrative synthetic cases, not findings from an independent review of the 250-record dataset.

## 1. Negative vs Complaint

The deciding factor is whether an unresolved problem requires intervention.

| Message | Label | Reason |
|---|---|---|
| "The battery life is disappointing." | Negative | Dissatisfaction without an active request for intervention. |
| "The battery stopped working. Please replace it." | Complaint | Specific failure and remedy request. |
| "This app is frustrating and poorly designed." | Negative | Criticism, but no specific unresolved incident requiring action. |
| "I cannot log in because the password reset link is broken. Please help." | Complaint | Specific access failure requiring support. |

## 2. Neutral vs Complaint

| Message | Label | Reason |
|---|---|---|
| "The package was delivered to reception." | Neutral | Factual status information. |
| "The package was delivered to the wrong address. Please recover it." | Complaint | Delivery failure requiring action. |
| "My subscription renews on the first of each month." | Neutral | Factual information. |
| "I was billed after cancelling my subscription. Please reverse the charge." | Complaint | Billing issue requiring correction. |

## 3. Positive vs Complaint

| Message | Label | Reason |
|---|---|---|
| "The replacement arrived and works perfectly. Thank you." | Positive | The issue is resolved and satisfaction is expressed. |
| "The support agent was helpful, but my account is still locked." | Complaint | Praise does not remove the unresolved access problem. |
| "The delivery was quick and the packaging was excellent." | Positive | Favorable experience with no active issue. |

## 4. Mixed Sentiment

- "The product looks nice, but the screen is too dim for outdoor use." — **Negative**: criticism is the main point; no remedy is requested.
- "The parcel arrived, but one item is missing. Please send it." — **Complaint**: an unresolved fulfillment issue requires action.
- "The replacement arrived and works perfectly. I'm pleased with the solution." — **Positive**: the issue appears resolved.

## 5. Indirect and Ambiguous Requests

| Message | Suggested label | Rationale |
|---|---|---|
| "I have been waiting three weeks and still have no update on my refund." | Complaint | A specific unresolved refund issue is apparent even without a direct question. |
| "I wish this phone had a better camera." | Negative | Preference/criticism, not an active failure requiring intervention. |
| "Could someone explain how the loyalty points work?" | Neutral | Information request without a reported failure. |
| "My loyalty points disappeared after checkout. Can you restore them?" | Complaint | Specific account/reward issue requiring correction. |

If the text does not provide enough information to decide, flag it for review rather than guessing.

## 6. Taxonomy Risk

This project combines sentiment labels (Positive, Negative, Neutral) with a problem-resolution label (Complaint). These are not naturally mutually exclusive dimensions. The precedence rule makes a single-label exercise possible, but a production task may be better represented by separate fields such as:

- `sentiment`: positive / negative / neutral
- `issue_present`: yes / no
- `resolution_needed`: yes / no

Do not silently change the current project's taxonomy; follow the documented primary-label precedence.

## 7. Review Status

The examples in this document are illustrative decision cases. They are not an audit of the main dataset and do not establish that a second annotator agreed with the labels.

For a real error analysis, independently annotate a sample, compare labels, classify disagreement types, adjudicate each disagreement, and report the results with the sample size.