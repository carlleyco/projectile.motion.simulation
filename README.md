# Projectile Motion Simulator

A projectile motion simulator built in Python. This graphs the trajectory of an object under gravity and air drag, then plots it in real time with built-in sliders. There added is a no-drag trajectory for reference shown simultaneously for comparison.

This is my first project in a series of simulations relevant about aerospace to be a part of a long-term engineering porfolio.

## Features
- Simulates Projectile Motion with **air drag** using numerical integration (Euler's Method)
- Displays a **no-drag reference trajectory** for comparison
- **5 Interactive Sliders** - adjust any parameter
  - Initial speed (m/s)
  - Launch angle (deg)
  - Drag Coefficient
  - Mass (kg)
  - Cross-Section Area (m²)
- **Live Information Box** showing max altitude, range, and time of the flight
- Labeled Graphs with Grid, Legend, and Axis units

## How it Works

### Physics
**Gravity** pulls the object downward:
```
Fg = m * g
```

**Air Drag** opposes the direction of motion:
```
Fd = 0.5 * Cd * ρ * A * v²
```

Where:
- `Cd` — Drag Coefficient
- `ρ` — Air Density (1.225 kg/m³)
- `A` — Cross-Section Area of the Object
- `v` — Current Speed of the Object

The drag force is split into x and y components based on the velocity direction:
```
Fd_x = -Fd * (vx / v)
Fd_y = -Fd * (vy / v)
```

Acceleration is derived from Newton's Second Law:
```
ax = Fd_x / m
ay = -g + (Fd_y / m)
```

**Note:** The trajectory of no-drag does not use mass because in the absence of drag, mass cancels out of the equations entirely.

### Numerical Method

The simulation uses the **Euler's Method**. At each timestep (`dt = 0.01s`), velocity and position are updated:
```
vx += ax * dt
vy += ay * dt
x  += vx * dt
y  += vy * dt
```

This repeats in a loop until the object returns to ground level (`y < 0`).

### Code Structure
| Function | Purpose |
|---|---|
| `start(v0, angle, Cd, m, A)` | Runs the simulation |
| `nodrag(v0, angle)` | Computes the no-drag trajectory |
| `update_box(x_data, y_data)` | Updates the text box on the plot |
| `update(val)` | Called by every slider and reruns both simulations and redraws the graph |

---

## What I Learned
- How to model physical forces as code using Newton's Second Law
- Why mass does not affect trajectory in the absence of air resistance
- How `matplotlib.widgets.Slider` works and how to connect multiple of them in one single function
- The importance of building in stages (e.g. get it working first, then add more features)

---

## How it could be Improved
- **Runge-Kutta (RK4) Integration** instead of Euler for higher accuracy, most importantly at larger timesteps
- **Varying Air Density with Altitude** using the International Standard Atmosphere (ISA) model instead of a fixed value
- **3D Trajectory** by adding a third axis and a heading angle to simulate lateral movement
- **Multiple Trajectories** by adding several angle or speed inputs for comparison
- **Exporting Data** by saving the simulation output to a CSV file for more analysis
- **Drag Coefficient Presets** by adding a dropdown for common shapes (sphere, rocket nosecone, cylinder)

---

## How to Run

##Requirements:** Python 3.8 or newer

**Install dependencies:**
```bash
pip install numpy matplotlib
```

**Run the simulator:**
```bash
python main.py
```

Use the sliders at the bottom of the window to adjust parameters. The graph updates in real time.

---

## Project Status
This is the **Final Stage** of the program fully functional with sliders, comparison trajectories, and live statistics. Future improvements will be added listed above if there are any.

## Demo

> Demo Video will be linked here once recorded.
