from battleships.pirate_battleship import PirateBattleship
from zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str, volume = INITIAL_VOLUME):
        super().__init__(code, volume)


    def zone_info(self):
        battleships_total_count = len(self.ships)
        pirateships_count = sum(1 for p in self.ships if isinstance(p, PirateBattleship))

        ordered_ships = self.get_ships()
        ship_names = [s for s in ordered_ships]

        ships_line = f'\n#{", ".join(ship_names)}#' if ship_names else ''
        return (
            f'@Royal Zone Statistics@\n'
            f'Code: {self.code}; Volume: {self.volume}\n'
            f'Battleships currently in the Royal Zone: {battleships_total_count}, '
            f'{pirateships_count} out of them are Pirate Battleships.'
            f'{ships_line}'
        )
