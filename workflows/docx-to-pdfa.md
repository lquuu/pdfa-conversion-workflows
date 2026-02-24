# Adobe Acrobat Create PDF: Batch Conversion Workflow

## 1. Purpose

This workflow describes a reproducible process for batch-converting DOC and DOCX files to PDF using Adobe Acrobat’s **Create PDF** tool.

This workflow serves as a baseline conversion method for **comparison** against PDF/A-specific workflows (e.g., Guided Actions targeting PDF/A-2u), and is included to document observed behavior, stability, and limitations during batch processing.


---


## 2. Inputs & Preconditions

- Source files: DOC and DOCX only, including legacy 1997–2003 DOC files
- Files may be added individually or via folders
- Mixed file types (e.g., LNK, JPG, existing PDFs) should be excluded prior to conversion
- Adobe Acrobat is installed and licensed


---


## 3. Batch Conversion via Create PDF

### 3.1 Selecting Multiple PDF Files for Conversion

1. Open Adobe Acrobat
2. Select **Menu** from the top left corner
3. Under **Create**, select **Create multiple PDF files**

<img src="../screenshots/adobe-ui/create-regular-pdf-a/1-create-multiple-pdf-files.png"
     alt="Adobe Acrobat Create multiple PDF files menu"
     width="700">


---


### 3.2 Add Files for Batch Conversion

4. Select **Add files**

<img src="../screenshots/adobe-ui/create-regular-pdf-a/2-add-files-or-folder.png"
     alt="Create multiple PDFs dialog with Add files option"
     width="700">


5. Select a folder or specific DOC/DOCX files in the pop-up window and click **Open**

<img src="../screenshots/adobe-ui/create-regular-pdf-a/3-open-files.png"
     alt="File picker window showing selecting DOC/DOCX files and clicking Open"
     width="700">


6. Click **OK**

<img src="../screenshots/adobe-ui/create-regular-pdf-a/4-multiple-pdf-files-OK.png"
     alt="Create multiple PDFs dialog showing selected files and OK button"
     width="700">


---


### 3.3 Configure Output Settings

7. Under **Target Folder**, select **A Folder on My Computer**. Then click **Browse…** and select the destination folder for converted PDFs.

<img src="../screenshots/adobe-ui/create-regular-pdf-a/5-browse-target-folder.png"
     alt="Target Folder setting showing Browse option to choose output folder"
     width="700">


8. Under **File Naming**, select **Keep original file names**

<img src="../screenshots/adobe-ui/create-regular-pdf-a/6-keep-original-name.png"
     alt="File Naming setting showing Keep original file names selected"
     width="700">


9. Ensure **Overwrite existing files** is unchecked. (Default is checked; and we typically need to uncheck it. However, you may choose to keep it checked due to specific needs.)

<img src="../screenshots/adobe-ui/create-regular-pdf-a/7-uncheck-overwrite.png"
     alt="Option to overwrite existing files shown unchecked"
     width="700">


---


### 3.4 Run the Batch Conversion

10. Select **OK** to begin the conversion process
11. When the process completes, review any error messages or warnings


---


## 4. Outputs

- Standard PDF/A files saved to the designated output folder
- File naming preserved from original DOC/DOCX sources


---


## 5. Observed Behavior

Based on batch testing, the following behaviors have been observed when using "Create PDF" for large or mixed document sets:

- Increased likelihood of application crashes when processing mixed file types (e.g., `.png`) or shortcut (i.e., `.lnk`) files
- Reduced stability when processing deeply nested folder structures
- Limited transparency into batch-level failures without manual inspection

These behaviors may vary depending on file composition and system state.


---


## 6. Known Limitations

- Output files are **not** PDF/A compliant by default
- Unicode text mapping is not explicitly enforced
- Batch reports are limited compared to Guided Actions
- Less control over downstream preservation and access characteristics


---


## 7. Relation to Other Workflows

This workflow is intended to function as a baseline comparison for PDF/A-specific workflows documented elsewhere in this repository, including:
- `docx-to-pdfa2u-custom-action.md`


---

