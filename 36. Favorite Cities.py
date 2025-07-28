class City:

    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

pune = City('Pune', 'India', 1500000, ['Shaniwar Wada', 'Aga Khan Palace', 'Sinhagad Fort'])
chicago = City('Chicago', "USA", 1000000, ['Navy Pier', 'Millennium Park', 'Cloud Gate', 'Wrigley Field'])

print(vars(pune))
print(vars(chicago))
