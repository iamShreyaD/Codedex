class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ' ' + self.name)

    def display_details(self):
        print('Entry Number: ' + str(self.entry))
        print('Name: ' + self.name)
        print('Type: ' + self.types)
        print('Description: ' + self.description)
        print(self.name + ' has already been caught!')

charmander = Pokemon(8, 'Charmander', 'Normal', 'Very smart and compassionate', False)
charmander.speak()
charmander.display_details()

squirtle = Pokemon(56, 'Squirtle', 'Fire', 'Can ommit fire', True)
squirtle.speak()
squirtle.display_details()

bulbasaur = Pokemon(43, 'Bulbasaur', 'Ice', 'Can fly with beautiful wings', False)
bulbasaur.speak()
bulbasaur.display_details()



        