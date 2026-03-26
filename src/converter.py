# Absolute zero in Celsius
ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    if c < ABSOLUTE_ZERO_C:
        raise ValueError(f"Temperature {c}°C is below absolute zero")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    if k < 0:
        raise ValueError(f"Kelvin cannot be negative: {k}")
    return k - 273.15


def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return float(value)

    # Convert to Celsius first
    if from_unit == "C":
        celsius = float(value)
    elif from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown unit: {from_unit}")

    # Convert from Celsius to target
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "K":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown unit: {to_unit}")
