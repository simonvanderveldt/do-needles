#!/usr/bin/env python
""" Interactively plot Dell'Orto D needles to easily compare them """
import math

import matplotlib.pyplot as plt
import mplcursors

TOTAL_LENGTH = 52

# TODO Missing needles with multiple tapers (D42, D43, D45, D58, D59, D60)
NEEDLES = {
    "D01": {
        "d_a": 2.45,
        "d_b": 1.50,
        "c": 15.4
    },
    "D03": {
        "d_a": 2.42,
        "d_b": 1.50,
        "c": 14
    },
    "D21": {
        "d_a": 2.50,
        "d_b": 1.80,
        "c": 20.2
    },
    "D22": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 18
    },
    "D23": {
        "d_a": 2.46,
        "d_b": 1.00,
        "c": 22
    },
    "D24": {
        "d_a": 2.50,
        "d_b": 0.60,
        "c": 20
    },
    "D25": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 16
    },
    "D26": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 20
    },
    "D27": {
        "d_a": 2.50,
        "d_b": 1.80,
        "c": 16
    },
    "D28": {
        "d_a": 2.50,
        "d_b": 1.80,
        "c": 18
    },
    "D29": {
        "d_a": 2.50,
        "d_b": 1.80,
        "c": 20
    },
    "D30": {
        "d_a": 2.50,
        "d_b": 0.60,
        "c": 18
    },
    "D31": {
        "d_a": 2.50,
        "d_b": 0.60,
        "c": 22
    },
    "D32": {
        "d_a": 2.50,
        "d_b": 1.00,
        "c": 18
    },
    "D33": {
        "d_a": 2.50,
        "d_b": 1.00,
        "c": 20
    },
    "D34": {
        "d_a": 2.50,
        "d_b": 1.00,
        "c": 22
    },
    "D35": {
        "d_a": 2.46,
        "d_b": 1.40,
        "c": 18
    },
    "D36": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 22
    },
    "D37": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 24
    },
    "D38": {
        "d_a": 2.50,
        "d_b": 1.00,
        "c": 26
    },
    "D39": {
        "d_a": 2.50,
        "d_b": 0.95,
        "c": 25
    },
    "D40": {
        "d_a": 2.48,
        "d_b": 1.00,
        "c": 24
    },
    "D41": {
        "d_a": 2.52,
        "d_b": 1.00,
        "c": 24.5
    },
    "D44": {
        "d_a": 2.48,
        "d_b": 1.60,
        "c": 24
    },
    "D46": {
        "d_a": 2.50,
        "d_b": 1.00,
        "c": 24
    },
    "D47": {
        "d_a": 2.52,
        "d_b": 1.40,
        "c": 26
    },
    "D48": {
        "d_a": 2.50,
        "d_b": 0.80,
        "c": 28
    },
    "D49": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 26
    },
    "D50": {
        "d_a": 2.50,
        "d_b": 0.80,
        "c": 30
    },
    "D51": {
        "d_a": 2.50,
        "d_b": 1.40,
        "c": 28
    },
    "D52": {
        "d_a": 2.50,
        "d_b": 1.00,
        "c": 26
    },
    "D53": {
        "d_a": 2.52,
        "d_b": 1.00,
        "c": 28
    },
    "D54": {
        "d_a": 2.48,
        "d_b": 1.40,
        "c": 25
    },
    "D55": {
        "d_a": 2.48,
        "d_b": 1.80,
        "c": 25
    },
    "D56": {
        "d_a": 2.48,
        "d_b": 1.80,
        "c": 22
    },
    "D57": {
        "d_a": 2.52,
        "d_b": 0.80,
        "c": 28
    },
}

def get_points(d_a, d_b, c):
    r_a = d_a / 2
    r_b = d_b / 2
    straigth_length = TOTAL_LENGTH - c
    taper_max_height = r_a - r_b
    taper_angle = math.atan(taper_max_height / c)

    buckets = range(TOTAL_LENGTH + 1)

    points = []
    for bucket in buckets:
        if bucket <= (straigth_length):
            points.append([bucket, d_a])
        else:
            taper_radius = math.tan(taper_angle) * (c - (bucket - straigth_length))
            taper_diameter = 2 * (r_b + taper_radius)
            points.append([bucket, taper_diameter])

    # taper_midpoint = TOTAL_LENGTH - (c / 2)
    # taper_midpoint_radius = math.tan(taper_angle) * (c / 2)
    # taper_midpoint_diameter = 2 * (r_b + taper_midpoint_radius)
    # print(f"{taper_midpoint}: {taper_midpoint_diameter}")

    return points

def plot_points(axis, needle_name):
    points = get_points(**NEEDLES[needle_name])
    x, y = zip(*points)
    line = axis.plot(x, y, label=needle_name, marker="o", linestyle="none")[0]
    return line

fig, ax = plt.subplots()

lines = []
for needle in NEEDLES:
    lines.append(plot_points(ax, needle))

leg = ax.legend(loc="upper left")

lined = {} # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True) # Enable picking on the legend line.
    legline.set_pickradius(10)
    lined[legline] = origline

def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the marker face color in the legend so we can see which lines have been toggled.
    if visible:
        legline._legmarker.set_markerfacecolor(legline._legmarker.get_markeredgecolor())
    else:
        legline._legmarker.set_markerfacecolor("white")
    fig.canvas.draw()

fig.canvas.mpl_connect("pick_event", on_pick)
mplcursors.cursor(hover=2)
plt.show()
