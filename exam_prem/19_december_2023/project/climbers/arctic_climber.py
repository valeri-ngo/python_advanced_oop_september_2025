from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    MINIMUM_REQUIRED = 100

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return True if self.strength >= self.MINIMUM_REQUIRED else False

    def climb(self, peak: BasePeak):
        extreme_cost = 20 * 2
        advanced_cost = 20 * 1.5

        if peak.difficulty_level == 'Extreme':
            self.strength -= extreme_cost

        elif peak.difficulty_level == 'Advanced':
            self.strength -= advanced_cost

        self.conquered_peaks.append(peak.name)
