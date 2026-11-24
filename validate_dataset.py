#!/usr/bin/env python3
"""Validate the structure of dataset.csv for the text-classification project."""

import csv
import sys
from collections import Counter
from pathlib import Path

DATASET_PATH = Path(__file__).with_name("dataset.csv")
REQUIRED_COLUMNS = {"ID", "Text", "Label"}
ALLOWED_LABELS = {"Positive", "Negative", "Neutral", "Complaint"}


def main():
    if not DATASET_PATH.exists():
        print(f"ERROR: Dataset file not found: {DATASET_PATH}")
        return 1

    with DATASET_PATH.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print("ERROR: Dataset is empty or has no header.")
            return 1

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing_columns:
            print("ERROR: Missing required columns:", ", ".join(sorted(missing_columns)))
            return 1

        rows = list(reader)

    errors = []
    seen_ids = set()
    label_counts = Counter()

    for line_number, row in enumerate(rows, start=2):
        record_id = (row.get("ID") or "").strip()
        text = (row.get("Text") or "").strip()
        label = (row.get("Label") or "").strip()

        if not record_id:
            errors.append(f"Line {line_number}: missing ID.")
        elif record_id in seen_ids:
            errors.append(f"Line {line_number}: duplicate ID {record_id!r}.")
        else:
            seen_ids.add(record_id)

        if not text:
            errors.append(f"Line {line_number}: empty Text field.")

        if label not in ALLOWED_LABELS:
            errors.append(
                f"Line {line_number}: invalid Label {label!r}. "
                f"Allowed labels: {', '.join(sorted(ALLOWED_LABELS))}."
            )
        else:
            label_counts[label] += 1

    print(f"Records checked: {len(rows)}")
    print(f"Unique non-empty IDs: {len(seen_ids)}")
    print("Label distribution:")
    for label in sorted(ALLOWED_LABELS):
        print(f"  {label}: {label_counts[label]}")

    if errors:
        print(f"\nValidation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nValidation passed: no structural issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
