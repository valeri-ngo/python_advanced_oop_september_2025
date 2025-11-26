from typing import List

from battleships.base_battleship import BaseBattleship
from zones.base_zone import BaseZone


class BattleManager:
    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        pass

    @staticmethod
    def _find_obj_by_type(obj_type, collection):
        if not collection:
            return None

        if isinstance(obj_type, type):
            return next((obj for obj in collection if isinstance(obj, obj_type)), None)

        if isinstance(obj_type, str):
            type_name = obj_type.strip()
        else:
            type_name = getattr(obj_type, '__name__', str(obj_type))

        type_name = str(obj_type)
        return next((obj for obj in collection if getattr(obj, 'type', obj.__class__.__name__) == type_name), None)

    @staticmethod
    def _find_obj_by_name(obj_name, collection):
        if not collection or obj_name is None:
            return None

        name = obj_name if isinstance(obj_name, str) else str(obj_name)
        return next((obj for obj in collection if getattr(obj, "name", None) == name),None)