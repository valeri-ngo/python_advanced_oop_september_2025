from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = {
        'ArcticClimber': ArcticClimber,
        'SummitClimber': SummitClimber
    }

    VALID_PEAKS = {
        'ArcticPeak': ArcticPeak,
        'SummitPeak': SummitPeak
    }

    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        if any(c.name == climber_name for c in self.climbers):
            return f"{climber_name} has been already registered."

        climber = self.VALID_CLIMBERS[climber_type](climber_name)
        self.climbers.append(climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        peak = self.VALID_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear:list[str]):
        climbers = next((c for c in self.climbers if c.name == climber_name), None)
        peaks = next((p for p in self.peaks if p.name == peak_name), None)

        recommended_gear = peaks.get_recommended_gear()
        missing_gear = sorted([item for item in recommended_gear if item not in gear])

        if missing_gear:
            climbers.is_prepared = False
            return (f"{climber_name} is not prepared to climb {peak_name}. "
                    f"Missing gear: {', '.join(missing_gear)}.")
        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        peak = next((p for p in self.peaks if p.name == peak_name), None)

        if not climber:
            return f'Climber {climber_name} is not registered yet.'

        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."


    def get_statistics(self):
        climbers = [c for c in self.climbers if c.conquered_peaks]

        sorted_climbers = sorted(climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        climbed_peaks = {peak_name for c in climbers for peak_name in c.conquered_peaks}
        total_climbed_peaks = len(climbed_peaks)

        result = [f"Total climbed peaks: {total_climbed_peaks}\n"
                  f"**Climber's statistics:**"]

        for c in sorted_climbers:
            result.append(str(c))

        return "\n".join(result)

