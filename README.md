# PDF/A Conversion Workflows

This repository documents the evaluation of document conversion workflows from DOC and DOCX to PDF/A-2u and PDF/A-2b for digital preservation and access contexts. The project focuses on text extractability, metadata preservation, accessibility, and batch processing behavior in library and archival environments.

The work focuses on:

- Batch conversion behavior and stability
- Observed failures and limitations
- Metadata preservation across formats
- Accessibility and text-extractability
- Workflow documentation suitable for library reuse


---


## Context

This repository was developed as part of research conducted at the **University of Michigan Digital Preservation Lab** (DPL). The goal of this work is to produce reusable, well-documented workflows that can support long-term digital preservation and access in library and archival settings.

The work reflects my individual research, testing, and documentation; with the intention that the resulting workflows can be:
- Integrated into institutional preservation practices
- Used by future researchers and interns
- Shared publicly as a reference for similar preservation work


---


## Access Formats

While PDF/A is primarily a preservation format, this work explicitly evaluates conversion outputs as **access formats***. Particular attention is given to:

- Unicode text mapping and searchability (PDF/A-2u)
- Copy/paste fidelity for non-Latin scripts
- Metadata availability for discovery and reuse
- Accessibility considerations, including tagging and structure
- Tradeoffs between strict preservation compliance and practical access


---


## Start Here

Depending on your goals, you may wish to begin with one of the following workflows:

- **Baseline Conversion Behavior**: Overview of standard conversion behavior and baseline observations
  - `workflows/docx-to-pdfa.md`

- **PDF/A-2u Conversion Using Adobe Guided Actions**: Step-by-step workflow for producing PDF/A-2u using Adobe Acrobat
  - `workflows/docx-to-pdfa2u-custom-action.md`

- **End-to-End Workflow with Metadata Extraction & Comparison**: Complete workflow including conversion, metadata extraction, and comparison
  - `workflows/docx-to-pdfa2u-with-metadata.md`

- **Accessibility Evaluation**: Instructions for generating and interpreting accessibility reports in Adobe Acrobat
  - `workflows/accessibility-checker.md`

- **Detailed Metadata Extraction & Comparison Method**: Detailed documentation of how metadata is extracted and compared across files
  - `metadata/metadata-comparison-method.md`


---


## Repository Structure

This repository is organized to separate documentation, empirical evidence, and tooling:

/workflows
    Step-by-step guides for conversion workflows and accessibility evaluation

/samples
    Representative test files used to evaluate conversion quality
    Includes real archival documents and a comprehensive stress-test file

/reports
    Accessibility reports and batch conversion logs

/metadata
    Methods, scripts, and results for metadata extraction and comparison

/docs
    Decision logs, environment setup instructions, and research notes

/screenshots
    Images used in documentation and workflow guides

/README.md
    Project overview and navigation guide


---


## About the Samples

The sample files included in this repository were intentionally selected to represent a range of real-world preservation challenges:
- Legacy DOC files (1997–2003 formats)
- Non-Latin scripts (e.g., Chinese, Portuguese)
- Complex formatting, layout, and styling
- A comprehensive stress-test document designed to evaluate conversion robustness
- These samples support meaningful evaluation of conversion fidelity, accessibility, and metadata preservation.


---


## Reproducibility

This repository is designed to support reproducible digital preservation workflows. Documentation includes:
- Detailed step-by-step conversion instructions
- Environment setup guidance
- Decision logs explaining methodological choices
- Scripts for metadata comparison
- Accessibility evaluation procedures


---


## Intended Audience

This repository may be useful for:
- Digital preservation practitioners
- Library and archival professionals
- Researchers studying document conversion
- Students learning preservation workflows
- Institutions developing PDF/A policies


---


## Acknowledgments

This work was conducted as part of research at the **University of Michigan Digital Preservation Lab**. The documentation and workflows reflect individual research and testing conducted to support long-term preservation and access goals.