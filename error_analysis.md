# Error Analysis and Ambiguity Notes

## Purpose

This document records label boundaries that are easy to confuse under the project's four-label taxonomy. The examples below illustrate how the decision rules should be applied; they are not an independent audit by a second annotator.

## 1. Negative vs Complaint

The key distinction is whether the message reports an active issue that requires intervention.

| Example | Label | Reason |
|---|---|---|
| "The battery life is disappointing." | Negative | Dissatisfaction is expressed, but no remedy is requested. |
| "The battery stopped working. Please replace it." | Complaint | A specific problem and a request for action are both present. |

## 2. Neutral vs Complaint

A factual update is not automatically a complaint. Look for an issue that requires intervention.

| Example | Label | Reason |
|---|---|---|
| "The package was delivered to reception." | Neutral | Factual delivery information. |
| "The package was delivered to the wrong address. Please recover it." | Complaint | Reports a delivery problem and asks for resolution. |

## 3. Mixed Sentiment

A message may contain both praise and criticism. If an unresolved issue still needs action, use Complaint. If no action is needed, use the dominant sentiment.

- "The product looks nice, but the screen is too dim for outdoor use." — **Negative** (ID 41): criticism is the main point; no remedy is requested.
- "The parcel arrived, but one item is missing. Please send it." — **Complaint** (ID 42): a missing item and a remedy request are stated.
- "The replacement arrived and works perfectly. I'm pleased with the solution." — **Positive** (ID 48): the issue appears resolved and the message expresses satisfaction.

## 4. Other Cases to Watch

- **Polite wording:** A polite request to fix a problem is still Complaint.
- **Strong wording:** An angry opinion without an active issue or remedy request is Negative, not automatically Complaint.
- **Questions:** A factual question is Neutral; a question asking for help with a specific problem is Complaint.
- **Resolved problems:** If the message confirms the issue is resolved and expresses satisfaction, use Positive unless a new active issue is raised.
- **Missing context:** Do not infer a problem from a vague statement. Flag it for review when possible.

## 5. Dataset Review Notes

The current file contains 50 synthetic examples with a nearly balanced label distribution. The existing labels and this analysis are based on the project's written decision rules. No independent second annotator or adjudicator has reviewed the records, so these notes must not be described as inter-annotator agreement or external validation.

## 6. Recommended Next Quality Step

Have another person independently annotate a sample without seeing the existing labels. Compare the two sets, document disagreements, adjudicate each difference, and revise the guidelines if the same confusion appears repeatedly. Calculate an agreement statistic only after the independent labels are collected.
