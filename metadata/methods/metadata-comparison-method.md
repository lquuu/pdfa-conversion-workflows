# Metadata Extraction and Comparison Method

## Purpose

This document describes the method used to extract, pair, and compare metadata between original Microsoft Word documents (DOC/DOCX) and their converted PDF/A outputs. The goal of this process is to evaluate how document conversion impacts descriptive and technical metadata relevant to digital preservation and access.

This method supports batch-level analysis and is designed to scale beyond single-file testing.


---


## Scope

This method applies to:

- Original files: DOC and DOCX, including legacy 1997-2003 DOCs
- Converted files: PDF/A-2u (and PDF/A-2b, where applicable)
- Metadata extraction using ExifTool
- Batch orchestration using PowerShell
- Field-level comparison using Python


---


## Prerequisites

Before running this workflow, ensure that:

- ExifTool is installed and available via the system PATH
- PowerShell is available (Windows)
- Python 3 is installed
- The following scripts are available:
  - `scripts/run_pairs.ps1`
  - `scripts/compare_single_row_csvs.py`

- Original and converted files exist in separate directories


---


## Overview of the Process

The metadata comparison workflow consists of four stages:

1. Extract metadata from original DOC/DOCX files
2. Extract metadata from converted PDF/A files
3. Pair original and converted files
4. Compare selected metadata fields and generate reports

Each stage is described in detail below.


---


## 1. Metadata Extraction (Per-File CSVs)

Metadata is extracted from files using ExifTool, with each file producing a single CSV output containing one row of metadata fields.

Metadata extraction is performed separately for:
- Original DOC/DOCX files
- Converted PDF/A files

This design prioritizes auditability and one-to-one comparison over schema normalization.


### 1.1 Metadata Extraction from Original Files

ExifTool is run on each DOC/DOCX file to produce a single-row CSV containing all available metadata fields for that file.

Each CSV represents exactly one source document.

The resulting file contains one metadata object per source file.


### 1.2 Metadata Extraction from Converted PDF/A Files

ExifTool is run on each converted PDF/A file to produce a corresponding single-row CSV.

Original and converted CSVs are later paired using filename-based logic.


## 2. File Pairing Logic

Each original file is paired with its converted counterpart based on a shared base filename.

Pairing assumptions:

- One CSV corresponds to one original file
- One CSV corresponds to one converted file
- Filenames (excluding extensions) match exactly
- Pairing is one-to-one

Files that cannot be paired are excluded from comparison.


---


## 3. Metadata Field Selection

Not all metadata fields are directly comparable across file formats. This method prioritizes metadata fields that are relevant to preservation, access, and discovery.

### Core Comparison Fields

Typical fields of interest include:

- Title
- Author / Creator
- Subject
- Keywords
- Language (when present)
- CreateDate
- ModifyDate
- CreatorTool / Producer

File-system-level attributes (e.g., file size, file path) and format-specific internal identifiers are excluded from direct comparison unless explicitly required for analysis.


---


## 4. Automated Metadata Comparison

Metadata comparison is performed by a Python script that compares two single-row CSV files (original vs converted) and outputs a long-form comparison table.


### 4.1 Running the PowerShell Wrapper

The PowerShell script orchestrates the comparison process by invoking the Python comparison script for each file pair.

```
& C:\path\to\metadata\scripts\run_pairs.ps1 `
    -origDir C:\path\to\original_DOC_DOCX `
    -pdfDir C:\path\to\converted_PDF_A `
    -workDir C:\path\to\metadata_output `
    -pythonScriptPath C:\path\to\metadata\scripts\compare_single_row_csvs.py
```

Parameter definitions:

- `origDir`: directory containing original DOC/DOCX files
- `pdfDir`: directory containing converted PDF/A files
- `workDir`: output directory for extracted metadata and comparison results
- `pythonScriptPath`: path to the Python comparison script


### 4.2 Python-Based Field Comparison

The Python script (`compare_single_row_csvs.py`) performs the following steps:

- Reads two single-row metadata CSV files (original and converted)
- Computes the union of all metadata fields across both files
- Compares values field by field
- Classifies each field as:
  - Unchanged
  - Modified
  - Added in converted
  - Removed from original
- Writes a long-form CSV with one row per metadata field


---


## 5. Outputs

The metadata comparison workflow produces the following outputs:

metadata/
├── originals_csv/
│   └── <filename>_original.csv
├── converted_csv/
│   └── <filename>_converted.csv
└── results/
    └── <filename>_metadata_comparison.csv

Each comparison CSV contains:
- Base filename
- Metadata field name
- Original value
- Converted value
- Change status


---


## Implementation Notes

Batch extraction and orchestration are handled via a PowerShell script, which invokes ExifTool and a Python comparison script. The PowerShell layer manages paths and batch coordination, while the Python script performs pairing and field-level comparison.

Implementation details are documented separately in the `metadata/scripts/` directory.


---


## Limitations

- Metadata schemas differ significantly between DOC/DOCX and PDF/A formats
- Some metadata changes are expected and may not indicate loss
- Pairing relies on consistent file naming
- This method does not assess PDF tagging or accessibility structure

These limitations should be considered when interpreting results.

---

## Relation to Access Evaluation

While metadata extraction is often treated as a preservation concern, this method explicitly supports access evaluation by identifying metadata fields relevant to discovery, reuse, and text-based interaction.

Metadata comparison results may be used in conjunction with other analyses (e.g., text extractability, language stress tests) to assess the suitability of PDF/A outputs as access formats.


---
