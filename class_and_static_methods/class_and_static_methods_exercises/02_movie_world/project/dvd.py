import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: int, age_restriction: int):
        self.name: str = name
        self.id: id = id
        self.creation_year: int = creation_year
        self.creation_month: int = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> 'DVD':
        _, month, year = [int(x) for x in date.split(".")]
        month_name = calendar.month_name[month]
        return cls(name, id, year, month_name, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})"
                f" has age restriction {self.age_restriction}. "
                f"Status: {'' if self.is_rented else 'not '}rented")