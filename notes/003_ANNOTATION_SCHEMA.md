# OPP-115 Annotation Schema

## Core Concepts

### Privacy Practice (Data Practice)
A structured annotation derived from privacy policy text that describes:
- **Category**: One of 10 privacy practice categories
- **Attributes**: Set of attribute-value pairs (some optional)
- **Text Spans**: Selected text from policy associated with each value

### Policy Segmentation
- Policies divided into **segments** (roughly paragraph-length)
- Each segment annotated independently
- Segments numbered sequentially starting from 0
- Segments separated by `|||` in sanitized policies

### Multiple Annotators
- 3 annotators per policy
- Creates redundancy for quality/agreement analysis
- Can be consolidated using similarity thresholds

## The 10 Privacy Practice Categories

### 1. First Party Collection/Use
**Description**: Data collection or use by the company/organization owning the website/app

**Key Attributes**:
- Action First-Party (required): How data is collected
  - Collect on website, Collect in mobile app, Track user on other websites, etc.
- Personal Information Type (required): What data is collected
  - Financial, Health, Contact, Location, Demographic, etc.
- Purpose (required): Why data is collected/used
  - Basic service, Advertising, Marketing, Analytics, etc.
- Collection Mode (optional): Explicit vs Implicit
- Identifiability (optional): Identifiable, Aggregated/anonymized
- User Type (optional): User with/without account
- Choice Type (optional): User control options
- Choice Scope (optional): What choices apply to
- Does/Does Not (optional): Affirmative or negative statement

### 2. Third Party Sharing/Collection
**Description**: Data sharing with or collection by third parties

**Key Attributes**:
- Third Party Entity (required): Who receives data
  - Named/unnamed third party, Affiliates, Other users, Public
- Action Third Party (required): How third party gets data
  - Receive/shared with, Collect on site, Track on site, See
- Personal Information Type (required)
- Purpose (required)
- Identifiability (optional)
- User Type (optional)
- Choice Type (optional)
- Choice Scope (optional)
- Does/Does Not (optional)

### 3. User Choice/Control
**Description**: General choices and control options available to users

**Key Attributes**:
- Choice Type (required): Type of control
  - Don't use service, Opt-in, Opt-out link, Privacy controls, etc.
- Choice Scope (required): What it applies to
  - First party collection/use, Third party sharing/collection/use
- Personal Information Type (required)
- Purpose (required)
- User Type (optional)

### 4. User Access, Edit and Deletion
**Description**: User ability to access, edit, or delete their data

**Key Attributes**:
- Access Type (required): What users can do
  - None, View, Export, Edit, Deactivate account, Delete account (partial/full)
- Access Scope (required): What data it applies to
  - User account data, Transactional data, Profile data, Other
- User Type (optional)

### 5. Data Retention
**Description**: How long user information is retained

**Key Attributes**:
- Retention Period (required): Duration
  - Indefinitely, Limited, Stated period, Unspecified
- Retention Purpose (required): Why data is kept
  - Perform service, Legal requirement, Analytics, Security, etc.
- Personal Information Type (required)

### 6. Data Security
**Description**: How user information is secured and protected

**Key Attributes**:
- Security Measure (required): Type of protection
  - Secure data transfer, Secure authentication, Secure storage
  - Data access limitation, Privacy training, Privacy review/audit
  - Privacy/Security program, Generic statements

### 7. Policy Change
**Description**: How users are informed of policy changes

**Key Attributes**:
- Change Type (required): What changes trigger notification
  - Non-privacy relevant, Privacy relevant, Merger/acquisition
- Notification Type (required): How users are notified
  - No notification, General notice, Personal notice (email)
- User Choice (required): Options when policy changes
  - None, Opt-out, Opt-in, User participation

### 8. Do Not Track
**Description**: How Do-Not-Track signals are handled

**Key Attributes**:
- Do Not Track policy (required):
  - Not mentioned, Honored, Not honored, Mentioned but unclear

### 9. International and Specific Audiences
**Description**: Special provisions for specific user groups

**Key Attributes**:
- Audience Type (required):
  - Californians, Europeans, Citizens from other countries, Children, Other

### 10. Other
**Description**: Aspects not covered by other categories

**Key Attributes**:
- Other Type (required):
  - Introductory/Generic
  - Practice not covered
  - Privacy contact information
  - Other

## Personal Information Types (Common Across Categories)

1. **Financial**: Credit cards, payment info, credit scores
2. **Health**: Medical info, prescriptions, fitness data
3. **Contact**: Name, email, phone, address
4. **Location**: GPS, ZIP code, city-level location
5. **Demographic**: Age, gender, occupation, education
6. **Personal identifier**: SSN, driver's license, unique IDs
7. **User online activities**: Browsing behavior, pages visited
8. **User profile**: Account data, uploaded content, preferences
9. **Social media data**: Connected account data
10. **IP address and device IDs**: Network identifiers
11. **Cookies and tracking elements**: Persistent identifiers
12. **Computer information**: OS, browser type
13. **Survey data**: Survey responses
14. **Generic personal information**: General "personal info"
15. **Other**: Specific type not listed
16. **Unspecified**: Not clearly stated
