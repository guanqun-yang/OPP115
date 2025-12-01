# OPP-115 Datasets Guide

## Location

- `datasets/annotations/` — Raw CSV annotations (one file per policy)
- `datasets/documentation/` — Manual, schema XML, metadata CSVs
- `datasets/original_policies/` — Saved source web pages for policies
- `datasets/OPP-115_v1_0.zip` — Original archive (additional dirs may be zipped)

## What’s Included Here

- Raw annotation CSVs with three annotators per policy
- Policy metadata and schema references in `documentation/`
- Original HTML pages used to source policies

## Common Tasks

- Load an annotation CSV and parse the JSON attributes (Column G)
- Count practices by category within a policy
- Aggregate category counts across all policies
- Map `policy_id` and domains using `documentation/websites_opp115.csv`

## File Structure of Annotation Rows

1. `annotation_id`
2. `batch_id`
3. `annotator_id`
4. `policy_id`
5. `segment_id` (0-indexed)
6. `category` (one of 10 privacy practice types)
7. `attributes` (JSON string)
8. `url`
9. `date`

## Attributes JSON

- Top-level keys are attribute names (e.g., `Personal Information Type`)
- Each key maps to a dict with `value`, optional `selectedText`, and span indexes
- Optional attributes may have `value` set to `not-selected`

## Known Issues

- Some rows have missing `selectedText` or invalid span indexes
- JSON parsing may fail for a small number of rows; handle gracefully

## Tips

- Use raw annotations for full detail; use consolidated data if you unzip the full archive
- Segment IDs reference the segmented policy text; if `sanitized_policies/` isn’t present locally, focus on category/attribute analyses
- Always parse Column G as JSON before extracting attribute values

