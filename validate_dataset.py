#!/usr/bin/env python3
"""Validate structural quality of the portfolio CSV datasets.

This script checks file structure and allowed values. It does not assess
whether a label is semantically correct.
"""

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAIN_PATH = ROOT / "dataset.csv"
CHALLENGE_PATH = ROOT / "challenge_cases.csv"

LABELS = {"Positive", "Negative", "Neutral", "Complaint"}
MAIN_COLUMNS = ["ID", "Text", "Label"]
CHALLENGE_COLUMNS = ["Case_ID", "Text", "Expected_Label", "Decision_Rationale"]


def read_csv(path, required_columns, errors):
    if not path.exists():
        errors.append(f"{path.name}: file not found.")
        return []

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                errors.append(f"{path.name}: missing header.")
                return []
            if reader.fieldnames != required_columns:
                errors.append(
                    f"{path.name}: expected columns {required_columns}, "
                    f"found {reader.fieldnames}."
                )
                return []
            return list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{path.name}: could not read CSV: {exc}")
        return []


def validate_rows(path, rows, id_column, text_column, label_column,
                  rationale_column, errors):
    seen_ids = set()
    seen_text = set()
    counts = Counter()

    for line, row in enumerate(rows, start=2):
        record_id = (row.get(id_column) or "").strip()
        text = (row.get(text_column) or "").strip()
        label = (row.get(label_column) or "").strip()

        if not record_id:
            errors.append(f"{path.name}:{line}: empty {id_column}.")
        elif record_id in seen_ids:
            errors.append(f"{path.name}:{line}: duplicate ID {record_id!r}.")
        else:
            seen_ids.add(record_id)

        normalized_text = " ".join(text.split()).casefold()
        if not text:
            errors.append(f"{path.name}:{line}: empty {text_column}.")
        elif normalized_text in seen_text:
            errors.append(f"{path.name}:{line}: duplicate text after normalization.")
        else:
            seen_text.add(normalized_text)

        if label not in LABELS:
            errors.append(
                f"{path.name}:{line}: invalid label {label!r}; "
                f"allowed: {', '.join(sorted(LABELS))}."
            )
        else:
            counts[label] += 1

        if rationale_column and not (row.get(rationale_column) or "").strip():
            errors.append(f"{path.name}:{line}: empty {rationale_column}.")

    print(f"\n{path.name}: {len(rows)} records")
    print(f"  Unique IDs: {len(seen_ids)}")
    print(f"  Unique normalized texts: {len(seen_text)}")
    if label_column:
        print("  Label distribution:")
        for label in sorted(LABELS):
            print(f"    {label}: {counts[label]}")

    return counts


def main():
    errors = []
    main_rows = read_csv(MAIN_PATH, MAIN_COLUMNS, errors)
    challenge_rows = read_csv(CHALLENGE_PATH, CHALLENGE_COLUMNS, errors)

    main_counts = validate_rows(
        MAIN_PATH, main_rows, "ID", "Text", "Label", None, errors
    )
    validate_rows(
        CHALLENGE_PATH, challenge_rows, "Case_ID", "Text",
        "Expected_Label", "Decision_Rationale", errors
    )

    if not main_rows:
        errors.append("Main dataset contains no usable records.")
    if not challenge_rows:
        errors.append("Challenge dataset contains no usable records.")

    print(f"\nMain dataset total: {sum(main_counts.values())}")

    if errors:
        print(f"\nVALIDATION FAILED: {len(errors)} issue(s)")
        for issue in errors:
            print(f"- {issue}")
        return 1

    print("\nVALIDATION PASSED: structural checks found no issues.")
    print("This result does not establish semantic label correctness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
