# PDF/A Conversion Workflows

This repository documents the evaluation of document conversion workflows from DOC/DOCX to PDF/A-2u and PDF/A-2b for digital preservation and access contexts, with a focus on text extractability, metadata preservation, and batch processing behavior.

The work focuses on:

- Batch conversion behavior and stability
- Observed failures and limitations
- Metadata preservation across formats
- Workflow documentation suitable for library reuse


---


## Context

This repository was developed as part of research conducted at the University of Michigan Digital Preservation Lab, with the goal of producing reusable, documented workflows suitable for library and archival environments.

The work reflects my individual research, testing, and documentation, and is intended both for integration into institutional repositories and for public reference.


---


## Access Formats

While PDF/A is primarily a preservation format, this work explicitly evaluates conversion outputs as *access formats*, with particular attention to:

- Unicode text mapping and searchability (PDF/A-2u)
- Copy/paste fidelity for non-Latin scripts
- Metadata availability for discovery and reuse
- Tradeoffs between preservation compliance and practical access


---


## Start Here

Readers may wish to begin with the following workflows, depending on their goals:

- **Baseline Conversion Behavior**
  - `workflows/docx-to-pdfa.md`

- **PDF/A-2u Conversion Using Adobe Guided Actions**
  - `workflows/docx-to-pdfa2u-custom-action.md`

- **End-to-End Workflow with Metadata Extraction & Comparison**
  - `workflows/docx-to-pdfa2u-with-metadata.md`

- **Detailed Metadata Extraction & Comparison Method**
  - `metadata/metadata-comparison-method.md`


---


## Repository Structure

This repository is organized to separate documentation, empirical evidence, and tooling:

- `workflows/` — Step-by-step conversion workflows intended for reuse
- `batch-testing/` — Batch testing logs and observed tool behavior
- `metadata/` — Metadata extraction methods, scripts, and comparison results
- `samples/` — Small representative input/output examples
- `figures/` — Screenshots and visual evidence referenced in documentation
- `reports/` — Interpretive summaries, limitations, and future research
