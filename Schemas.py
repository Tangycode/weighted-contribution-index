from pydantic import BaseModel

class PlayerInput(BaseModel):
    runs_scored: int
    balls_faced: int
    strike_rate: float

    overs_bowled: float
    runs_conceded: int
    wickets_taken: int

    catches: int
    run_outs: int
    stumpings: int


class ContributionResponse(BaseModel):
    batting_score: float
    bowling_score: float
    fielding_score: float
    total_score: float
    impact: str
