# End-to-End Workflow: DOC/DOCX → PDF/A-2u with Metadata Comparison

## 1. Overview

This orchestration workflow combines:
1) Adobe Acrobat Guided Actions to batch-convert DOC/DOCX files to PDF/A-2u, and
2) A scripted metadata extraction + comparison process…

This document is intentionally high-level.

Detailed, tool-specific steps are documented in the linked workflows and method documents below.

---

## 2. Inputs

- Source documents: DOC and DOCX (including legacy 1997–2003 DOC files)
- A destination folder for converted PDF/A-2u outputs
- A working/output folder for metadata CSVs and comparison results

---

## 3. Preconditions

- Adobe Acrobat is installed and licensed
- An Adobe Guided Action named **Save as PDF/A-2u** exists and is configured to save outputs to a local folder
- ExifTool is installed and available via the system PATH
- PowerShell is available (Windows)
- Python 3 is installed
- The following scripts are available in this repository:
  - `metadata/scripts/run_pairs.ps1`
  - `metadata/scripts/compare_single_row_csvs.py`

---

## 4. Recommended Folder Bundle Structure (Per Batch)

This workflow supports a folder-by-folder bundle structure to improve reproducibility and review.

```text
Folder_01/
├── originals/                 (DOC/DOCX inputs)
├── pdfa_2u/                   (PDF/A-2u outputs)
└── metadata/
    ├── originals_csv/         (per-file ExifTool CSVs for DOC/DOCX)
    ├── converted_csv/         (per-file ExifTool CSVs for PDF/A outputs)
    └── results/               (per-file comparison CSVs)
```

---

## 5. Complete Workflow

### 5.1 - Step 1: Convert DOC/DOCX to PDF/A-2u (Adobe Guided Actions)

Follow the detailed Adobe conversion workflow:
- `docx-to-pdfa2u-custom-action.md`

Expected outcome:
- PDF/A-2u files are created in the designated output folder (`pdfa_2u/`).

Optional artifact:
- Adobe’s Full report (HTML) may be saved as an additional record of the run.


### 5.2 - Step 2: Extract and Compare Metadata (PowerShell + Python)

Follow the detailed method documentation:
- `../metadata/metadata-comparison-method.md`

At a high level, this stage:
- Extracts metadata from each original DOC/DOCX as a single-row CSV
- Extracts metadata from each converted PDF/A-2u as a single-row CSV
- Pairs original and converted files using filename-based logic
- Produces long-form comparison tables (CSV) indicating whether each metadata field is unchanged, modified, added, or removed


### 5.3 - Step 3: Execution (PowerShell)

Run the PowerShell wrapper script to perform extraction and comparison.

Example (paths must not be quoted):

```
& C:\path\to\run_pairs.ps1 `
  -origDir C:\path\to\Folder_01\originals `
  -pdfDir C:\path\to\Folder_01\pdfa_2u `
  -workDir C:\path\to\Folder_01\metadata `
  -pythonScriptPath C:\path\to\compare_single_row_csvs.py
```

Parameter definitions:
- `origDir`: directory containing original DOC/DOCX files
- `pdfDir`: directory containing converted PDF/A-2u files
- `workDir`: directory where metadata CSVs and results will be written
- `pythonScriptPath`: path to the Python comparison script

---

## 6. Outputs

After completion, the bundle should include:
- Converted PDF/A-2u outputs
- Per-file metadata CSVs for originals and converted files
- Per-file metadata comparison CSVs in metadata/results/

These outputs support both:
- file-by-file auditability, and
- batch-level review and reporting.

---

## 7. Related Workflows

The following workflow is maintained as a baseline comparator:
- `docx-to-pdfa.md`

---

## 8. Known Limitations

- Pairing depends on consistent filenames between originals and converted outputs
- DOC/DOCX and PDF/A expose different metadata schemas; differences do not
automatically imply metadata loss
- This workflow does not assess PDF tagging or accessibility structure (PDF/UA)

For limitations specific to metadata comparison, see:
- `../metadata/metadata-comparison-method.md`
