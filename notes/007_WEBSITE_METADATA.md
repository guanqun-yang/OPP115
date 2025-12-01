# OPP-115 Website Metadata

## Dataset Composition

### Total Coverage
- **115 websites** from US Alexa rankings
- **115 privacy policies** (one per website)
- Collected between 2014-2016
- Primarily from US Alexa Top 100

## Sample Websites (Partial List)

### Major E-Commerce
- **Amazon** (Policy ID: 105) - Alexa Rank: 6 Global, 4 US
- **Walmart** (Policy ID: 348)
- **Barnes & Noble** (Policy ID: 453)
- **GameStop** (Policy ID: 640)

### News & Media
- **New York Times** (Policy ID: 26) - Alexa Rank: 101 Global, 22 US
- **The Atlantic** (Policy ID: 20) - Alexa Rank: 975 Global, 289 US
- **Washington Post** (Policy ID: 200) - Alexa Rank: 202 Global, 45 US
- **ABC News** (Policy ID: 186) - Alexa Rank: 553 Global, 159 US
- **Fortune** (Policy ID: 133) - Alexa Rank: 1443 Global, 518 US
- **Adweek** (Policy ID: 164) - Alexa Rank: 2893 Global, 1415 US

### Social Media & Entertainment
- **Instagram** (Policy ID: 135) - Alexa Rank: 24 Global, 20 US
- **IMDb** (Policy ID: 21) - Alexa Rank: 49 Global, 27 US
- **Reddit** (Policy ID: 303)

### Technology & Internet
- **Google** (Policy ID: 591)
- **Yahoo** (Policy ID: 1361)
- **MSN** (Policy ID: 1582)
- **Verizon (Vox Media)** (Policy ID: 32) - Alexa Rank: 525 Global, 230 US
- **The Verge** (part of Vox Media)

### Sports & Recreation
- **MLB (Major League Baseball)** (Policy ID: 175) - Alexa Rank: 1026 Global, 235 US
- **ESPN (Allrecipes)** (Policy ID: 70) - Alexa Rank: 399 Global, 117 US
- **Fox Sports** (Policy ID: 1708)

### Broadcasting
- **NBC Universal** (Policy ID: 33) - Alexa Rank: 1548 Global, 426 US
- **PBS** (Policy ID: 93) - Alexa Rank: 980 Global, 225 US
- **CBS Interactive** (Policy ID: 641)

### Fashion & Lifestyle
- **Vogue (Style.com)** (Policy ID: 144)
- **Esquire** (Policy ID: 58) - Alexa Rank: 1696 Global, 554 US

### Food & Beverage
- **Allrecipes** (Policy ID: 70) - Alexa Rank: 399 Global, 117 US
- **Liquor.com** (Policy ID: 59) - Alexa Rank: 19805 Global, 4787 US
- **DrinksMixer** (Policy ID: 82) - Alexa Rank: 36039 Global, 11117 US

### Regional & Local
- **New Orleans Online** (Policy ID: 98) - Alexa Rank: 68030 Global, 12634 US

### Gaming
- **Rockstar Games** (Policy ID: 1468)
- **Steam (Valve)** (Policy ID: 1470)
- **PlayStation** (Policy ID: 635)

### Finance & Insurance
- **Bank of America** (Policy ID: 1300)
- **Chase Paymentech** (Policy ID: 1306)
- **Allstate** (Policy ID: 1106)
- **Zacks** (Policy ID: 1261)
- **The Motley Fool** (Policy ID: 1259)

### Government & Education
- **USA.gov** (Policy ID: 523)
- **Archives.gov** (Policy ID: 531)
- **Library of Congress** (Policy ID: 559)
- **Smithsonian** (Policy ID: 760)
- **Austin Community College** (Policy ID: 1224)
- **Dallas County Community College** (Policy ID: 1206)

### Health & Medical
- **Everyday Health** (Policy ID: 891)
- **UpToDate** (Policy ID: 898)

### Travel & Entertainment
- **Ticketmaster** (Policy ID: 1498)
- **JibJab** (Policy ID: 1510)
- **Geocaching** (Policy ID: 1539)

## Metadata Files

### websites_opp115.csv
Contains 115 websites with columns:
- **Site UID**: Unique identifier
- **Site URL**: Website domain
- **Site Human-Readable Name**: Common name
- **Policy UID**: Links to policy file
- **Site check date**: When policy was verified (YYYY-MM-DD)
- **In 115 Set?**: Confirmation of inclusion
- **Comments**: Additional notes (often includes Alexa ranks)
- **Sectoral Data**: DMOZ categories (variable number of columns)

### policies_opp115.csv
Contains 115 policies with columns:
- **Policy UID**: Unique identifier
- **Policy URL**: Direct URL to privacy policy
- **Policy collection date**: When retrieved (YYYY-MM-DD)
- **Policy last updated date**: Last update per policy (YYYY-MM-DD)

### websites_covered_opp115.csv
Superset of websites_opp115.csv
- Includes websites with policies covered by the dataset
- May include multiple sites using same policy

### websites_at100.csv & policies_at100.csv
Data on all websites in US Alexa Top 100
- Same format as opp115 files
- May include sites not in the 115 annotated set

## Sectoral Coverage

Based on DMOZ categorization, the dataset includes websites from:

### Arts & Entertainment
- Literature, Music, Movies, TV, Theater
- Photography, Animation, Comics
- Performing Arts, Magic

### Business
- E-commerce, Finance, Marketing
- Publishing, News Media
- Technology Companies

### Recreation & Sports
- Food & Drink, Cooking
- Outdoor Activities, Hunting, Fishing
- Professional Sports (MLB, Football, etc.)
- Gaming (Video Games, Board Games)

### Reference & Education
- Libraries, Museums
- Educational Institutions
- Government Resources
- Scientific Resources

### Regional
- City Guides
- Local News
- Regional Services

### Society & Culture
- Politics, History
- Health & Wellness
- Religion & Spirituality
- Issues & Activism

### Science & Technology
- Astronomy, Biology, Physics
- Social Sciences
- Earth Sciences
- Technology News

### Health
- Medical Information
- Fitness & Wellness
- Mental Health
- Alternative Medicine

## Temporal Information

### Collection Period
- Policies collected: 2014-2016
- Most policies from 2014-2015
- Some updated in 2016

### Policy Update Dates
- Policies show "Last Updated" dates
- Example: Amazon - "Last updated: March 3, 2014"
- Dates vary by website's update schedule

## Alexa Ranking Context

### Global Rankings (Examples)
- Top 10: Amazon (#6)
- Top 50: IMDb (#49), Instagram (#24)
- Top 100: NYTimes (#101)
- Top 500: Vox Media/The Verge (#525)
- Top 1000: PBS (#980), MLB (#1026)
- Top 2000: Esquire (#1696), NBC (#1548)
- Top 3000: Adweek (#2893)

### US Rankings (Examples)
- Top 10: Amazon (#4)
- Top 25: Instagram (#20), NYTimes (#22), IMDb (#27)
- Top 50: Washington Post (#45)
- Top 100: Allrecipes (#117)
- Top 250: PBS (#225), The Verge (#230), MLB (#235)
- Top 500: Fortune (#518), NBC (#426), Esquire (#554)
- Top 1500: Adweek (#1415)

## Selection Methodology

### Policy Selection Approach
See `documentation/policy-selection-approach.txt` for details on:
- How policies were selected
- Sector representation goals
- Inclusion/exclusion criteria
- Sampling strategy

### Coverage Goals
- Diverse industry sectors
- Mix of large and medium-sized sites
- US-focused but some international
- Both specialized and general-purpose sites

## Using Metadata for Analysis

### By Sector
```python
import pandas as pd

websites = pd.read_csv('documentation/websites_opp115.csv')

# Group by sector (requires parsing DMOZ columns)
# Columns H onwards contain sectoral data
```

### By Alexa Rank
```python
# Extract Alexa rank from comments
def extract_alexa_rank(comment):
    if 'Alexa Rank' in str(comment):
        # Parse: "Alexa Rank: 975 (Global), 289 (US)"
        parts = comment.split(',')
        global_rank = int(parts[0].split(':')[1].strip().split()[0])
        return global_rank
    return None

websites['alexa_global'] = websites['Comments'].apply(extract_alexa_rank)
```

### By Collection Date
```python
policies = pd.read_csv('documentation/policies_opp115.csv')
policies['collection_date'] = pd.to_datetime(policies['Policy collection date'])

# Analyze by year
policies['year'] = policies['collection_date'].dt.year
print(policies['year'].value_counts())
```

## Key Insights

### High-Traffic Focus
- Most websites are high-traffic (Alexa Top 1000)
- Represents policies seen by millions of users
- Bias toward popular, established websites

### US-Centric
- Primarily US Alexa rankings
- Most websites target US audiences
- Some international sites included

### Diverse but Selective
- Wide range of sectors represented
- Not comprehensive coverage of any sector
- Focus on well-established brands

### Snapshot in Time
- 2014-2016 policies
- Pre-GDPR enforcement (May 2018)
- Pre-CCPA (January 2020)
- Policies likely updated since collection
