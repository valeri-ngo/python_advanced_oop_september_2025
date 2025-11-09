from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200_000
    SPONSORS = {}

    @property
    def team_data(self):
        expenses = 200_000
        sponsors = {"Petronas": {1: 1_000_000, 3: 500_000},
                    "TeamViewer": {5: 100_000, 7: 50_000},
                    }
        return expenses, sponsors