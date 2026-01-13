# Website Technology Profiler

A Python-based API service to scan websites and detect the technologies they are using (CMS, Analytics, Frameworks, etc.).

> **Credit**: This project is based on the logic and extensive technology database of the [Wappalyzer](https://www.wappalyzer.com/) Chrome Extension. It adapts that powerful detection engine into a standalone Python API.

## Features

- **REST API**: Simple JSON API to profile any URL.
- **Accurate Detection**: Uses the comprehensive Wappalyzer signatures.
- **Dockerized**: specific container setup for seamless Selenium/Firefox usage.

## Installation

### Using Docker (Recommended)

1.  Build and start the container:
    ```bash
    docker-compose up -d --build
    ```

2.  The API will be available at `http://localhost:8000`.

### Local Installation

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the server:
    ```bash
    uvicorn main:app --reload
    ```

## Usage

### API Documentation
- **Swagger UI**: [http://localhost:8000/](http://localhost:8000/)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

<img width="1587" height="950" alt="api-docs" src="https://github.com/user-attachments/assets/d24cabdf-39f0-4477-9c9d-3749c197d024" />


### Scan a Website
**Endpoint**: `POST /scan`

**Example Request**:
```bash
curl -X POST "http://localhost:8000/scan" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com", "scan_type": "full"}'
```

**Example Response**:
```json
{
  "url": "https://..../",
  "technologies": {
    "HSTS": {
      "version": "",
      "categories": [
        "Security"
      ]
    },
    "HTTP/2": {
      "version": "",
      "categories": [
        "Miscellaneous"
      ]
    },
    "Apple Sign-in": {
      "version": "",
      "categories": [
        "Authentication"
      ]
    },
    "DoubleClick Floodlight": {
      "version": "",
      "categories": [
        "Advertising"
      ]
    },
    "Firebase": {
      "version": "",
      "categories": [
        "Databases",
        "Development"
      ]
    },
    "GeeTest": {
      "version": "",
      "categories": [
        "Security"
      ]
    },
    "Google Analytics": {
      "version": "",
      "categories": [
        "Analytics"
      ]
    },
    "Google Optimize": {
      "version": "",
      "categories": [
        "A/B Testing"
      ]
    },
    "Google Publisher Tag": {
      "version": "",
      "categories": [
        "Advertising"
      ]
    },
    "Google Sign-in": {
      "version": "",
      "categories": [
        "Authentication"
      ]
    },
    "Google Tag Manager": {
      "version": "",
      "categories": [
        "Tag managers"
      ]
    },
    "Hubilo": {
      "version": "",
      "categories": [
        "Marketing automation"
      ]
    },
    "PerimeterX": {
      "version": "",
      "categories": [
        "Security"
      ]
    },
    "Criteo": {
      "version": "",
      "categories": [
        "Advertising",
        "Retargeting"
      ]
    },
    "core-js": {
      "version": "2.6.12",
      "categories": [
        "JavaScript libraries"
      ]
    },
    "Efilli": {
      "version": "",
      "categories": [
        "Cookie compliance"
      ]
    },
    "Facebook Login": {
      "version": "",
      "categories": [
        "Authentication"
      ]
    },
    "Facebook Pixel": {
      "version": "",
      "categories": [
        "Analytics"
      ]
    },
    "Funding Choices": {
      "version": "",
      "categories": [
        "Cookie compliance"
      ]
    },
    "Hotjar": {
      "version": "",
      "categories": [
        "Analytics"
      ]
    },
    "Microsoft Advertising": {
      "version": "",
      "categories": [
        "Advertising"
      ]
    },
    "Microsoft Clarity": {
      "version": "",
      "categories": [
        "Analytics"
      ]
    },
    "Nuxt.js": {
      "version": "",
      "categories": [
        "JavaScript frameworks",
        "Web frameworks",
        "Static site generator"
      ]
    },
    "PostHog": {
      "version": "",
      "categories": [
        "Analytics"
      ]
    },
    "Taboola": {
      "version": "",
      "categories": [
        "Advertising"
      ]
    },
    "TikTok Pixel": {
      "version": "",
      "categories": [
        "Analytics"
      ]
    },
    "Twitter Ads": {
      "version": "",
      "categories": [
        "Advertising"
      ]
    },
    "VWO": {
      "version": "",
      "categories": [
        "Analytics",
        "A/B Testing"
      ]
    },
    "Vue.js": {
      "version": "",
      "categories": [
        "JavaScript frameworks"
      ]
    },
    "Webpack": {
      "version": "",
      "categories": [
        "Miscellaneous"
      ]
    },
    "AppNexus": {
      "version": "",
      "categories": [
        "Advertising"
      ]
    },
    "Open Graph": {
      "version": "",
      "categories": [
        "Miscellaneous"
      ]
    },
    "RTB House": {
      "version": "",
      "categories": [
        "Retargeting"
      ]
    },
    "jsDelivr": {
      "version": "",
      "categories": [
        "CDN"
      ]
    }
  }
}
```

### Data Endpoints
The API exposes its internal technology database:

- **Technologies**: `GET /technologies` - Returns the full list of detectable technologies.
- **Categories**: `GET /categories` - Returns all technology categories.

### System Endpoints
- **Health Check**: `GET /health`

## Project Structure

- `main.py`: FastAPI application entry point.
- `technology_tracker/`: Core scanning library.
- `technology_tracker/data/`: Technology fingerprints (Wappalyzer compatible).
