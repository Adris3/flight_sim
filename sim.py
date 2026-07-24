import csv
import matplotlib.pyplot as plt
from spacecraft import Spacecraft


def run_sim(duration=360, dt=1.0, inject_fault_at = None):
    sc = Spacecraft()
    log = []
    t = 0.0

    while t < duration:
        if inject_fault_at is not None and abs(t - inject_fault_at) < dt:
            sc.battery_lvl -= 30 # Simulates a sudden power fault
        log.append(sc.step(t, dt))
        t += dt
    return log

def save_csv(log, path="telemtry.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log[0].keys())
        writer.writeheader()
        writer.writerows(log)

def plot(log):
    t = [row["t"] for row in log]
    bat_lvl = [row["battery_lvl"] for row in log]
    modes = [row["mode"] for row in log]

    fig, ax1 = plt.subplots()
    ax1.plot(t, bat_lvl, label = "Batter %")
    ax1.set_xlabel("Time (min)")
    ax1.set_ylabel("Battery %")

    for i in range(len(t) - 1):
        color = {"SAFE": "red", "SUN_POINTING": "yellow", "NOMINAL": "green"}[modes[i]]
        ax1.axvspan(t[i], t[i+1], color = color, alpha = 0.1)

    plt.title("Spacecraft Mode & Battery Over Time")
    plt.tight_layout()
    plt.savefig("sim_output.png")
    plt.show()

if __name__ == "__main__":
    log = run_sim(inject_fault_at=120) # adds fault at t = 120 min mark
    save_csv(log)
    plot(log)
    print(f"Simulation complete. {len(log)} steps have been logged to telemetry.csv")
