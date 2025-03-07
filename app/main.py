class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(data: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in data]

    for person in data:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]

    return person_list
