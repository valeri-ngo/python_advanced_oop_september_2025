from battleships.royal_battleship import RoyalBattleship
from zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str, volume: int):
        super().__init__(code, volume)


    def zone_info(self):
        battleships_total_count = len(self.ships)
        royalships_count = sum(1 for r in self.ships if isinstance(r, RoyalBattleship))

        ordered_ships = self.get_ships()
        ship_names = [s for s in ordered_ships]

        ships_line = f'\n#{", ".join(ship_names)}#' if ship_names else ''

        return (
            f'@Pirate Zone Statistics@\n'
            f'Code: {self.code}; Volume: {self.volume}\n'
            f'Battleships currently in the Pirate Zone: {battleships_total_count}, '
            f'{royalships_count} out of them are Royal Battleships.'
            f'{ships_line}'
        )
