from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MINIMUM_REQUIRED = 75

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return True if self.strength >= self.MINIMUM_REQUIRED else False

    def climb(self, peak: BasePeak):
        other_cost = 30 * 2.5
        advanced_cost = 30 * 1.3

        if peak.difficulty_level == 'Advanced':
            self.strength -= advanced_cost
        else:
            self.strength -= other_cost

        self.conquered_peaks.append(peak.name)
