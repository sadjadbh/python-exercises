"""
A simple object-oriented model for representing animals in a zoo.

This module contains the Animal and Bird classes to demonstrate inheritance.
"""


class Animal:
    """
    Animal class to represent an animal with its basic attributes.

    Attributes:
    - zoo_name (class variable): Name of the zoo where the animal resides.
    - name (str): The name of the animal.
    - species (str): The species of the animal.
    - age (int): The age of the animal.
    - sound (str): The sound the animal makes.
    """

    zoo_name = 'Western Zoo'  # Class-level variable shared by all instances

    def __init__(self, name, species, age, sound):
        """
        Initialize the Animal object with provided attributes.

        Parameters:
        - name (str): The name of the animal.
        - species (str): The species of the animal.
        - age (int): The age of the animal.
        - sound (str): The sound the animal makes.
        """
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        """
        Method that returns the sound the animal makes.

        Returns:
        - str: Sound description.
        """
        return f"This animal makes a sound like: {self.sound}"

    def info(self):
        """
        Returns the information about the animal.

        Returns:
        - str: A string with the animal's name, species, age, and sound.
        """
        return f"\nName: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nSound: {self.sound}\n"

    def __str__(self):
        """
        Magic method to return a human-readable string representation of the Animal object.

        Returns:
        - str: A string that represents the animal’s information.
        """
        return self.info()


class Bird(Animal):
    """
    Bird class that inherits from Animal, adding the wing span attribute.

    Inherits all attributes and methods from Animal, but overrides the make_sound method.

    Attributes:
    - wing_span (int): The wing span of the bird.
    """

    def __init__(self, name, species, age, sound, wing_span):
        """
        Initialize the Bird object with additional wing_span attribute.

        Parameters:
        - name (str): The name of the bird.
        - species (str): The species of the bird.
        - age (int): The age of the bird.
        - sound (str): The sound the bird makes.
        - wing_span (int): The wing span of the bird.
        """
        super().__init__(name, species, age, sound)  # Initialize inherited attributes
        self.wing_span = wing_span  # New attribute for birds

    def make_sound(self):
        """
        Overridden method that returns a unique sound for the bird.

        Returns:
        - str: Sound description specific to the bird.
        """
        return f"This bird makes a sound like: {self.sound}"


# Create instances of Animal and Bird
animal1 = Animal('Lion', 'West African', 9, 'Roar')
animal2 = Bird('Eagle', 'Bald', 20, 'Screech', 7)

# Print the Animal and Bird objects, which will use the __str__ method
print(animal1)
print(animal2)

# Print detailed information of the animal and bird
print(animal1.info())
print(animal2.info())

# Print the sounds they make
print(animal1.make_sound())
print(animal2.make_sound())

# Demonstrating the class variable 'zoo_name'
print(animal1.zoo_name)  # Accessing the zoo name via instance
Animal.zoo_name = 'Grand Zoo'  # Changing the class variable
print(animal2.zoo_name)  # Accessing the updated zoo name
