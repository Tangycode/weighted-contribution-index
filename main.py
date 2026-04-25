from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import WCIRequest
from services import compute_wci, validate_request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Weighted Contribution Index API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/weighted-contribution")
def weighted_contribution(request: WCIRequest):

    try:
        validate_request(request)
        result = compute_wci(request)
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
