from fastapi import FastAPI
from schemas import PlayerInput, ContributionResponse
from services import calculate_contribution

app = FastAPI()

@app.post("/weighted-contribution", response_model=ContributionResponse)
def weighted_contribution(data: PlayerInput):
    return calculate_contribution(data)
