import numpy as np
import matplotlib.pyplot as plt

# Values
g = 9.80665     # gravity
dt = 0.01       # time (s)
v0 = 50         # initial speed
angle = 45      # launch angle

m = 1.0         # mass (kg)
Cd = 0.47       # drag coefficient
rho = 1.225     # air density
A = 0.01        # area of the cross section

# Starting Conditions
angle2rad = np.radians(angle)
vx = v0 * np.cos(angle2rad)
vy = v0 * np.sin(angle2rad)

x = 0.0
y = 0.0

x_list = [x]
y_list = [y]

# Simulate
while y >= 0:
    v = np.sqrt(vx**2 + vy**2) # get current speed

    Fd = 0.5 * Cd *rho * A * v**2 # add drag

    # negate velocity
    if v > 0:
        Fd_x = -Fd * (vx/v)
        Fd_y = -Fd * (vy/v)
    else:
        Fd_x, Fd_y = 0,0

    ax = Fd_x / m
    ay = -g + (Fd_y/m)

    vx += ax * dt
    vy += ay * dt
    
    x += vx * dt
    y += vy * dt

    x_list.append(x)
    y_list.append(y)

# --- Plot ---
plt.figure(figsize=(10, 5))
plt.plot(x_list, y_list, color='royalblue')
plt.title(f'Projectile Motion Simulator | v0={v0} m/s, angle={angle}°')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.axis('equal')
plt.show()
