class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        if name in Person.people:
            raise ValueError(f"Person with '{name}' already exists.")
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(data: list) -> list:
    person_list = []

    for person in data:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)

    for person in data:
        instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                instance.wife = Person.people[wife_name]
            else:
                print(
                    f"Warning: {wife_name} not found in dictionary."
                )

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                instance.husband = Person.people[husband_name]
            else:
                print(
                    f"Warning: {husband_name} not found in dictionary."
                )

    return person_list
