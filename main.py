from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import uvicorn
from typing import Dict, Any, List
from technology_tracker import analyze
from technology_tracker.core.config import tech_db, cat_db

app = FastAPI(
    title="Website Technology Profiler",
    description="API to detect technologies used on websites (based on Wappalyzer logic)",
    version="F0.31",
    docs_url="/",
    redoc_url="/redoc"
)

class ScanRequest(BaseModel):
    url: HttpUrl
    scan_type: str = 'full' # 'fast', 'balanced', 'full'

class TechnologyInfo(BaseModel):
    version: str | None
    categories: List[str]

class ScanResponse(BaseModel):
    url: str
    technologies: Dict[str, TechnologyInfo]

class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/health", response_model=HealthResponse, tags=["System"])
def health_check():
    """Check if the API is running"""
    return {"status": "ok", "version": "F0.31"}

@app.post("/scan", response_model=ScanResponse, tags=["Scan"])
def scan_website(request: ScanRequest):
    try:
        url_str = str(request.url)
        # analyze function expects a string URL
        results = analyze(
            url=url_str,
            scan_type=request.scan_type,
            threads=3
        )
        
        if not results or url_str not in results:
            return {"url": url_str, "technologies": {}}

        # Format results for the response
        formatted_techs = {}
        raw_techs = results.get(url_str, {})
        
        for tech_name, tech_data in raw_techs.items():
            formatted_techs[tech_name] = TechnologyInfo(
                version=tech_data.get("version"),
                categories=tech_data.get("categories", [])
            )
            
        return ScanResponse(url=url_str, technologies=formatted_techs)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scan failed: {str(e)}")


@app.get("/technologies", tags=["Data"])
def get_technologies():
    """Get the full list of detectable technologies"""
    return tech_db

@app.get("/categories", tags=["Data"])
def get_categories():
    """Get the list of technology categories"""
    return cat_db


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)