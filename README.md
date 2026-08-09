# Pvyle Vector Orbital Engine (PVOE)

Personal project: a 2D orbital mechanics simulator with real-time trajectory
calculation and a Mission Control-style UI.

## Status

🚧 Early stage. Core physics and UI layout are working, but many features
are still missing or placeholder (fuel, mass, multiple bodies, navball is
just a visual stub for now).

## What works

- ✅ Gravity simulation (Verlet integrator)
- ✅ Ship rotation independent of velocity vector; thrust applies in facing direction
- ✅ Real-time orbital elements: apoapsis, periapsis, eccentricity
- ✅ Orbit ellipse rendering, recalculated live from position/velocity
- ✅ Mission Control-style UI: grid layout with telemetry, resources, trajectory panels
- ✅ Time warp (x1 to x10000)
- ✅ Real-world scale (~1:10 Earth), realistic orbital velocities (km/s)

## Roadmap

- ⬜ Fuel consumption and ship mass (Tsiolkovsky rocket equation)
- ⬜ Working navball (currently a visual placeholder)
- ⬜ Multiple celestial bodies / sphere of influence transitions
- ⬜ Custom star system config
- ⬜ Several ship presets with different mass/thrust/fuel capacity
- ⬜ Mission save/load

## Getting started

```bash
pip install -r requirements.txt
python main.py
```

## Controls

- `Z` — full throttle
- `X` — cut throttle
- `Left Shift` / `Left Ctrl` — adjust throttle
- `Left` / `Right` — rotate ship
- `,` / `.` — decrease/increase time warp

## Why this project

Exploring Python/OOP and orbital mechanics fundamentals (state vectors →
orbital elements, numerical integration under gravity, coordinate systems)
by building something concrete. Will keep expanding as it progresses.
