# Pvyle Vector Orbital Engine (PVOE)

Personal project: a 2D orbital mechanics simulator with real-time trajectory
calculation and a Mission Control-style UI.

## Status

🚧 Early stage. Core physics, ship selection, and UI layout are working.
Still missing: multiple celestial bodies, working navball (currently a
visual stub), and mission save/load.

## What works

- ✅ Gravity simulation (Verlet integrator)
- ✅ Ship rotation independent of velocity vector; thrust applies in facing direction
- ✅ Real-time orbital elements: apoapsis, periapsis, eccentricity
- ✅ Orbit ellipse rendering, recalculated live from position/velocity
- ✅ Mission Control-style UI: grid layout with telemetry, resources, trajectory panels
- ✅ Time warp (x1 to x10000)
- ✅ Real-world scale (~1:10 Earth), realistic orbital velocities (km/s)
- ✅ Fuel consumption and ship mass (thrust scales with current mass as fuel depletes)
- ✅ 5 selectable ship presets with different mass/thrust/fuel characteristics
- ✅ TWR calculation based on local gravity

## Roadmap

- ⬜ Working navball (currently a visual placeholder)
- ⬜ Multiple celestial bodies / sphere of influence transitions
- ⬜ Custom star system config
- ⬜ Assignments and missions
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
- `1`-`5` — switch ship

## Why this project

Exploring Python/OOP and orbital mechanics fundamentals (state vectors →
orbital elements, numerical integration under gravity, coordinate systems)
by building something concrete. Will keep expanding as it progresses.
