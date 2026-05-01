import numpy as np
import matplotlib.pyplot as plt

# Values
g = 9.80665     # gravity
dt = 0.01       # time (s)
v0 = 50         # initial speed
angle = 45      # launch angle

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
    ax = 0
    ay = -g

    vx += ax * dt
    vy += ay * dt
    
    x += vx * dt
    y += vy * dt

    x_list.append(x)
    y_list.append(y)

# --- Plot ---
plt.figure(figsize=(10, 5))
plt.plot(x_list, y_list, color='royalblue')
plt.title(f'Projectile Motion with No Drag Resistance | v0={v0} m/s, angle={angle}°')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.axis('equal')
plt.show()