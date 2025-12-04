
import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_grid(grid):
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    conv = scipy.signal.convolve2d(grid, kernel, mode='same')
    birth = (conv == 3) & ~grid
    survive = ((conv == 2) | (conv == 3)) & grid
    grid = birth | survive
    return grid

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    lights = np.array([list(line.strip()) for line in f.readlines()])

grid = lights == '#'
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xticks([])
ax.set_yticks([])
im = ax.imshow(grid, vmin=0, vmax=1, interpolation='nearest', animated=True)
frame_text = ax.text(
    2, 5, "", color="white", fontsize=12,
    bbox=dict(facecolor="black", alpha=0.6, pad=3)
)
def animate(frame_num):
    global grid
    grid = update_grid(grid)
    im.set_data(grid)
    frame_text.set_text(f"Frame: {frame_num}")
    return im, frame_text

interval_ms = 80
anim = animation.FuncAnimation(
    fig, animate, frames=100, interval=interval_ms, blit=True
    )
try:
    writer = animation.PillowWriter(fps=1000/interval_ms)
    anim.save(__file__.rsplit("/", 1)[0] + "/18.1.gif", writer=writer)
except Exception as e:
    print('Failed to save animation:', e)
