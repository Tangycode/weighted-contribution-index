# Weighted Contribution Index API

## Purpose
Evaluates a player's overall contribution using batting, bowling, and fielding metrics.

---

## Endpoint
POST /api/v1/weighted-contribution

---

## Input Schema
- player_id (string)
- player_name (string)
- match_id (string)
- innings_id (string)
- runs (int)
- balls_faced (int)
- overs_bowled (float)
- runs_conceded (int)
- wickets (int)
- catches (int)
- runouts (int)
- stumpings (int)

---

## Output Schema
- batting_score
- bowling_score
- fielding_score
- total_score (0–100 normalized)
- impact (High / Medium / Low)
- strike_efficiency
- run_impact
- economy
- wicket_impact
- economy_impact
- fielding_impact

---

## Formula
- Batting: 70% strike rate + 30% runs
- Bowling: 60% wickets + 40% economy impact
- Fielding: weighted actions
- Final: 40/40/20 weighted sum

---

## Sample Request
```json
{
  "player_id": "P001",
  "player_name": "Virat",
  "match_id": "M001",
  "innings_id": "I001",
  "runs": 60,
  "balls_faced": 40,
  "overs_bowled": 4,
  "runs_conceded": 28,
  "wickets": 2
}
