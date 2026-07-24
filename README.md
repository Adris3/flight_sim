# Flight Software Mode Simulator

Minimal and simple simulation of a spacecraft switching it's flight mode based on battery and whether or not there is an eclipse.

## What it models
- Simplified orbit with periodic light/eclipse phases
- Battery charge and drain (charge in sunlight, drain in eclipse)
- Transitions between 3 modes: SAFE, SUN_POINTING, and NOMINAL
    - When the spacecraft is in danger, it will enter SAFE mode
    - When the spacecraft is charging it is in SUN_POINTING mode
    - When the spacecraft is operating normally, it is in NOMINAL mode

## Design Decisions
- **Eclipse model**: the eclipse is treated as a fixed, regular occurance at the start of each orbit, this produces a realistic repeating power cycle 
- **Mode transitions are threshold based**: this is not ideal in a real world system, as sitting near a threshold could cause rapid switching between two states
    - The next step for this would be to make it so that the condition to exit SAFE mode would be set to 5 % higher than the condition to enter SAFE mode (enter SAFE at 20%, exit SAFE mode at 25%)
- **Battery charge/discharge is linear**: this simplification was made to keep the focus on state machine changes


## File structure
    flight-sim/
    ├── README.md
    ├── sim.py              # simulation loop, telemetry logging, plotting
    ├── spacecraft.py        # state machine + power/environment model
    ├── test.py    # unit tests for state machine behavior
    └── requirements.txt

## How to run

Use command:

    pip install -r requirements.txt
    python sim.py

Outputs:

telemetry.csv - logged state and mode at each timestamp
sim_output.png - batter & mode over time plotted on a line graph, each mode has its own shading

## Test

    pytest test.py -v

## Next Steps and Known Limitations
- Add hysteresis to the mode transitions 
- Replace the fixed eclipse model to one that simulates true orbital geometry
- Model additional subsystems such as thermal and comms
- Add configurable orbit patterns via CLI instead of simply hard coding them