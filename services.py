def safe_div(a, b):
    return a / b if b != 0 else 0


def validate_request(data):
    if not data.player_id:
        raise ValueError("Missing player_id")

    if not data.player_name:
        raise ValueError("Missing player_name")

    if not data.match_id:
        raise ValueError("Missing match_id")

    if not data.innings_id:
        raise ValueError("Missing innings_id")

    if data.balls_faced == 0 and data.runs > 0:
        raise ValueError("Invalid batting data: runs > 0 but balls_faced = 0")

    if data.overs_bowled < 0:
        raise ValueError("overs_bowled cannot be negative")

    if data.runs_conceded < 0:
        raise ValueError("runs_conceded cannot be negative")


def compute_wci(data):

    notes = []

    # --------------------
    # Batting
    # --------------------
    strike_efficiency = safe_div(data.runs, data.balls_faced) * 100
    run_impact = data.runs

    # Explanation:
    # 70% strike rate importance, 30% volume scoring
    batting_score = (0.7 * strike_efficiency) + (0.3 * run_impact)

    # --------------------
    # Bowling
    # --------------------
    if data.overs_bowled == 0:
        economy = 0
        economy_impact = 0
        notes.append("No bowling contribution (overs_bowled = 0)")
    else:
        economy = safe_div(data.runs_conceded, data.overs_bowled)

        # Explanation:
        # Lower economy is better → inverted scale
        economy_impact = max(0, 10 - economy)

    # Each wicket weighted heavily
    wicket_impact = data.wickets * 20

    # 60% wickets, 40% economy
    bowling_score = (0.6 * wicket_impact) + (0.4 * economy_impact)

    # --------------------
    # Fielding
    # --------------------
    fielding_impact = (
        data.catches * 10 +
        data.runouts * 15 +
        data.stumpings * 15
    )

    fielding_score = fielding_impact

    # --------------------
    # Total (Weighted)
    # --------------------
    total_raw = (
        0.4 * batting_score +
        0.4 * bowling_score +
        0.2 * fielding_score
    )

    # Normalize to 0–100
    normalized_score = min(100, round(total_raw / 2, 2))

    # Impact classification
    if normalized_score >= 75:
        impact = "High"
    elif normalized_score >= 40:
        impact = "Medium"
    else:
        impact = "Low"

    return {
        "player_id": data.player_id,
        "player_name": data.player_name,
        "match_id": data.match_id,
        "innings_id": data.innings_id,

        "batting_score": round(batting_score, 2),
        "bowling_score": round(bowling_score, 2),
        "fielding_score": round(fielding_score, 2),

        "total_score": normalized_score,
        "impact": impact,

        "strike_efficiency": round(strike_efficiency, 2),
        "run_impact": run_impact,
        "economy": round(economy, 2),
        "wicket_impact": wicket_impact,
        "economy_impact": round(economy_impact, 2),
        "fielding_impact": fielding_impact,

        "weights": {
            "batting": 0.4,
            "bowling": 0.4,
            "fielding": 0.2
        },

        "formula_explanation": {
            "batting": "70% strike efficiency + 30% runs",
            "bowling": "60% wickets + 40% economy impact",
            "fielding": "Catches (10), Runouts (15), Stumpings (15)",
            "normalization": "Total score scaled to 0–100 for interpretability"
        },

        "notes": notes
    }
