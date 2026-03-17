# 📘 Decision Log: PDF/A Conversion Workflow Research

## Purpose

This document records the rationale behind the key decisions made during the research, testing, and development of PDF/A conversion workflows. The goal is to provide transparency into the decision-making process so that future researchers, practitioners, and digital preservation staff can understand the reasoning behind each methodological choice and adapt it to their own contexts.

This log supports reproducibility, institutional knowledge transfer, and long-term sustainability of the workflows documented in this repository.


---


## Table of Contents

1. [Choice of PDF/A as Target Format](#1-choice-of-pdfa-as-target-format)  
2. [Selection of PDF/A-2u and PDF/A-2b Variants](#2-selection-of-pdfa-2u-and-pdfa-2b-variants)  
3. [Focus on Access-Oriented Evaluation](#3-focus-on-access-oriented-evaluation)  
4. [Selection of Adobe Acrobat as Primary Tool](#4-selection-of-adobe-acrobat-as-primary-tool)  
5. [Use of Guided Actions for Batch Processing](#5-use-of-guided-actions-for-batch-processing)  
6. [Inclusion of Cloud-Based Auto-Tagging](#6-inclusion-of-cloud-based-auto-tagging)  
7. [Emphasis on Metadata Preservation](#7-emphasis-on-metadata-preservation)  
8. [Development of Metadata Comparison Methods](#8-development-of-metadata-comparison-methods)  
9. [Selection of Sample Files](#9-selection-of-sample-files)  
10. [Inclusion of Accessibility Evaluation](#10-inclusion-of-accessibility-evaluation)  
11. [Documentation of Setup and Environment](#11-documentation-of-setup-and-environment)  
12. [Creation of Detailed Workflow Documentation](#12-creation-of-detailed-workflow-documentation)  
13. [Separation of Repository Components](#13-separation-of-repository-components)  
14. [Emphasis on Reproducibility and Transparency](#14-emphasis-on-reproducibility-and-transparency)


---


## 1. Choice of PDF/A as Target Format

### Decision

Use PDF/A as the primary output format for converted documents.


### Rationale

PDF/A is an ISO-standardized format designed for long-term digital preservation. It ensures that documents remain accessible and render consistently over time, regardless of changes in software or hardware environments.

In digital preservation contexts, PDF/A is widely accepted as a preferred format for textual documents due to its:
- Self-contained nature (fonts, metadata, and resources embedded)
- Platform independence
- Long-term readability


---


## 2. Selection of PDF/A-2u and PDF/A-2b Variants

### Decision

Evaluate both PDF/A-2u and PDF/A-2b conversion outputs.


### Rationale

- PDF/A-2u supports Unicode text mapping, which improves:
    - Searchability
    - Copy/paste fidelity
    - Accessibility
    - Multilingual text support
- PDF/A-2b ensures visual preservation but does not guarantee text extractability.

Evaluating both variants allows comparison between:
- Strict preservation fidelity (2b)
- Preservation + access usability (2u)

This comparison supports informed decisions for institutions balancing preservation and access needs.


---


## 3. Focus on Access-Oriented Evaluation

### Decision

Evaluate PDF/A outputs not only as preservation formats but also as access formats.


### Rationale

While PDF/A is primarily intended for preservation, in practice, many institutions also use PDF/A files for access and discovery. Therefore, the evaluation considers:
- Text searchability
- Copy/paste accuracy
- Multilingual text handling
- Accessibility tagging
- Metadata usability

This reflects real-world usage in libraries and archives, where preservation and access are closely linked.



---


## 4. Selection of Adobe Acrobat as Primary Tool

### Decision

Use Adobe Acrobat Pro as the primary tool for PDF/A conversion.


### Rationale

Adobe Acrobat was selected because:
- It is widely used in institutional environments
- It provides robust support for PDF/A standards
- It offers Guided Actions for batch processing
- It supports accessibility evaluation tools
- It enables metadata inspection and editing

Using a tool already available to many institutions increases the likelihood that the workflows will be adopted and reused.


---


## 5. Use of Guided Actions for Batch Processing

### Decision

Use Adobe Acrobat’s Guided Actions feature to automate batch conversion to PDF/A-2u.


### Rationale

Batch processing is essential for real-world digital preservation workflows, where large volumes of documents must be converted efficiently.

Guided Actions allow:
- Consistent application of settings
- Reduced manual intervention
- Scalable processing
- Reproducible workflows

This approach aligns with institutional needs for efficiency and standardization.


---


## 6. Inclusion of Cloud-Based Auto-Tagging


### Decision

Evaluate the impact of Adobe’s cloud-based auto-tagging for accessibility on conversion outputs.


### Rationale

Accessibility is a critical component of modern digital preservation. Cloud-based auto-tagging was evaluated to determine:
- Whether it improves document structure
- Whether it enhances accessibility compliance
- Whether it affects metadata or text extraction

This evaluation supports institutions seeking to align preservation workflows with accessibility standards.


---


## 7. Emphasis on Metadata Preservation

## Decision

Include detailed analysis of metadata preservation across conversion workflows.


## Rationale

Metadata is essential for:
- Discovery
- Contextual understanding
- Long-term management and storage
- Institutional repository integration

Evaluating metadata retention ensures that converted documents remain useful within digital collections and not just visually preserved.


---


## 8. Development of Metadata Comparison Methods

### Decision

Create structured methods and scripts to extract and compare metadata across original and converted files.


### Rationale

Manual comparison of metadata is inefficient and error-prone. Automated comparison allows:
- Systematic evaluation
- Repeatable analysis
- Objective identification of differences
- Scalable testing

This supports evidence-based evaluation of conversion workflows.


---


## 9. Selection of Sample Files

### Decision

Use a combination of real archival documents and a synthetic stress-test document.


### Rationale

**Real Documents**
- Represent authentic and real-world preservation challenges
- Include legacy formats
- Include multilingual content
- Reflect real-world variability

**Stress-Test Document:** A custom-created document was designed to include:
- Multiple languages
- Special characters and symbols
- Complex formatting
- Images, tables, and diagrams
- Mathematical equations (LaTex)
- Microsoft WordArt & SmartArt
- Accessibility edge cases (e.g., headings)

This combination ensures realistic, robut, and comprehensive testing coverage.


---


## 10. Inclusion of Accessibility Evaluation

### Decision

Include accessibility testing using Adobe Acrobat’s Accessibility Checker.


### Rationale

Accessibility is a core component of digital access and equity. Including accessibility evaluation ensures that converted documents are not only preserved but also usable by a broader audience.

This aligns with modern digital preservation principles, which emphasize both longevity and accessibility.


---


## 11. Documentation of Setup and Environment

### Decision

Document the configuration steps required to set up conversion workflows in Adobe Acrobat.


### Rationale

Without setup documentation, workflows cannot be reliably reproduced. Documenting environment setup ensures:
- Reproducibility
- Consistency across users
- Reduced onboarding time for future researchers
- Long-term usability of the workflows


---


## 12. Creation of Detailed Workflow Documentation

### Decision

Provide step-by-step workflow guides for all major processes.


### Rationale

Detailed documentation supports:
- Knowledge transfer
- Institutional reuse
- Training staff or students
- Transparency in research methods

This ensures the work can function as both a research artifact and a practical guide.


---


## 13. Separation of Repository Components

### Decision

Organize the repository into distinct sections (workflows, samples, metadata, reports, docs, screenshots).

### Rationale

Clear organization improves:
- Usability
- Navigability
- Reproducibility
- Maintainability

This structure supports both research and operational use.


---


## 14. Emphasis on Reproducibility and Transparency

### Decision

Design the project to be fully reproducible and transparent.

### Rationale

Digital preservation research must be verifiable and adaptable. By documenting methods, decisions, and results, this project ensures that others can:
- Replicate the workflows
- Validate findings
- Adapt methods to new contexts
- Build upon the research


---


## 🌟 Final Note

This Decision Log reflects the intentional choices made to ensure that the workflows developed in this project are:
- Practical
- Reusable
- Transparent
- Evidence-based
- Aligned with real-world digital preservation needs

Future researchers and practitioners are encouraged to use this log as a reference when adapting these workflows to their own institutional contexts.
