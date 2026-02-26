# 📂 Sample Files Overview

This directory contains the representative sample documents used to evaluate PDF/A conversion workflows in this repository. The samples were intentionally selected to reflect a range of real-world digital preservation challenges, including legacy formats, multilingual content, and complex formatting.

Each sample includes:
- The original source document
- Converted versions in PDF/A-2u and PDF/A-2b
- Associated metadata extracted for comparison


---


## 🎯 Purpose of the Samples

The sample set was designed to support evaluation of:
- Text extractability and Unicode mapping
- Metadata preservation across formats
- Accessibility and document structure
- Layout fidelity and formatting stability
- Behavior of batch conversion workflows

By combining real archival documents with a comprehensive stress-test document, the samples enable both realistic and controlled testing scenarios.


---


## 📄 Sample Descriptions

### Sample 1 — Portuguese Legacy Document

**Source:** Acervo Mirasola Collection
**Format:** Microsoft Word 1997–2003 (`.doc`)
***Language:** Portuguese

#### Features

- Obsolete Word file format
- Multiple pages
- Bold and italicized text
- Multiple fonts and font sizes
- Non-English language content

#### Purpose

This sample represents authentic archival material and tests:
- Legacy format handling
- Multilingual text preservation
- Formatting fidelity in older documents


---


### Sample 2 — Traditional Chinese Document

**Source:** Ding-Jun Wang Collection
**Format:** Microsoft Word 1997–2003 (`.doc`)
**Language:** Traditional Chinese

#### Features

- Non-Latin script
- Multiple pages
- Consistent font size and alignment
- Page numbers in Arabic numerals
- Colored text (blue)


#### Purpose

This sample evaluates:
- Unicode text mapping
- Copy/paste fidelity for non-Latin scripts
- Metadata preservation for multilingual documents


---


### Sample 3 — Stress-Test Document

**Source:** Synthetic document created for testing
**Format:** Microsoft Word (`.docx`)
**Languages:** Multilingual (English, Chinese, Arabic, symbols)

#### Features

This document was intentionally designed to include a wide range of formatting and structural elements, including:
- Multiple languages & scripts
- Special characters & symbols
- Mathematical equations and LaTeX expressions
- Tables with varied borders and alignment
- Images with different wrapping styles
- WordArt and SmartArt elements
- Columns, lists, and complex spacing
- Headers & footers (with different first page)
- Page breaks
- Text boxes & overlays
- Accessibility edge cases


#### Purpose

This sample serves as a comprehensive robustness test to evaluate:
- Conversion stability
- Layout preservation
- Text extractability under complex conditions
- Accessibility and tagging behavior


---


## 📑 Included File Types

For each sample, the following versions are included:
- **Original** — The source DOC or DOCX file
- **PDF/A-2u** — Converted version with Unicode text mapping
- **PDF/A-2b** — Converted version with visual preservation
- **Metadata** — Extracted metadata for comparison

Including both PDF/A variants allows for direct comparison between:
- Preservation fidelity (PDF/A-2b)
- Preservation + accessibility (PDF/A-2u)


---


## 🔬 Research Value

The combination of these samples supports meaningful analysis of:
- Preservation vs. access tradeoffs
- Multilingual document behavior
- Accessibility considerations
- Metadata retention
- Real-world batch processing scenarios


---


## 📁 Folder Structure

Each sample follows the same internal structure:

```
sample-name/
├── original/
├── converted_pdfa_2u/
├── converted_pdfa_2b/
└── metadata/
```

This standardized structure ensures:
- Clear organization
- Easy comparison between versions
- Reproducibility of results


---


## 🌟 Final Note

These samples were selected and designed to provide a balanced and realistic foundation for evaluating PDF/A conversion workflows. They are intended to support both research analysis and practical digital preservation applications.

Future users are encouraged to use these samples as a baseline for testing additional tools, workflows, or preservation strategies.