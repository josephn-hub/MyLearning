import random
import string


def generate_vehicle_id() -> str:
    """Generates a random vehicle id."""
    return "".join(random.choices(string.ascii_uppercase, k=3))


def generate_vehicle_license(id: str) -> str:
                    """Generates a random vehicle license plate."""
                    first_two_digits = id[:2]
                    middle_two_digits = "".join(random.choices(string.digits, k=2))
                    last_two_digits = "".join(random.choices(string.ascii_uppercase, k=2))
                    return f"{first_two_digits}-{middle_two_digits}-{last_two_digits}"


vehicle_id = generate_vehicle_id()
print(vehicle_id)

generating_vehicle_id = generate_vehicle_license(vehicle_id)
print(generating_vehicle_id)
