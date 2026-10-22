# pitch-sources-ivan

A practical workbook and source library for structuring, drafting, and improving a startup pitch.

Built for an early-stage, approximately 15-minute startup pitch with a separate hardware demonstration and no funding ask. The outline is a synthesis of the sources, adapted to that context; it is not an official YC or Sequoia template.

## Start here

| What you need | Open | What you get |
| --- | --- | --- |
| Turn an idea into an argument | **[Starting guide](docs/start-here.md)** | A short workflow and the role of each method |
| Draft the pitch | **[Copy the workbook](templates/pitch-workbook.md)** | Eight sections with prompts, evidence notes, and a narrative outline |
| Improve an existing draft | **[Review checklist](docs/improve-your-pitch.md)** | Questions, common structural repairs, and a review record |
| Learn from an example | **[Guided examples](docs/examples.md)** | Specific pages to study, useful techniques, and limits of borrowing them |

Read on GitHub and copy the workbook into Google Docs, Word, or Markdown. No installation or full-library reading is required. The **[eight-section content specification](docs/pitch-structure.md)** remains the foundation; the workbook helps you apply it. Follow the **[working principles](docs/principles.md)** throughout.

Sections define what the argument must cover, not a fixed number of slides. Keep evidence beside its claim and supporting detail in the appendix. Treat customer need as the starting point for technology choices.

## PDF structures and pitch examples

| Material | Open | Role |
| --- | --- | --- |
| Our agreed outline | [PDF](docs/pitch-structure.pdf) | Printable section requirements |
| Sequoia-style template | [PDF](library/pdfs/sequoia-pitch-deck-template.pdf) | Content prompts; PitchDeckCoach reproduction |
| NABC value proposition | [PDF](library/pdfs/nabc-value-proposition.pdf) | Need, approach, benefits/costs, and alternatives |
| Intercom's first pitch | [PDF](library/pdfs/intercom-first-pitch-deck.pdf) | Eight-page early-stage startup example |
| LinkedIn Series B | [PDF](library/pdfs/linkedin-series-b-2004.pdf) | Investor example; use with the [founder's critique](https://www.reidhoffman.org/linkedin-pitch-to-greylock/) |

Use the [guided examples](docs/examples.md) to understand what to borrow and what to question. Real decks contain weaknesses as well as useful techniques. For readable-slide revisions, start with [YC's illustrated before-and-after examples](https://www.ycombinator.com/blog/how-to-design-a-better-pitch-deck/).

## What is included

- A starting guide, fill-in workbook, review checklist, and guided examples.
- YC and Sequoia guidance; IDEO, NABC, Duarte, Heilmeier, a16z, and supporting evidence and slide-design methods.
- Mistake guides from YC, Hustle Fund, and a16z.
- LinkedIn and Intercom pitch decks; linked Sandbox VR and Nancy Duarte videos.
- Seven downloaded PDFs, two original editable PowerPoint files, and our printable outline.
- A [machine-readable catalogue](sources.json), with provenance, download status, page counts, file sizes, and SHA-256 checksums.
- Notes on [similar Git repositories](docs/similar-repositories.md).

Find the source summaries in the [annotated reading list](docs/reading-list.md) and every included file in the [download library](library/README.md). The catalogue distinguishes publisher files, mirror copies, and our own generated document. Several sources publish articles or videos rather than standalone downloadable presentations; those remain linked. No videos have been downloaded. File availability was checked on **22 October 2026**.

## File checks and downloads

<details>
<summary>Optional maintenance commands</summary>

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

</details>

## Contributing

Add a source only when it brings a useful method, a concrete mistake, or an instructive example. Prefer an author's or publisher's page. Record mirrors explicitly, distinguish examples from templates, and describe what evidence an example illustrates. Add any downloaded file to the catalogue and verify it before committing.

Third-party copyrights and existing notices are retained. This private collection has no blanket redistribution license; see [third-party material notes](THIRD_PARTY.md) and the rights information in the catalogue.
