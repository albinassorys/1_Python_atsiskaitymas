# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title: str, director: str, budget: int):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        if self.budget >= 100000000:
            print(True)
        else:
            print(False)


movie1 = Movie("Jaws", "Steven Spielberg", 9000000)
movie2 = Movie("Terminator", "James Cameron", 6400000)
movie3 = Movie("Titanic", "James Cameron", 200000000)
movie4 = Movie("Coffee and Cigarettes", "James Jarmusch", 0)
movie5 = Movie("Tadas Blinda. Pradžia", "Donatas Ulvydas", 1000000)

movie1.was_expensive()
movie2.was_expensive()
movie3.was_expensive()
movie4.was_expensive()
movie5.was_expensive()
