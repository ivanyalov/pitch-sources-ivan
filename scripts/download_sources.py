#!/usr/bin/env python3
"""Restore catalogued public files without accepting silent source changes."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def signature_ok(path, fmt):
    with path.open('rb') as stream:
        prefix = stream.read(8)
    return prefix.startswith(b'%PDF-') if fmt == 'pdf' else prefix == bytes.fromhex('d0cf11e0a1b11ae1')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--id', help='Download only this artifact ID')
    args = parser.parse_args()
    items = json.loads((ROOT / 'sources.json').read_text())['artifacts']
    if args.id and args.id not in {x['id'] for x in items}:
        parser.error('Unknown artifact ID')
    if not shutil.which('curl'):
        parser.error('curl is required')
    errors = []
    for item in items:
        if args.id and item['id'] != args.id:
            continue
        if not item.get('download_url'):
            print(f"SKIP {item['id']}: generated locally; see build instructions")
            continue
        dest = (ROOT / item['local_path']).resolve()
        if ROOT not in dest.parents:
            raise ValueError('Catalogue path escapes repository')
        if dest.exists():
            if hashlib.sha256(dest.read_bytes()).hexdigest() == item['sha256']:
                print(f"OK {item['id']}: already present")
            else:
                errors.append(f"{item['id']}: existing file has changed; left untouched")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=dest.parent) as tmp:
            candidate = Path(tmp) / 'download.part'
            result = subprocess.run([
                'curl', '--fail', '--location', '--proto', '=https', '--proto-redir', '=https',
                '--connect-timeout', '15', '--max-time', '120', '--silent', '--show-error',
                '--output', str(candidate), item['download_url']
            ], capture_output=True, text=True)
            if result.returncode:
                errors.append(f"{item['id']}: {result.stderr.strip()}")
            elif (not signature_ok(candidate, item['format']) or
                  hashlib.sha256(candidate.read_bytes()).hexdigest() != item['sha256']):
                errors.append(f"{item['id']}: format or checksum mismatch; not installed")
            else:
                candidate.replace(dest)
                print(f"SAVED {item['id']}")
    for error in errors:
        print('ERROR ' + error)
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
