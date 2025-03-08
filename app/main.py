class Person:
    people = {}  # Stores all Person instances by their name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self  # Store the instance globally

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            instance.wife = Person.people.get(person["wife"])

        if "husband" in person and person["husband"]:
            instance.husband = Person.people.get(person["husband"])

    return person_list
