# OPP-115 Quick Start Guide

## Getting Started in 5 Minutes

### 1. Understanding the Basic Structure

**One Privacy Policy = Multiple Files**:
- `annotations/{id}_{domain}.csv` - Structured annotations
- `sanitized_policies/{id}_{domain}.html` - Segmented policy text
- `original_policies/{id}_{domain}/` - Original web page

**Example for Amazon (Policy ID 105)**:
- `annotations/105_amazon.com.csv`
- `sanitized_policies/105_amazon.com.html`
- `original_policies/105_www.amazon.com/`

### 2. Reading Annotation Files

#### Load annotations in Python:
```python
import pandas as pd
import json

# Load annotations for Amazon
df = pd.read_csv('annotations/105_amazon.com.csv',
                 names=['annotation_id', 'batch_id', 'annotator_id',
                        'policy_id', 'segment_id', 'category',
                        'attributes', 'url', 'date'])

# Parse JSON attributes
df['attributes_parsed'] = df['attributes'].apply(json.loads)

# See first annotation
print(df.iloc[0])
```

#### Basic exploration:
```python
# Count annotations by category
print(df['category'].value_counts())

# See unique categories
print(df['category'].unique())

# Filter to specific category
collection_practices = df[df['category'] == 'First Party Collection/Use']
```

### 3. Extracting Information from Attributes

```python
# Extract a specific attribute value
def get_attribute_value(attr_dict, attr_name):
    """Extract value for a specific attribute"""
    if attr_name in attr_dict:
        return attr_dict[attr_name]['value']
    return None

# Example: Get all collected data types
data_types = []
for idx, row in collection_practices.iterrows():
    attrs = row['attributes_parsed']
    data_type = get_attribute_value(attrs, 'Personal Information Type')
    if data_type:
        data_types.append(data_type)

print("Data types collected:", set(data_types))
```

### 4. Working with Policy Text

```python
# Read sanitized policy
with open('sanitized_policies/105_amazon.com.html', 'r') as f:
    policy_text = f.read()

# Split into segments
segments = policy_text.split('|||')

# Get text for a specific segment
segment_id = 4
print(f"Segment {segment_id}:")
print(segments[segment_id])
```

### 5. Linking Annotations to Text

```python
# Get annotation and its text
annotation = df.iloc[7]  # Example annotation
attrs = annotation['attributes_parsed']

segment_id = annotation['segment_id']
segment_text = segments[segment_id]

print(f"Category: {annotation['category']}")
print(f"Segment {segment_id}: {segment_text[:200]}...")
print("\nSelected text spans:")

# Show all selected text
for attr_name, attr_data in attrs.items():
    if 'selectedText' in attr_data and attr_data['selectedText']:
        print(f"  {attr_name}: '{attr_data['selectedText']}'")
        print(f"    → Value: {attr_data['value']}")
```

## Common Tasks

### Task 1: Find All Third-Party Sharing Practices

```python
third_party = df[df['category'] == 'Third Party Sharing/Collection']

for idx, row in third_party.iterrows():
    attrs = row['attributes_parsed']
    entity = get_attribute_value(attrs, 'Third Party Entity')
    purpose = get_attribute_value(attrs, 'Purpose')
    print(f"Shares with {entity} for {purpose}")
```

### Task 2: Check What User Choices Are Offered

```python
user_choice = df[df['category'] == 'User Choice/Control']

for idx, row in user_choice.iterrows():
    attrs = row['attributes_parsed']
    choice_type = get_attribute_value(attrs, 'Choice Type')
    scope = get_attribute_value(attrs, 'Choice Scope')
    print(f"Choice: {choice_type} - Scope: {scope}")
```

### Task 3: Analyze Data Retention Policies

```python
retention = df[df['category'] == 'Data Retention']

for idx, row in retention.iterrows():
    attrs = row['attributes_parsed']
    period = get_attribute_value(attrs, 'Retention Period')
    purpose = get_attribute_value(attrs, 'Retention Purpose')
    data_type = get_attribute_value(attrs, 'Personal Information Type')
    print(f"{data_type} retained {period} for {purpose}")
```

### Task 4: Cross-Policy Analysis

```python
import glob

def analyze_all_policies(category_name):
    """Count practices of a specific category across all policies"""
    results = {}

    for csv_file in glob.glob('annotations/*.csv'):
        policy_name = csv_file.split('/')[-1].replace('.csv', '')
        df = pd.read_csv(csv_file, names=['annotation_id', 'batch_id',
                         'annotator_id', 'policy_id', 'segment_id',
                         'category', 'attributes', 'url', 'date'])

        count = len(df[df['category'] == category_name])
        results[policy_name] = count

    return results

# Example: Which sites have most third-party sharing?
sharing_counts = analyze_all_policies('Third Party Sharing/Collection')
sorted_sites = sorted(sharing_counts.items(), key=lambda x: x[1], reverse=True)
print("Top 10 sites by third-party sharing practices:")
for site, count in sorted_sites[:10]:
    print(f"  {site}: {count} practices")
```

### Task 5: Use Consolidated Data

```python
# Use consolidated annotations to reduce redundancy
df_consolidated = pd.read_csv(
    'consolidation/threshold-0.75-overlap-similarity/105_amazon.com.csv',
    names=['annotation_id', 'batch_id', 'annotator_id', 'policy_id',
           'segment_id', 'category', 'attributes', 'url', 'date']
)

# Annotations starting with 'C' are consolidated from multiple annotators
consolidated = df_consolidated[df_consolidated['annotation_id'].str.startswith('C')]
singlets = df_consolidated[~df_consolidated['annotation_id'].str.startswith('C')]

print(f"Consolidated annotations: {len(consolidated)}")
print(f"Singlet annotations: {len(singlets)}")
```

## Useful Helper Functions

```python
import json

def load_policy_annotations(policy_id_or_name):
    """Load annotations for a specific policy"""
    if isinstance(policy_id_or_name, int):
        # Find by ID
        files = glob.glob(f'annotations/{policy_id_or_name}_*.csv')
    else:
        # Find by name
        files = glob.glob(f'annotations/*{policy_id_or_name}*.csv')

    if not files:
        raise ValueError(f"No policy found for: {policy_id_or_name}")

    return pd.read_csv(files[0], names=['annotation_id', 'batch_id',
                       'annotator_id', 'policy_id', 'segment_id',
                       'category', 'attributes', 'url', 'date'])

def get_category_distribution(df):
    """Get distribution of categories in a policy"""
    return df['category'].value_counts().to_dict()

def extract_all_values(df, attribute_name):
    """Extract all values for a specific attribute across all annotations"""
    values = []
    for idx, row in df.iterrows():
        try:
            attrs = json.loads(row['attributes'])
            if attribute_name in attrs:
                values.append(attrs[attribute_name]['value'])
        except:
            continue
    return values

def find_practices_about(df, data_type):
    """Find all practices related to a specific data type"""
    results = []
    for idx, row in df.iterrows():
        try:
            attrs = json.loads(row['attributes'])
            if 'Personal Information Type' in attrs:
                if attrs['Personal Information Type']['value'] == data_type:
                    results.append(row)
        except:
            continue
    return pd.DataFrame(results)
```

## Common Pitfalls to Avoid

1. **Don't forget to parse JSON**: Column G is a JSON string, not a dict
2. **Segment IDs start at 0**: First segment is 0, not 1
3. **Character indexes are segment-relative**: Not global document positions
4. **Check for "not-selected"**: Optional attributes may be "not-selected"
5. **Multiple annotators**: Raw annotations have 3× redundancy
6. **Use consolidation**: For most analyses, use consolidated data
7. **Read the manual**: documentation/manual.txt has important details

## Next Steps

1. Read `/documentation/manual.txt` for complete technical details
2. Examine `/documentation/categories-july30.xml` for full schema
3. Check `/documentation/errant_span_indexes/` for known errors
4. Explore different consolidation thresholds
5. Compare raw vs consolidated annotations
6. Try analyzing trends across multiple policies
