import csv
from spacecraft import Spacecraft

def run_sim(duration=360, dt=1.0):
    sc = Spacecraft()
    log = []
    t = 0.0

    while t < duration:
        log.append(sc.step(t, dt))
        t += dt
    return log

