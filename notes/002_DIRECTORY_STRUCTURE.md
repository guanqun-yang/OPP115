# OPP-115 Directory Structure

## Main Directories

### `/annotations/` - Raw Annotations
- **115 CSV files** (one per website)
- Each file named: `{policy_id}_{domain}.csv`
- Example: `105_amazon.com.csv`
- Contains all 3 annotators' work (no consolidation)
- **Total**: ~23,194 annotation rows across all files

### `/consolidation/` - Consolidated Annotations
Three subdirectories with different consolidation thresholds:
- `threshold-0.5-overlap-similarity/`
- `threshold-0.75-overlap-similarity/`
- `threshold-1.0-overlap-similarity/`

Each contains consolidated annotations where redundant annotations from multiple annotators are merged.

**Consolidation IDs**:
- Annotations starting with 'C': Consolidated from 2-3 annotators
- Other annotations: "Singlets" - identified by only one annotator

### `/sanitized_policies/` - Cleaned Policy Text
- 115 HTML files (one per policy)
- Simplified markup with minimal formatting
- Segmented into chunks using `|||` separator
- What annotators actually viewed during annotation
- Example: `105_amazon.com.html`

### `/original_policies/` - Raw Source Files
- 115+ original policy web pages (mostly HTML, one PDF)
- As downloaded from the internet
- May include supporting directories for rendering

### `/pretty_print/` - Human-Readable Annotations
- CSV files with annotations as English sentences
- Makes annotations easier to understand
- Columns: annotation_id, segment_id, annotator_id, pretty_print_string

### `/pretty_print_uniquified/` - Grouped Annotations
- Groups identical privacy practices together
- Shows count of how many times each practice appears
- Reduces redundancy for analysis

### `/documentation/` - Metadata and Documentation
Key files:
- `manual.txt` - Technical documentation
- `categories-july30.xml` - Complete annotation schema
- `websites_opp115.csv` - Website metadata
- `policies_opp115.csv` - Policy metadata
- `errant_span_indexes/` - Known annotation errors

## File Naming Convention

All data files follow the pattern:
```
{policy_id}_{domain_name}.{extension}
```

Where:
- `policy_id`: Numeric identifier (e.g., 105, 21, 26)
- `domain_name`: Website domain (e.g., amazon.com, imdb.com)
- `extension`: .csv, .html, or directory

## Directory Sizes

- **annotations/**: 115 CSV files
- **sanitized_policies/**: 115 HTML files
- **original_policies/**: 115+ files/directories
- **consolidation/**: 3 directories × 115 files each
