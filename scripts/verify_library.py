#!/usr/bin/env python3
"""Check catalogue integrity, file coverage, and local Markdown links."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


def main():
    catalogue = json.loads((ROOT / 'sources.json').read_text())
    errors, tracked = [], set()
    sources = {s['id'] for s in catalogue['sources']}
    ids = [a['id'] for a in catalogue['artifacts']]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate artifact ID')
    if len(sources) != len(catalogue['sources']):
        errors.append('Duplicate source ID')
    for source in catalogue['sources']:
        for ident in source.get('artifact_ids', []):
            if ident not in ids:
                errors.append(f"{source['id']}: missing artifact reference {ident}")
    for item in catalogue['artifacts']:
        path = (ROOT / item['local_path']).resolve()
        tracked.add(path)
        if ROOT not in path.parents or not path.is_file():
            errors.append(f"Missing or unsafe path: {item['local_path']}")
            continue
        data = path.read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            errors.append(f"Integrity mismatch: {item['local_path']}")
        if item['format'] == 'pdf':
            if not data.startswith(b'%PDF-'):
                errors.append(f"Invalid PDF signature: {path.name}")
            elif PdfReader is not None and len(PdfReader(path).pages) != item['pages']:
                errors.append(f"PDF page count mismatch: {path.name}")
        elif data[:8] != bytes.fromhex('d0cf11e0a1b11ae1'):
            errors.append(f"Invalid PPT signature: {path.name}")
        if any(s not in sources for s in item['source_ids']):
            errors.append(f"Unknown source reference: {item['id']}")
    for folder in ['library/pdfs', 'library/presentations']:
        for path in (ROOT / folder).iterdir():
            if path.is_file() and path.resolve() not in tracked:
                errors.append(f"Uncatalogued file: {path.relative_to(ROOT)}")
    for path in [ROOT / 'README.md', ROOT / 'THIRD_PARTY.md', *(ROOT / 'docs').glob('*.md'), ROOT / 'library/README.md']:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            target = unquote(target.split('#')[0])
            if not (path.parent / target).exists():
                errors.append(f"Broken local link in {path.name}: {target}")
    outline = (ROOT / 'docs/pitch-structure.md').read_text()
    if len(re.findall(r'^## [1-8]\. ', outline, re.M)) != 8:
        errors.append('Expected eight numbered outline sections')
    for error in errors:
        print('ERROR ' + error)
    print(f"Checked {len(catalogue['sources'])} sources and {len(ids)} artifacts; {len(errors)} errors.")
    if PdfReader is None:
        print('PDF page-count validation skipped: optional pypdf is not installed.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
