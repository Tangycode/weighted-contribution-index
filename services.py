from schemas import PlayerInput

def calculate_contribution(data: PlayerInput):

    # ---------------- Batting ----------------
    strike_eff = data.strike_rate / 100
    run_impact = data.runs_scored / 50

    batting_score = (0.6 * run_impact) + (0.4 * strike_eff)

    # ---------------- Bowling ----------------
    if data.overs_bowled > 0:
        economy = data.runs_conceded / data.overs_bowled
    else:
        economy = 8  # neutral fallback

    wicket_impact = data.wickets_taken * 0.5
    economy_impact = max(0, (8 - economy) / 8)

    bowling_score = (0.7 * wicket_impact) + (0.3 * economy_impact)

    # ---------------- Fielding ----------------
    fielding_score = (
        data.catches * 0.3 +
        data.run_outs * 0.5 +
        data.stumpings * 0.4
    )

    # ---------------- Final Score ----------------
    total_score = (
        0.4 * batting_score +
        0.4 * bowling_score +
        0.2 * fielding_score
    )

    # ---------------- Interpretation ----------------
    if total_score >= 1.5:
        impact = "High Impact"
    elif total_score >= 1.0:
        impact = "Moderate Impact"
    else:
        impact = "Low Impact"

    return {
        "batting_score": round(batting_score, 2),
        "bowling_score": round(bowling_score, 2),
        "fielding_score": round(fielding_score, 2),
        "total_score": round(total_score, 2),
        "impact": impact
    }

