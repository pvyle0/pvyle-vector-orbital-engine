# Pvyle Vector Orbital Engine (PVOE)

Personal project: a 2D orbital mechanics simulator with real-time trajectory
calculation and a Mission Control

## Status

🚧 Very early stage. This is currently more of a physics prototype than a
finished simulator — a lot is still missing or not working as intended.

## What works

- Gravity simulation (Verlet integrator)
- Thrust control (throttle)
- Real-time orbital elements: apoapsis, periapsis, eccentricity

## Roadmap

- Orbit rendering (ellipse) on screen
- Telemetry UI panel (velocity, altitude, apoapsis/periapsis)
- Fuel and ship mass
- Navball (orientation indicator)
- Multiple celestial bodies

## Getting started

```bash
pip install -r requirements.txt
python main.py
```

## Controls

- `Z` — full throttle
- `X` — cut throttle
- `Left Shift` — increase throttle
- `Left Ctrl` — decrease throttle

## Why this project

Exploring Python/OOP and orbital mechanics fundamentals (state vectors →
orbital elements, numerical integration under gravity) by building something
concrete. Will keep expanding as it progresses.
