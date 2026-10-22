# pitch-sources-ivan

Startup pitch sources, examples, and an evidence-based outline for a small team.

Built for an early-stage, approximately 15-minute startup pitch with a separate hardware demonstration and no funding ask. The outline is a synthesis of the sources, adapted to that context; it is not an official YC or Sequoia template.

## Start here

1. Use the **[eight-section pitch structure](docs/pitch-structure.md)** to divide content responsibilities and build the narrative. A [printable PDF](docs/pitch-structure.pdf) contains the same structure.
2. Follow the **[working principles](docs/principles.md)** for evidence, assumptions, comparisons, and visuals.
3. Choose readings from the **[annotated reading list](docs/reading-list.md)**: methods, mistakes, and examples.
4. Open the **[download library](library/README.md)** for decks, templates, and supporting reference PDFs.

Sections define what the argument must cover, not a fixed number of slides. Keep evidence beside its claim and supporting detail in the appendix. Treat customer need as the starting point for technology choices.

## What is included

- YC and Sequoia guidance; IDEO, NABC, Duarte, Heilmeier, a16z, and supporting evidence and slide-design methods.
- Mistake guides from YC, Hustle Fund, and a16z.
- LinkedIn and Intercom pitch decks; linked Sandbox VR and Nancy Duarte videos.
- Seven downloaded PDFs, two original editable PowerPoint files, and our printable outline.
- A [machine-readable catalogue](sources.json), with provenance, download status, page counts, file sizes, and SHA-256 checksums.
- Notes on [similar Git repositories](docs/similar-repositories.md).

The catalogue distinguishes publisher files, mirror copies, and our own generated document. Several sources publish articles or videos rather than standalone downloadable presentations; those remain linked. No videos have been downloaded. File availability was checked on **22 October 2026**.

## File checks and downloads

The files are already included. To verify them locally:

```sh
python3 scripts/verify_library.py
```

The verifier uses only Python's standard library. If `pypdf` is installed, it also checks PDF page counts. To restore missing third-party files using the recorded public download URLs:

```sh
python3 scripts/download_sources.py
```

The downloader requires Python 3 and `curl`. It checks each file against its recorded checksum and refuses changed downloads. It does not download linked webpages or videos. To restore one file, add `--id sequoia-template` (see IDs in the catalogue).

To rebuild our outline PDF, install `reportlab` in your own Python environment, then run:

```sh
python3 scripts/build_structure_pdf.py
```

Rebuilding can change the PDF checksum; update its metadata in `sources.json` after inspecting the result. The Markdown outline is the editable source of truth.

## Contributing

Add a source only when it brings a useful method, a concrete mistake, or an instructive example. Prefer an author's or publisher's page. Record mirrors explicitly, distinguish examples from templates, and describe what evidence an example illustrates. Add any downloaded file to the catalogue and verify it before committing.

Third-party copyrights and existing notices are retained. This private collection has no blanket redistribution license; see [third-party material notes](THIRD_PARTY.md) and the rights information in the catalogue.
