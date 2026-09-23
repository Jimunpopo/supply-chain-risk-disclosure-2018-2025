"""Verify original source bytes, including CSVs inside lossless ZIP archives."""
import hashlib
import json
import zipfile
from pathlib import Path


def sha256_stream(source):
    digest = hashlib.sha256()
    for chunk in iter(lambda: source.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest()


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "04_data_verification/file_manifest.json").read_text(encoding="utf-8"))
    failures = 0
    for entry in manifest["files"]:
        path = root / entry["path"]
        archive_path = root / entry["archive_path"] if "archive_path" in entry else None
        matches = False
        try:
            if path.is_file():
                with path.open("rb") as source:
                    matches = path.stat().st_size == entry["size_bytes"] and sha256_stream(source) == entry["sha256"]
            elif archive_path is not None and archive_path.is_file():
                with archive_path.open("rb") as source:
                    archive_ok = archive_path.stat().st_size == entry["archive_size_bytes"] and sha256_stream(source) == entry["archive_sha256"]
                with zipfile.ZipFile(archive_path) as archive:
                    info = archive.getinfo(path.name)
                    with archive.open(info) as source:
                        matches = archive_ok and info.file_size == entry["size_bytes"] and sha256_stream(source) == entry["sha256"]
            print(f"{'OK' if matches else 'MISSING OR CHANGED'} {entry['path']}")
        except (OSError, KeyError, zipfile.BadZipFile) as error:
            print(f"ERROR {entry['path']}: {error}")
        failures += not matches
    print(f"Checked {len(manifest['files'])} original files; {failures} failures.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
