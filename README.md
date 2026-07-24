# Flight Software Mode Simulator

Minimal and simple simulation of a spacecraft switching it's flight mode based on battery and whether or not there is an eclipse.

## What it models
- Simplified orbit with periodic light/eclipse phases
- Battery charge and drain (charge in sunlight, drain in eclipse)
- Transitions between 3 modes: SAFE, SUN_POINTING, and NOMINAL
    - When the spacecraft is in danger, it will enter SAFE mode
    - When the spacecraft is pointing at the sun it is in SUN_POINTING mode
    - When the spacecraft is operating normally, it is in NOMINAL mode

## How to run

Use command:

    pip install -r requirements.txt
    python sim.py

