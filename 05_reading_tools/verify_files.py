"""Verify release files and unchanged CSV data sections against the manifest."""
import codecs
import hashlib
import json
import zipfile
from pathlib import Path


def sha256_stream(source):
    digest = hashlib.sha256()
    for chunk in iter(lambda: source.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest()


def verify_file_stream(source, entry):
    """Check exact release bytes and, for CSVs, the original table bytes."""
    full_digest = hashlib.sha256()
    table_digest = hashlib.sha256()
    size = 0
    is_csv = entry['path'].endswith('.csv')
    first = True
    valid_header = not is_csv
    for chunk in iter(lambda: source.read(1024 * 1024), b''):
        full_digest.update(chunk)
        size += len(chunk)
        table_chunk = chunk
        if first and is_csv:
            if table_chunk.startswith(codecs.BOM_UTF8):
                table_chunk = table_chunk[len(codecs.BOM_UTF8):]
            valid_header = table_chunk.startswith(b'code,industry,year,denom,')
        if is_csv:
            table_digest.update(table_chunk)
        first = False
    matches = size == entry['size_bytes'] and full_digest.hexdigest() == entry['sha256']
    if is_csv:
        matches = matches and valid_header and entry['header_row'] == 1
        matches = matches and table_digest.hexdigest() == entry['data_section_sha256']
        matches = matches and table_digest.hexdigest() == entry['source_data_section_sha256']
    if entry.get('transformation') == 'none':
        matches = matches and entry['sha256'] == entry['source_sha256']
    return matches


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "04_data_verification/file_manifest.json").read_text(encoding="utf-8"))
    failures = 0
    for entry in manifest["files"]:
        path = root / entry["path"]
        archive_path = root / entry["archive_path"] if "archive_path" in entry else None
        matches = True
        found = False
        try:
            if path.is_file():
                found = True
                with path.open("rb") as source:
                    matches = verify_file_stream(source, entry) and matches
            if archive_path is not None and archive_path.is_file():
                found = True
                with archive_path.open("rb") as source:
                    archive_ok = archive_path.stat().st_size == entry["archive_size_bytes"] and sha256_stream(source) == entry["archive_sha256"]
                with zipfile.ZipFile(archive_path) as archive:
                    archive_ok = archive_ok and archive.namelist() == [path.name]
                    info = archive.getinfo(path.name)
                    with archive.open(info) as source:
                        matches = verify_file_stream(source, entry) and archive_ok and matches
            matches = matches and found
            print(f"{'OK' if matches else 'MISSING OR CHANGED'} {entry['path']}")
        except (OSError, KeyError, zipfile.BadZipFile) as error:
            matches = False
            print(f"ERROR {entry['path']}: {error}")
        failures += not matches
    print(f"Checked {len(manifest['files'])} release files; {failures} failures.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
