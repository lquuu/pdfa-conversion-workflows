# ⚙️ Setup Environment: PDF/A Conversion Workflows

## Purpose

This document describes how to configure the software environment used to develop and evaluate the PDF/A conversion workflows documented in this repository. The goal is to ensure that future researchers and practitioners can reproduce the workflows consistently and accurately.


---


## 1. Required Software

### Adobe Acrobat Pro

The primary tool used for document conversion and accessibility evaluation is Adobe Acrobat Pro.

This software is available to University of Michigan students and faculty through institutional licensing.

Key Features Used:

- Save as PDF/A-2u and PDF/A-2b
- Guided Actions for batch processing
- Accessibility Checker
- Metadata inspection tools
- Cloud-based auto-tagging for accessibility


---


## 2. Adobe Acrobat Configuration

### 2.1 Enable/Disable Cloud-Based Auto-Tagging

Cloud-based auto-tagging improves accessibility tagging for PDFs.

**Steps:**

1. Open Adobe Acrobat
2. Go to **Preferences**
    - Windows: Ctrl + K
    - macOS: Command + K
3. In the left panel, select **Accessibility**
4. Check/Uncheck **Enable cloud-based auto-tagging for accessibility** for your unique needs.
5. Click **OK**

This setting allows Adobe to use cloud-based AI services to improve document structure and tagging.


### 2.2 Configure PDF/A Conversion Settings

To ensure consistency, Adobe Acrobat must be configured to export documents as PDF/A-2u.

**Steps:**

1. Open a DOC or DOCX file in Adobe Acrobat
2. Select **Menu** (hamburger icon)
3. Go to:
    - Save As Other
    - Archival PDF

4. Click **Settings…**
5. Select **Save as PDF/A-2u**
6. Click **OK**

This configuration ensures that Unicode text mapping is preserved.


### 2.3 Create a Guided Action for Batch Conversion

Batch processing is performed using Guided Actions in Adobe Acrobat.

**Steps:**

1. Open **Adobe Acrobat**
2. Use the search bar and type: **Create New Action**
3. Under **Save & Export**, select **Save**
4. Click the **+** icon to add it to the action
5. Choose **Specify Settings**
6. Set:
    - **Export to:** PDF/A

7. Confirm settings and save the action

This allows multiple DOC/DOCX files to be converted to PDF/A-2u in a single workflow.


---


## 3. Accessibility Checker Setup

Adobe Acrobat’s Accessibility Checker is used to evaluate the accessibility of converted documents.

**Steps to Run Accessibility Checker:**

1. Open a PDF in Adobe Acrobat
2. On the left sidebar, select **Accessibility Full Check** (circle with checkmark icon)
3. Under **Report Options**, click **Choose…** to select a save location
4. Ensure all items under **Checking Options** are selected
5. Confirm the **Category** is set to **Document**
6. Click **Start Checking**
7. Review results in the **Accessibility Checker panel**

This process also generates a detailed accessibility report for each document, located in the location you specified in **Step 3**.


---


## 4. Metadata Extraction Environment

Metadata comparison is performed using Python scripts included in this repository.

**Required Tools**
- Python 3.x
- PowerShell (for batch execution on Windows)

**Repository Scripts**

Located in:
```
metadata/scripts/
```

Includes:
- `compare_single_row_csvs.py`
- `run_pairs.ps1`

These scripts automate metadata comparison between original and converted files.


---


## 5. File Organization Expectations

To ensure workflows function correctly, files should be organized as follows:

```
samples/
    original_docs/
    converted_pdfa_2u/
    metadata/
```

Maintaining this structure ensures compatibility with scripts and documentation.


---


## 6. Screenshots and Documentation

Screenshots referenced in workflow documentation are stored in:

```
screenshots/
```

These images support step-by-step instructions and help users visually verify settings.


---


## 7. Environment Summary
## Environment Summary

| Component            | Purpose                                                     |
|----------------------|-------------------------------------------------------------|
| Adobe Acrobat Pro    | PDF/A conversion and accessibility evaluation               |
| Cloud Auto-Tagging   | Tested; no measurable impact on final outputs               |
| Guided Actions       | Enables automated batch processing                          |
| Accessibility Checker| Evaluates accessibility compliance and document structure   |
| Python Scripts       | Performs metadata extraction and comparison                 |
| Repository Structure | Supports reproducibility and organized workflow execution   |


---


8. Reproducibility Notes

This environment was configured to ensure:
- Consistent PDF/A conversion results
- Reliable accessibility evaluation
- Repeatable metadata comparison
- Scalable batch processing

Future users should follow this setup guide before running any workflows in this repository.
