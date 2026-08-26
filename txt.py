import math 
def vertical_force(magnitude: float, angle_degrees: float) -> float:
    """Calculate the vertical component of force at an angle to the horizontal."""
    angle_radians = math.radians(angle_degrees)
    return magnitude * math.sin(angle_radians)

x = vertical_force (54, 27)
print(f"Vertical component: {x:.2f} N")

print("hello world")
