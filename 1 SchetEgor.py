import random

class Animal:
    def __init__(self, name, size, food_type, habitat, lifespan):
        self.name = name
        self.size = size
        self.food_type = food_type
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = 0
        self.satiation = 100
        self.gender = random.choice(['Male', 'Female'])

class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant_food = 1000

    def add_animal(self, animal):
        self.animals.append(animal)

    def increase_plant_food(self, amount):
        self.plant_food += amount

    def show_animal_info(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Age: {animal.age}, Satiation: {animal.satiation}, Gender: {animal.gender}")

    def reproduce(self, animal_type):
        animals_of_type = [a for a in self.animals if a.name == animal_type]
        males = [a for a in animals_of_type if a.gender == 'Male' and a.satiation > 50]
        females = [a for a in animals_of_type if a.gender == 'Female' and a.satiation > 50]
        if males and females:
            male = random.choice(males)
            female = random.choice(females)
            new_animals = []
            if male.habitat == 'Water':
                if male.age > 0:  # Adjust age threshold as per your requirement
                    new_animals = [Animal(male.name, male.size, male.food_type, male.habitat, male.lifespan) for _ in range(10)]
                    for new_animal in new_animals:
                        new_animal.satiation = 23
            elif male.habitat == 'Air':
                if male.age > 3:  # Adjust age threshold as per your requirement
                    new_animals = [Animal(male.name, male.size, male.food_type, male.habitat, male.lifespan) for _ in range(4)]
                    for new_animal in new_animals:
                        new_animal.satiation = 64
            elif male.habitat == 'Land':
                if male.age > 5:  # Adjust age threshold as per your requirement
                    new_animals = [Animal(male.name, male.size, male.food_type, male.habitat, male.lifespan) for _ in range(2)]
                    for new_animal in new_animals:
                        new_animal.satiation = 73
            self.animals.extend(new_animals)

    def simulate_time_step(self):
        for animal in self.animals[:]:  # Copy list to avoid changes during iteration
            animal.age += 1
            if animal.age >= animal.lifespan:
                self.animals.remove(animal)
                self.plant_food += animal.size
            elif animal.food_type == 'Plants':
                if self.plant_food > 0:
                    self.plant_food -= 1
                    animal.satiation = min(animal.satiation + 26, 100)
                else:
                    animal.satiation -= 9
            else:
                possible_prey = [a for a in self.animals if a.name in animal.food_type]
                if possible_prey:  # Check that list is not empty
                    prey = random.choice(possible_prey)
                    self.animals.remove(prey)
                    animal.satiation = min(animal.satiation + 53, 100)
                else:
                    animal.satiation -= 16
            if animal.satiation < 10:
                self.animals.remove(animal)
                self.plant_food += animal.size

# Create ecosystem and add initial animals
ecosystem = Ecosystem()
for _ in range(5):
    ecosystem.add_animal(Animal("Fish", 1, "Plants", "Water", 5))
    ecosystem.add_animal(Animal("Bird", 1, ["Fish"], "Air", 4))
    ecosystem.add_animal(Animal("Deer", 3, "Plants", "Land", 10))

# Infinite loop to run the ecosystem
while True:
    print("\nCurrent animal info:")
    ecosystem.show_animal_info()
    command = input("Enter command (time_step / reproduce [animal_type] / add_animal / increase_plant_food / exit): ").strip().lower()
    if command == 'time_step':
        ecosystem.simulate_time_step()
    elif command.startswith('reproduce'):
        _, animal_type = command.split(maxsplit=1)
        ecosystem.reproduce(animal_type)
    elif command == 'add_animal':
        name = input("Enter animal name: ").strip()
        size = int(input("Enter animal size: ").strip())
        food_type = input("Enter animal food type (Plants or list of prey): ").strip()
        if food_type.lower() != "plants":
            food_type = food_type.split(', ')
        habitat = input("Enter animal habitat (Water, Air, Land): ").strip()
        lifespan = int(input("Enter animal lifespan: ").strip())
        ecosystem.add_animal(Animal(name, size, food_type, habitat, lifespan))
    elif command == 'increase_plant_food':
        amount = int(input("Enter amount of plant food to add: ").strip())
        ecosystem.increase_plant_food(amount)
    elif command == 'exit':
        break
    else:
        print("Unknown command. Please try again.")