# OPP-115 Data Format

## Annotation CSV Format

### Column Structure
Each annotation CSV file has 9 columns:

| Column | Name | Description |
|--------|------|-------------|
| A | annotation_id | Globally unique identifier for the data practice |
| B | batch_id | Name of annotation batch (indicates annotators) |
| C | annotator_id | Unique annotator identifier |
| D | policy_id | Numeric ID matching filename prefix |
| E | segment_id | Zero-indexed segment number in policy |
| F | category | One of 10 category names |
| G | attribute_value_pairs | JSON dictionary of attributes |
| H | policy_url | URL of the privacy policy |
| I | date | Date of annotation (MM/DD/YY format) |

### Example Row
```csv
9603,test_category_labeling_highlight_fordham_aaaa,121,3819,1,Policy Change,"{""Change Type"": {""endIndexInSegment"": 65, ""startIndexInSegment"": 0, ""selectedText"": ""Last updated: March 3, 2014..."", ""value"": ""Unspecified""}, ...}",3/3/14,http://www.amazon.com/...
```

## Attribute-Value Pairs (Column G)

### JSON Structure
```json
{
  "Attribute Name": {
    "startIndexInSegment": <int>,
    "endIndexInSegment": <int>,
    "selectedText": "<string>",
    "value": "<category value>"
  },
  ...
}
```

### Components
- **Attribute Name**: Name from schema (e.g., "Personal Information Type")
- **startIndexInSegment**: Character position where highlighted text starts
- **endIndexInSegment**: Character position where highlighted text ends
- **selectedText**: Actual text selected from policy segment
- **value**: The assigned value for this attribute

### Special Values
- `"not-selected"`: Optional attribute not filled in
- `startIndexInSegment: -1, endIndexInSegment: -1`: No text selected (value only)

### Example
```json
{
  "Personal Information Type": {
    "endIndexInSegment": 125,
    "startIndexInSegment": 56,
    "selectedText": "any information you enter on our Web site or give us in any other way",
    "value": "Other"
  },
  "Purpose": {
    "endIndexInSegment": 424,
    "startIndexInSegment": 389,
    "selectedText": "customizing future shopping for you",
    "value": "Personalization/Customization"
  }
}
```

## Sanitized Policy Format

### File Structure
- HTML file with minimal markup
- Segments separated by `|||`
- Numbered starting from 0

### Example
```html
<segment_0>Amazon.com Privacy Notice</segment_0>
|||
<segment_1>Last updated: March 3, 2014. To see what has changed, click here.</segment_1>
|||
<segment_2>This notice describes our privacy policy. By visiting Amazon.com, you are accepting the practices described in this Privacy Notice.</segment_2>
|||
...
```

### Segment Indexing
- Character indexes in annotations refer to position WITHIN a segment
- Not global document position
- Segment 0 is first segment, segment 1 is second, etc.

## Pretty Print Format

### CSV Structure
| Column | Description |
|--------|-------------|
| A | annotation_id |
| B | segment_id |
| C | annotator_id |
| D | pretty_print_string |

### Example
```
9603,1,121,"The policy notifies users about policy changes. Users are notified when the policy changes via a general notice in the privacy policy."
```

## Consolidation File Format

Same as annotation CSV format, but:
- Annotation IDs starting with 'C': Consolidated annotations
- Other IDs: Singlet annotations (unique to one annotator)
- Different files for different consolidation thresholds (0.5, 0.75, 1.0)

## Known Data Issues

### Errant Span Indexes
- Small number of practices have incorrect character indexes
- Listed in `documentation/errant_span_indexes/`
- Bug in annotation tool caused this

### Missing Spans
- Some practices missing required text spans
- Indicated by: `"selectedText"` key missing OR both indexes = -1 or 0

### Missing Markup in HTML Spans
- Some Column I entries missing markup tags for selected spans
- Annotation tool error

## CSV Dialect

- Uses **Excel CSV dialect**
- Quoted fields can contain commas
- JSON in Column G is properly escaped
