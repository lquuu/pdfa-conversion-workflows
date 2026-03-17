# Research Notes: Access Format Evaluation for DOC/DOCX Files

## Overview
The goal of this project was to determine the most suitable **access format** for obsolete and legacy text-based file formats (specifically `.doc` and `.docx`), and to develop a **repeatable, scalable workflow** for converting and delivering these files for end-user access.

This research supports the University of Michigan Digital Preservation Lab (UM DPL) by:
- Defining evaluation criteria for access formats  
- Justifying the selection of a recommended format  
- Documenting workflows for reproducibility and future use  

This work builds on existing digital preservation frameworks while extending them to include **accessibility, sustainability, and workflow feasibility** within the DPL context.

---

## Research Questions

This project was guided by the following core questions:

- What format best preserves **visual fidelity** (layout, pagination, fonts)?
- What format best retains **metadata** from the original document?
- What format best supports **multilingual text** (Unicode)?
- What format is most **accessible** to users (e.g., screen readers)?
- What format is most **sustainable** in terms of:
  - storage size
  - energy usage
  - workflow feasibility
- What tools produce the most reliable conversions (e.g., Adobe vs LibreOffice)?

---

## Evaluation Criteria

To answer these questions, I developed the following evaluation framework:

- **Visual Fidelity**  
  Preservation of layout, pagination, fonts, spacing, and document structure  

- **Metadata Retention**  
  Preservation of author, creation date, language, and document properties  

- **Language Support (Unicode)**  
  Ability to preserve multilingual content (e.g., Portuguese, Chinese)  

- **Accessibility**  
  Screen-reader compatibility, tagging, reading order, and searchability  

- **Sustainability**  
  File size, storage implications, and energy cost of conversion workflows  

- **Ease of Use**  
  Accessibility of tools for both DPL staff and end users  

---

## Methodology

### Format Exploration
I evaluated a wide range of candidate access formats, including:

- PDF/A (A-1b, A-2b, A-2u, A-3)
- EPUB3
- HTML
- ODT
- RTF
- TXT
- XML-based formats (TEI, etc.)

This exploration was grounded in existing institutional guidance (e.g., Library of Congress recommendations) and expanded through independent testing and comparison.

---

### Tools Used

Primary tools:
- **Adobe Acrobat Pro**
- **ExifTool** (metadata extraction)
- **Python + PowerShell** (automation and comparison)

Additional tools explored:
- LibreOffice  
- Calibre  
- Google Docs  
- Gotenberg  

---

### Experimental Design

#### 1. Conversion Testing
- Converted DOC/DOCX files into multiple access formats  
- Compared outputs across tools and formats  

#### 2. Metadata Analysis
- Extracted metadata from original and converted files using ExifTool  
- Compared outputs using a custom Python script  

#### 3. Language Stress Testing
- Tested documents with:
  - Portuguese (accented characters)
  - Chinese (non-Latin scripts)

#### 4. Visual Inspection
- Compared:
  - pagination
  - spacing
  - fonts
  - layout consistency  

#### 5. Batch Processing
- Tested Adobe batch workflows using:
  - custom actions
  - guided actions
  - folder-based processing  

#### 6. Accessibility Testing
- Ran Adobe Accessibility Checks on converted files  
- Compared tagging behavior (Cloud AI vs non-Cloud)

---

## Key Findings

### 1. PDF/A-2u as the Preferred Access Format

PDF/A-2u emerged as the strongest candidate because it balances:

- **Visual fidelity** (layout preservation)
- **Unicode support** (multilingual compatibility)
- **Searchability and copy/paste functionality**
- **Wide accessibility and usability across platforms**

Compared to alternatives:
- EPUB → highly accessible but loses layout (reflowable)
- HTML → accessible but loses structure and pagination
- RTF/ODT → inconsistent formatting and layout drift
- DOCX → strong metadata, but requires proprietary software

---

### 2. Accessibility is Improved — But Not Guaranteed

A key insight:

> **PDF/A-2u does NOT guarantee full accessibility**

- Unicode mapping enables searchability and screen-reader compatibility  
- However, **semantic tagging is not required**  
- Manual intervention is still needed for:
  - tables
  - headings
  - reading order
  - image alt text  

This aligns with broader accessibility standards such as PDF/UA, which go further but require significantly more effort.

---

### 3. Accessibility Should Be Integrated Early

Accessibility should be treated as a **core part of the workflow**, not an afterthought.

If not:
- Files may need to be reprocessed later  
- Additional labor is introduced  
- Users may be excluded from access  

Designing for accessibility upfront:
- improves long-term usability  
- reduces rework  
- aligns with inclusive access goals  

---

### 4. File Size Implications (Sustainability)

A major finding:

- PDF/A-2u files are typically **2×–10× larger** than original DOC/DOCX files  
- Most commonly: **~7–8× increase**

Observed pattern:
- Smaller files → larger multipliers  
- Larger files → smaller multipliers  

Implication:
- Storage and cloud costs must be considered  
- Sustainability should be part of format selection decisions  

---

### 5. Metadata Tradeoffs

- Original DOC/DOCX files retain the richest metadata  
- PDF/A-2u:
  - preserves some metadata  
  - loses others (e.g., Word-specific statistics)

This reinforces:
> **Access formats should not replace preservation formats**

---

### 6. Cloud AI Tagging (Adobe)

- No significant difference observed in output quality  
- Does not eliminate need for manual accessibility checks  
- Still requires validation and human review  

---

## Observations & Reflections

Some notable learning experiences from this project:

- Discovery of multiple PDF/A standards and their tradeoffs  
- Custom Adobe batch workflows are highly powerful and underutilized  
- First experience running Python scripts via PowerShell for automation  
- Introduction to Dublin Core metadata standards  
- Creation of a “stress test” document to push workflow limits  

---

## Open Questions

- Does PDF/A-2u sufficiently meet accessibility needs at scale?
- Should accessibility compliance (e.g., PDF/UA) be required in workflows?
- What is the **minimum acceptable standard** for access formats?
- How should institutions balance:
  - accessibility  
  - fidelity  
  - sustainability  
  - labor cost  

---

## Next Steps

- Further research into **PDF/UA compliance workflows**
- Investigate **AI-assisted tagging reliability**
- Expand **sustainability analysis** (energy + storage)
- Finalize and document **production-ready workflows**
- Share findings with Special Collections for implementation decisions

---

## Repository Context

This research is supported by:
- Sample datasets (Portuguese, Chinese, stress test cases)
- Metadata comparison outputs
- Accessibility reports
- Adobe batch processing reports
- Step-by-step workflow documentation

See repository structure for full details.
