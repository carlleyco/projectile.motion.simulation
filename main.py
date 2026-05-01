import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def start(v0, angle, Cd, m, A):
    # Values
    g = 9.80665     # gravity
    dt = 0.01       # time (s)  
    rho = 1.225     # air density

    # Starting Conditions
    angle2rad = np.radians(angle)
    vx = v0 * np.cos(angle2rad)
    vy = v0 * np.sin(angle2rad)

    x = 0.0
    y = 0.0

    x_list, y_list = [x], [y]

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

        ax_val = Fd_x / m
        ay_val = -g + (Fd_y/m)

        vx += ax_val * dt
        vy += ay_val * dt
        
        x += vx * dt
        y += vy * dt

        x_list.append(x)
        y_list.append(y)
    
    return np.array(x_list), np.array(y_list)

def nodrag(v0, angle):
    g = 9.80665
    angle2rad = np.radians(angle)
    vx = v0 * np.cos(angle2rad)
    vy = v0 * np.sin(angle2rad)
    t_flight = 2 * vy / g
    t = np.linspace(0,t_flight, 500)
    x = vx * t
    y = vy * t - 0.5 * g * t**2

    return x, np.maximum(y,0)


# Starting Values
INIT = dict(v0=50, angle=45, Cd=0.47, m=1.0, A=0.01)

# Graph
fig, ax = plt.subplots(figsize=(11,6))
plt.subplots_adjust(left=0.1, right=0.98, top=0.93, bottom=0.42)

x_data, y_data = start(INIT['v0'], INIT['angle'], INIT['Cd'], INIT['m'], INIT['A'])
x_nodrag, y_nodrag = nodrag(INIT['v0'], INIT['angle'])

line, = ax.plot(x_data, y_data, color='royalblue', lw=2, label='With Drag')
line_nodrag, = ax.plot(x_nodrag, y_nodrag, color='tomato', lw=1.5, label='No Drag', linestyle='--')
ax.legend(loc='upper right')

ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Projectile Motion Simulator')
ax.grid(True)

# Add Information Box
box_text = ax.text(
    0.02, 0.97, '', transform=ax.transAxes,
    verticalalignment='top', fontsize=10,
    bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.8)
)

def update_box(x_data, y_data):
    max_alt = max(y_data)
    range = x_data[-1]
    tof = (len(x_data)-1) * 0.01
    box_text.set_text(
        f'Max Altitude  : {max_alt:.1f} m\n'
        f'Range         : {range:.1f} m\n'
        f'Time of Flight: {tof:.2f} s'
    )

update_box(x_data,y_data)

# Sliders
sliders_stats = [
    ('v0', 'Initial Speed (m/s)', 10, 200),
    ('angle', 'Launch Angle (deg)', 1, 90),
    ('Cd', 'Drag Coefficient', 0.0, 1.0),
    ('m', 'Mass (kg)', 0.1, 10.0),
    ('A', 'Cross Section Area (m²)', 0.001, 0.1)
]

sliders = {}
for i, (key, label, vmin, vmax) in enumerate(sliders_stats):
    slider_ax = fig.add_axes([0.18, 0.30 - i * 0.055, 0.72, 0.025])
    sliders[key] = Slider(slider_ax, label, vmin, vmax, valinit=INIT[key])

def update(val):
    x_data, y_data = start(
        sliders['v0'].val, sliders['angle'].val, sliders['Cd'].val, 
        sliders['m'].val, sliders['A'].val
    )

    x_nodrag, y_nodrag = nodrag(sliders['v0'].val, sliders['angle'].val)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    line_nodrag.set_xdata(x_nodrag)
    line_nodrag.set_ydata(y_nodrag)

    ax.relim()
    ax.autoscale_view()
    ax.set_ylim(bottom=0)
    update_box(x_data,y_data)
    fig.canvas.draw_idle()

for s in sliders.values():
    s.on_changed(update)

plt.show()
