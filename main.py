from typing import Literal

Stack = Literal["STANDARD", "SPECIAL", "REJECTED"]

def sort(width: float, height: float, length: float, mass: float) -> Stack:
    """
    Route a package to the correct stack based on dimensions (cm) and mass (kg).

    Bulky  := volume >= 1_000_000 cm^3 OR any dimension >= 150 cm
    Heavy  := mass >= 20 kg
    Return := "REJECTED" if bulky AND heavy
              "SPECIAL"  if exactly one of bulky/heavy is true
              "STANDARD" otherwise
    """
    # Defensive: clamp negative dimensions to 0 (non-physical inputs).
    w = max(0.0, float(width))
    h = max(0.0, float(height))
    l = max(0.0, float(length))
    m = float(mass)

    volume = w * h * l
    is_bulky = volume >= 1_000_000 or max(w, h, l) >= 150
    is_heavy = m >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
