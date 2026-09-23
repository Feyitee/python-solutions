
def filter_prices(prices, cutoff):
    result = []

    for price in prices:
        if price >= cutoff:
            result.append(price)

    return result


response =  {
    "model": "gpt",
    "score" : 0.92
}
response["score"]

numbers = [ 3, 5, 7, 5, 9]
seen = set()

for value in numbers:
    if value in seen:
        print (value)
    seen.add(value)



# Class blueprint - Things created from class


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} ad I am {self.age} years old"

        
michael = Student("Michael", 25)
sarah = Student("Sarah", 15)

# Each objeck keeps its own data but from the same class
# Inheritance means one class can reuse what another class already knows

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass