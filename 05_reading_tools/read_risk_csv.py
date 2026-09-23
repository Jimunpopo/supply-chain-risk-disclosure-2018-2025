"""Read a risk CSV while preserving company codes and skipping source notes."""

import argparse
import csv
import itertools
import json
import io
import zipfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def open_risk_text(path):
    path = Path(path)
    if path.suffix == ".zip":
        with zipfile.ZipFile(path) as archive:
            names = [name for name in archive.namelist() if name.endswith(".csv")]
            if len(names) != 1:
                raise ValueError("Expected exactly one CSV in the ZIP archive")
            with archive.open(names[0]) as raw:
                with io.TextIOWrapper(raw, encoding="utf-8-sig", newline="") as text:
                    yield text
    else:
        with path.open(encoding="utf-8-sig", newline="") as text:
            yield text


def iter_risk_rows(path):
    """Yield dictionaries of strings; empty cells remain empty strings."""
    with open_risk_text(path) as source:
        reader = csv.reader(source)
        for line_number, fields in enumerate(reader, start=1):
            if all(key in fields for key in ("code", "year", "denom")):
                header = fields
                break
            if line_number >= 100:
                raise ValueError(f"Risk CSV header not found in {path}")
        else:
            raise ValueError(f"Risk CSV header not found in {path}")
        if len(set(header)) != len(header):
            raise ValueError(f"Duplicate columns in {path}")
        for fields in reader:
            if not fields or not any(fields):
                continue
            if len(fields) != len(header):
                raise ValueError(f"Column count differs at CSV line {reader.line_num}")
            yield dict(zip(header, fields))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--rows", type=int, default=3)
    args = parser.parse_args()
    if args.rows < 0:
        parser.error("--rows must be non-negative")
    for row in itertools.islice(iter_risk_rows(args.path), args.rows):
        print(json.dumps(row, ensure_ascii=False))


if __name__ == "__main__":
    main()
