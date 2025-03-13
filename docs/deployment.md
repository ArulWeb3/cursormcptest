# Deployment Guide

## Local Deployment

### Method 1: Direct Deployment

1. **Deploy Calculator API**
   ```bash
   # Navigate to calculator directory
   cd calculator
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the API server
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Deploy Frontend**
   ```bash
   # Navigate to calculator-frontend directory
   cd calculator-frontend
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the Streamlit app
   streamlit run app.py
   ```
   The frontend will be available at `http://localhost:8501`

### Method 2: Docker Deployment

1. **Using Docker Compose**
   ```bash
   # Build and start all services
   docker-compose up --build
   ```
   This will start:
   - Calculator API at `http://localhost:8000`
   - Frontend at `http://localhost:8501`

2. **Individual Container Deployment**
   ```bash
   # Build and run API
   cd calculator
   docker build -t calculator-api .
   docker run -p 8000:8000 calculator-api
   
   # Build and run Frontend
   cd calculator-frontend
   docker build -t calculator-frontend .
   docker run -p 8501:8501 calculator-frontend
   ```

## Production Deployment

### Environment Variables

```bash
# API Settings
API_HOST=0.0.0.0
API_PORT=8000

# Frontend Settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
API_BASE_URL=http://api.example.com
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name calculator.example.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

server {
    listen 80;
    server_name api.calculator.example.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Deployment Checklist

- [ ] API server running and accessible
- [ ] Frontend application running and accessible
- [ ] Environment variables configured
- [ ] API endpoint configured in frontend
- [ ] SSL certificates installed (for production)
- [ ] Firewall rules configured
- [ ] Error logging enabled
- [ ] Monitoring setup

## Monitoring

1. **API Monitoring**
   - Endpoint health checks
   - Response times
   - Error rates

2. **Frontend Monitoring**
   - User sessions
   - Page load times
   - Error tracking

## Backup Strategy

1. **Code Backup**
   ```bash
   # Backup application code
   rsync -av /app/calculator/ /backup/calculator/
   rsync -av /app/calculator-frontend/ /backup/calculator-frontend/
   ```

2. **Log Backup**
   ```bash
   # Backup logs
   rsync -av /var/log/calculator/ /backup/logs/
   ```

## Scaling

1. **API Scaling**
   ```bash
   # Run multiple API instances
   docker-compose up --scale calculator-api=3
   ```

2. **Load Balancing**
   ```nginx
   upstream calculator_api {
       server localhost:8000;
       server localhost:8001;
       server localhost:8002;
   }
   ```