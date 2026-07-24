from enum import Enum, auto

# 3 different states for the spacecraft
class Mode(Enum):
    SAFE = auto() # Spacecraft enters SAFE mode when there is danger
    SUN_POINTING = auto() # Spacecraft enters SUN_POINTING when it is facing the sun
    NOMINAL = auto() # Spacecraft is NOMINAL when all is normal

