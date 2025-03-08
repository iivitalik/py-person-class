class Person:
    people = {}  # Stores all Person instances by name

    def __init__(self, name: str, age: int) -> None:
        if name in Person.people:
            raise ValueError(f"Error: Person with name '{name}' already exists.")
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self  # Store the instance globally

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(data: list) -> list:
    person_list = []

    # First pass: Create all Person objects (handling duplicate names)
    for person in data:
        if person["name"] in Person.people:
            print(f"Warning: Duplicate name '{person['name']}' found. Skipping entry.")
            continue  # Skip duplicate entries
        try:
            person_obj = Person(person["name"], person["age"])
            person_list.append(person_obj)
        except ValueError as e:
            print(e)  # Error already handled in __init__, but log it just in case

    # Second pass: Assign relationships
    for person in data:
        instance = Person.people.get(person["name"])
        if not instance:
            continue  # Skip if instance wasn't created

        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            instance.wife = Person.people.get(wife_name)
            if instance.wife is None:
                print(f"Warning: Wife '{wife_name}' not found for '{instance.name}'.")

        if "husband" in person and person["husband"]:
            husband_name = person["husband"]
            instance.husband = Person.people.get(husband_name)
            if instance.husband is None:
                print(f"Warning: Husband '{husband_name}' not found for '{instance.name}'.")

    return person_list
