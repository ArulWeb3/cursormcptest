# Odoo Product Cleansing Module Documentation

## Overview
The Product Data Cleansing and Enrichment module for Odoo 18 Enterprise provides a comprehensive solution for managing external product data, matching it with internal products, and enriching product information.

## Table of Contents
1. [Module Features](#module-features)
2. [Data Models](#data-models)
3. [API Reference](#api-reference)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage Guide](#usage-guide)

## Module Features
- External product data management with versioning
- Product matching with confidence scoring
- Data enrichment workflow
- REST API integration
- User-friendly interface

## Data Models

### 1. Product External Data (product.external.data)
```python
Fields:
- custom_id (Char): Unique identifier (UUID)
- source (Char): Data source (e.g., "Google Shopping")
- data (Json): Raw external product data
- version (Integer): Version number
- timestamp (Datetime): Last update time
- previous_version_id (Char): Reference to previous version
```

### 2. Product Match Mapping (product.match.mapping)
```python
Fields:
- product_id (Many2one): Reference to Odoo product
- external_data_id (Many2one): Reference to external data
- status (Selection): [pending, matched, unmatched]
- matching_score (Integer): 0-100 confidence score
- match_validated_at (Datetime): Validation timestamp
- validated_by (Many2one): User who validated
```

### 3. Extended Product (product.product)
```python
Added Fields:
- moombs_brand (Char): Product brand
- moombs_category (Char): Product category
- moombs_color (Char): Product color
- moombs_size (Char): Product size
```

## API Reference

### Authentication
All API endpoints require user authentication. Use the standard Odoo session authentication.

### 1. Get External Data
```http
POST /api/v1/product_cleansing/external_data
Content-Type: application/json

Request:
{
    "source": "Google Shopping"  # Optional filter
}

Response:
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "custom_id": "uuid-string",
            "source": "Google Shopping",
            "data": { ... },
            "version": 1
        }
    ]
}
```

### 2. Create Product Match
```http
POST /api/v1/product_cleansing/match
Content-Type: application/json

Request:
{
    "product_id": 1,
    "external_data_id": 1,
    "matching_score": 85
}

Response:
{
    "status": "success",
    "data": {
        "id": 1,
        "status": "pending"
    }
}
```

## Installation

### Prerequisites
- Odoo 18 Enterprise
- Python 3.10+
- Access to Odoo's addons directory

### Steps
1. Copy module to addons directory:
```bash
cp -r product_cleansing /path/to/odoo/addons/
```

2. Update addons list in Odoo:
- Go to Apps menu
- Click 'Update Apps List'

3. Install module:
- Search for 'Product Data Cleansing'
- Click Install

## Configuration

### Access Rights
The module creates the following access rights:
- Read/write access to external data for base users
- Read/write access to match mappings for base users

### Initial Setup
1. Configure data sources:
- Go to Product Cleansing > Configuration > Data Sources
- Add your external data sources

2. Set up matching rules (optional):
- Go to Product Cleansing > Configuration > Matching Rules
- Configure automatic matching criteria

## Usage Guide

### Managing External Data
1. Import external data:
- Use the API endpoint `/api/v1/product_cleansing/external_data`
- Or use the UI: Product Cleansing > External Data > Create

### Product Matching
1. Manual matching:
- Go to Product Cleansing > Product Matches
- Create new match mapping
- Set confidence score and validate

2. API-based matching:
- Use the endpoint `/api/v1/product_cleansing/match`
- Provide product_id and external_data_id

### Data Enrichment
1. View matches:
- Open product form
- Go to 'External Data Matching' tab

2. Validate matches:
- Select match record
- Update status to 'matched'
- System automatically sets score to 100

## Best Practices
1. Data Management:
- Regularly clean external data
- Maintain version history
- Document data sources

2. Matching Process:
- Review automatic matches
- Validate high-impact matches first
- Monitor matching scores

3. API Usage:
- Implement proper error handling
- Use pagination for large datasets
- Cache frequently accessed data

## Troubleshooting

### Common Issues
1. Match Score Validation:
```python
Error: "Matching score must be between 0 and 100"
Solution: Ensure score is within valid range
```

2. Duplicate Matches:
```python
Error: "A product can only be matched once with an external data record"
Solution: Check existing matches before creating new ones
```

## Support
- GitHub Issues: [Report Issues](https://github.com/ArulWeb3/cursormcptest/issues)
- Documentation: [View Full Documentation](https://github.com/ArulWeb3/cursormcptest/tree/dev/docs)
