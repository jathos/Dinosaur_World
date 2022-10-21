from django.db import models

class Dinosaur():
    def __init__(self, species, group, diet):
        self.species = species
        self.group = group
        self.diet = diet

dinosaurs = [
    Dinosaur('Tyrannosaurus', 'Theropod', 'Carnivore' ),
    Dinosaur('Carnotaurus', 'Theropod', 'Carnivore'),
    Dinosaur('Therizinosaurus', 'Theropod', 'Herbivore')
]
