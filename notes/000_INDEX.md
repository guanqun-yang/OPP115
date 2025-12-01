# OPP-115 Dataset Notes - Index

This directory contains comprehensive notes on the OPP-115 privacy policy corpus.

## Quick Navigation

### For First-Time Users
1. Start with **001_DATASET_OVERVIEW.md** - Understand what OPP-115 is
2. Read **006_QUICK_START_GUIDE.md** - Get hands-on quickly
3. Reference **003_ANNOTATION_SCHEMA.md** - Understand the categories

### For Researchers
1. **001_DATASET_OVERVIEW.md** - Citation and licensing
2. **005_RESEARCH_APPLICATIONS.md** - Use cases and methodologies
3. **003_ANNOTATION_SCHEMA.md** - Complete schema reference

### For Developers
1. **006_QUICK_START_GUIDE.md** - Code examples
2. **004_DATA_FORMAT.md** - File formats and structures
3. **002_DIRECTORY_STRUCTURE.md** - Where to find files
4. **008_DATASETS_GUIDE.md** - Working with `datasets/`

## File Descriptions

### 001_DATASET_OVERVIEW.md
**What it is**: High-level introduction to the OPP-115 dataset
**Contains**:
- What OPP-115 is and why it was created
- Key statistics (115 policies, 23K+ annotations)
- Required citation information
- License and usage terms
- Coverage and scope

**Read this if**: You're new to the dataset or need citation info

---

### 002_DIRECTORY_STRUCTURE.md
**What it is**: Guide to the file organization
**Contains**:
- Explanation of each directory (`/annotations/`, `/consolidation/`, etc.)
- File naming conventions
- What each file type contains
- Directory sizes and counts

**Read this if**: You need to locate specific files or understand the organization

---

### 003_ANNOTATION_SCHEMA.md
**What it is**: Complete reference for privacy practice categories
**Contains**:
- All 10 privacy practice categories
- Required and optional attributes for each
- Value options for each attribute
- Description of personal information types
- Examples and definitions

**Read this if**: You need to understand the annotation taxonomy or interpret annotations

---

### 004_DATA_FORMAT.md
**What it is**: Technical specification of data formats
**Contains**:
- CSV column structure for annotations
- JSON format for attribute-value pairs
- Sanitized policy HTML format
- Segment indexing explanation
- Character position indexing
- Known data issues and errors

**Read this if**: You're parsing the data programmatically or debugging issues

---

### 005_RESEARCH_APPLICATIONS.md
**What it is**: Research use cases and methodologies
**Contains**:
- Primary research use cases
- Dataset strengths and limitations
- Common research questions
- Analysis approaches (statistical, ML, text mining)
- Integration with other datasets
- Best practices
- Future research directions

**Read this if**: You're designing a research study or writing a paper

---

### 006_QUICK_START_GUIDE.md
**What it is**: Hands-on tutorial with code examples
**Contains**:
- 5-minute quick start
- Python code examples
- Common tasks and solutions
- Helper functions
- Common pitfalls
- Next steps

**Read this if**: You want to start analyzing data immediately

---

### 007_WEBSITE_METADATA.md
**What it is**: Information about the 115 websites in the dataset
**Contains**:
- List of websites by category
- Alexa rankings
- Sectoral coverage
- Temporal information (collection dates)
- Selection methodology
- Using metadata for analysis

**Read this if**: You need to understand which websites are included or analyze by sector

---

## Quick Reference

### Essential Statistics
- **Policies**: 115
- **Websites**: 115 (from US Alexa Top 100+)
- **Total Annotations**: 23,194
- **Annotators per Policy**: 3
- **Categories**: 10 privacy practice types
- **Time Period**: 2014-2016

### Key Directories
- `/annotations/` - Raw annotations (115 CSV files)
- `/consolidation/` - Merged annotations (3 threshold levels)
- `/sanitized_policies/` - Segmented policy text (115 HTML files)
- `/documentation/` - Metadata and schema
- `/original_policies/` - Source web pages

### Most Important Files
- `documentation/manual.txt` - Official technical manual
- `documentation/categories-july30.xml` - Complete schema XML
- `documentation/websites_opp115.csv` - Website metadata
- `annotations/{id}_{domain}.csv` - Individual policy annotations

### 10 Privacy Categories
1. First Party Collection/Use
2. Third Party Sharing/Collection
3. User Choice/Control
4. User Access, Edit and Deletion
5. Data Retention
6. Data Security
7. Policy Change
8. Do Not Track
9. International and Specific Audiences
10. Other

## Common Workflows

### Workflow 1: Analyze a Single Policy
1. Read **006_QUICK_START_GUIDE.md** (section 2-5)
2. Load annotation CSV
3. Parse JSON attributes
4. Link to policy text segments

### Workflow 2: Cross-Policy Analysis
1. Read **006_QUICK_START_GUIDE.md** (Task 4)
2. Loop through all annotation files
3. Use consolidated data to reduce redundancy
4. Aggregate statistics

### Workflow 3: Build ML Model
1. Read **005_RESEARCH_APPLICATIONS.md** (Machine Learning section)
2. Extract training data from annotations
3. Use attribute values as labels
4. Use selected text as features

### Workflow 4: Regulatory Compliance Check
1. Read **003_ANNOTATION_SCHEMA.md** (understand categories)
2. Read **005_RESEARCH_APPLICATIONS.md** (compliance checking)
3. Map regulations to categories
4. Check for presence/absence of practices

## Getting Help

### Dataset Issues
- **Known errors**: Check `documentation/errant_span_indexes/`
- **Missing data**: See **004_DATA_FORMAT.md** (Known Data Issues)
- **Questions**: Contact Prof. Norman Sadeh (sadeh@cs.cmu.edu)

### Understanding Annotations
- **Schema questions**: See **003_ANNOTATION_SCHEMA.md**
- **Format questions**: See **004_DATA_FORMAT.md**
- **Examples**: See **006_QUICK_START_GUIDE.md**

### Research Guidance
- **Methodology**: See **005_RESEARCH_APPLICATIONS.md**
- **Citation**: See **001_DATASET_OVERVIEW.md**
- **Paper**: Wilson et al., ACL 2016

## Related Resources

### Official
- Usable Privacy Policy Project: www.usableprivacy.org
- Contact: sadeh@cs.cmu.edu

### Academic
- ACL 2016 Paper (required reading)
- Technical manual: `documentation/manual.txt`

### Code Examples
- Python examples in **006_QUICK_START_GUIDE.md**
- Schema in XML: `documentation/categories-july30.xml`

## Last Updated
These notes created: 2025-11-17

## Note Organization

Files numbered 001-007 for easy sequential reading, but you can read in any order based on your needs. Use this index to jump to relevant sections.
