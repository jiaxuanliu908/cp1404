class Guitar:
    def __init__(self, guitar_name="", guitar_year=0, guitar_cost=0):
        self.name = guitar_name
        self.year = guitar_year
        self.cost = guitar_cost

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year


    def get_age(self):
        return 2023 - int(self.year)

    def is_vintage(self):
        return self.get_age() >= 50
