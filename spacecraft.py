from enum import Enum, auto

# 3 different states for the spacecraft
class Mode(Enum):
    SAFE = auto() # Spacecraft enters SAFE mode when there is danger
    SUN_POINTING = auto() # Spacecraft enters SUN_POINTING when it is facing the sun
    NOMINAL = auto() # Spacecraft is NOMINAL when all is normal

# Defining Spacecraft

class Spacecraft:
    def __init__(self):
        self.mode = Mode.SAFE
        self.battery_lvl = 40.0 # Starting low to show transitions through modes
        self.in_eclipse = False # False means the craft is not under the shadow of the Earth

    def update_env(self, t, orbit_period=90.0, eclipse_frac=0.35):
        # First 35 minutes of each 90 min orbit are an eclipse
        # Job of function is to indicatewhen there is an eclipse
        phase = (t % orbit_period) / orbit_period
        self.in_eclipse = phase < eclipse_frac

    def update_power(self, dt, charge_rate=0.5, drain_rate=0.3):
        if self.in_eclipse:
            self.battery_lvl -= drain_rate * dt # Drains when there is no sunlight
        else: 
            self.battery_lvl += charge_rate * dt # Charges in the sunglight
        self.battery_lvl = max(0.0, min(100.0, self.battery_lvl)) # Ensures simulator doesn't display a number over 100%

    def update_mode(self):
        if self.battery_lvl < 20:
            self.mode = Mode.SAFE
        elif self.battery_lvl < 60 or self.in_eclipse:
            self.mode = Mode.SUN_POINTING
        else:
            self.mode = Mode.NOMINAL

    def step(self, t, dt):
        self.update_env(t)
        self.update_power(dt)
        self.update_mode()
        return {
            "t": t,
            "mode": self.mode.name,
            "battery_lvl": round(self.battery_lvl, 2),
            "eclipse": self.in_eclipse
        }