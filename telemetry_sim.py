import math
import time

# Sounding Rocket Telemetry Simulation Script in Python
def simulate_flight():
    altitude = 0.0
    velocity = 0.0
    gravity = -9.81
    thrust = 55.0  # Net acceleration under motor burn

    print("[SYSTEM] AeroPulse Flight Telemetry Simulator Initialized...")
    print("Time(s) | Altitude(m) | Velocity(m/s) | Event")
    print("-" * 50)

    for t in range(0, 30):
        if t < 5:
            # Powered flight (Boost)
            velocity += thrust * 0.5
            event = "BOOST PHASE"
        elif velocity > 0:
            # Coasting to apogee
            velocity += gravity * 0.5
            event = "COASTING"
        else:
            # Apogee passed, Parachute deployment
            velocity = -12.0  # Terminal descent velocity with drogue
            event = "DROGUE PARACHUTE DEPLOYED"

        altitude = max(0.0, altitude + (velocity * 0.5))
        print(f"T+{t*0.5:04.1f}s | {altitude:08.2f}m | {velocity:06.2f}m/s | {event}")
        time.sleep(0.1)


if __name__ == "__main__":
    simulate_flight()