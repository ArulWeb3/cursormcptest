# Quick Start Guide: Odoo Product Cleansing Module

## 🚀 5-Minute Setup

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/ArulWeb3/cursormcptest.git

# Copy module to Odoo addons directory
cp -r cursormcptest/product_cleansing /path/to/odoo/addons/

# Restart Odoo server
sudo service odoo restart
```

### 2. Module Activation
1. Login to Odoo
2. Go to Apps menu
3. Click 'Update Apps List'
4. Search for 'Product Cleansing'
5. Click Install

## 🎯 First Steps

### 1. Quick Data Import
```python
# Using Python requests
import requests

# Login to get session
session = requests.Session()
login_url = 'http://localhost:8069/web/session/authenticate'
login_data = {
    'jsonrpc': '2.0',
    'params': {
        'db': 'your_database',
        'login': 'your_email',
        'password': 'your_password'
    }
}
session.post(login_url, json=login_data)

# Import external data
data = {
    'jsonrpc': '2.0',
    'params': {
        'source': 'Google Shopping',
        'data': {
            'name': 'Test Product',
            'price': 99.99,
            'sku': 'TEST001'
        }
    }
}
response = session.post(
    'http://localhost:8069/api/v1/product_cleansing/external_data',
    json=data
)
```

### 2. Quick Match Creation
```python
# Create a product match
match_data = {
    'jsonrpc': '2.0',
    'params': {
        'product_id': 1,        # Your Odoo product ID
        'external_data_id': 1,   # External data record ID
        'matching_score': 90
    }
}
response = session.post(
    'http://localhost:8069/api/v1/product_cleansing/match',
    json=match_data
)
```

## 🖥️ UI Quick Access

### 1. View External Data
1. Go to `Product Cleansing > External Data`
2. Click `Create` to add manually
3. Or view imported data

### 2. Manage Matches
1. Go to `Product Cleansing > Product Matches`
2. Click `Create` for new match
3. Select product and external data
4. Set matching score
5. Save and validate

## 📱 Quick API Reference

### 1. Get External Data
```bash
curl -X POST \
  http://localhost:8069/api/v1/product_cleansing/external_data \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "params": {}
  }'
```

### 2. Create Match
```bash
curl -X POST \
  http://localhost:8069/api/v1/product_cleansing/match \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "params": {
        "product_id": 1,
        "external_data_id": 1,
        "matching_score": 90
    }
  }'
```

## 🔍 Quick Validation

### 1. Check Installation
```python
# Using Odoo Shell
>>> env['ir.module.module'].search([('name', '=', 'product_cleansing')]).state
'installed'
```

### 2. Test Data Access
```python
# Check external data
>>> env['product.external.data'].search_count([])

# Check matches
>>> env['product.match.mapping'].search_count([])
```

## 📊 Quick Reports

### 1. Matching Status
Go to `Product Cleansing > Product Matches` and group by:
- Status
- Matching Score
- Validation Date

### 2. Data Sources
Go to `Product Cleansing > External Data` and group by:
- Source
- Version
- Import Date

## 🚨 Quick Troubleshooting

### 1. Module Not Visible
```bash
# Update Odoo modules list
sudo service odoo restart
# Go to Apps and click 'Update Apps List'
```

### 2. API Access Issues
```python
# Check user has correct access rights
>>> user = env['res.users'].browse(env.uid)
>>> user.has_group('base.group_user')
True
```

## 🎓 Next Steps

1. Read [Full Documentation](./odoo_product_cleansing.md)
2. Explore [API Reference](./api-reference.md)
3. Check [Development Guide](./development-guide.md)

## 💡 Tips

1. **Bulk Operations**
   - Use API for large imports
   - Group matches by product category
   - Validate matches in batches

2. **Performance**
   - Index frequently searched fields
   - Use pagination in API calls
   - Schedule large imports during off-hours

3. **Best Practices**
   - Always validate matches
   - Keep external data updated
   - Monitor matching scores

## 🆘 Quick Help

- Report issues: [GitHub Issues](https://github.com/ArulWeb3/cursormcptest/issues)
- Documentation: [Full Docs](./odoo_product_cleansing.md)
- Community: [Odoo Community](https://www.odoo.com/forum/help-1)