from pydantic import BaseModel, Field
from typing import Optional, Dict

class WCIRequest(BaseModel):
    player_id: str
    player_name: str

    match_id: str
    innings_id: str

    # Batting
    runs: int = Field(..., ge=0)
    balls_faced: int = Field(..., ge=0)

    # Bowling
    overs_bowled: float = Field(..., ge=0)
    runs_conceded: int = Field(..., ge=0)
    wickets: int = Field(..., ge=0)

    # Fielding
    catches: int = Field(0, ge=0)
    runouts: int = Field(0, ge=0)
    stumpings: int = Field(0, ge=0)

    # Khel AI extensions
    match: Optional[Dict] = None
    innings: Optional[Dict] = None
    teams: Optional[Dict] = None
    players: Optional[Dict] = None
