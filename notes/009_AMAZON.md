# Amazon Dataset Guide

## Files

- `datasets/annotations/105_amazon.com.csv` — raw fine-grained annotations for Amazon
- `datasets/original_policies/105_www.amazon.com.html` — original policy page
- `datasets/documentation/manual.txt` — format, schema, and directory explanations

## What It Captures

- Annotators label privacy practices in policy text as structured records
- Each record has a category, attributes (JSON), and optional selected text spans
- `segment_id` links practices to segments in sanitized text (not present locally)

## Categories

- Distribution in Amazon annotations:
  - First Party Collection/Use: 122
  - Third Party Sharing/Collection: 53
  - User Choice/Control: 41
  - Other: 29
  - User Access, Edit and Deletion: 26
  - Data Security: 14
  - Policy Change: 11
  - Data Retention: 10
  - International and Specific Audiences: 6

## Attributes

- Examples of `Personal Information Type` values:
  - Computer information, Contact, Cookies and tracking elements, Demographic
  - Financial, Generic personal information, IP address and device IDs
  - Location, Other, Personal identifier, User Profile, User profile
  - User online activities, Unspecified

## Folder Relationships

- `annotations/` holds raw CSVs with all three annotators’ practices
- `original_policies/` provides the source HTML policy for context and text search
- `documentation/` describes columns, schema, categories, and known issues
- Sanitized segmented HTML (`sanitized_policies/`) exists in the full corpus but is not present here

## Useful Scripts

- `tests/load_annotations.py` — load and parse annotation CSV (`tests/load_annotations.py:16`)
- `tests/category_counts_all.py` — per-policy category aggregates
- `tests/amazon_overview.py` — Amazon-specific summary and attribute usage
- `tests/amazon_selected_spans.py` — sample selected text spans
- `tests/amazon_text_search.py` — finds selected texts in the original HTML

## Run

- `python3 tests/amazon_overview.py`
- `python3 tests/amazon_selected_spans.py`
- `python3 tests/amazon_text_search.py`

