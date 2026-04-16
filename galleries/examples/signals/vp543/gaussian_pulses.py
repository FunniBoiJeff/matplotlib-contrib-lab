"""
================================
Gaussian Pulse Width Variation
================================

This example demonstrates how the standard deviation (sigma) affects the 
width and spread of a Gaussian signal. It is a fundamental concept for 
engineers working with windowing functions or signal dispersion.
"""

import matplotlib.pyplot as plt
import numpy as np

# Intent: Generate a time axis and define a range of sigma values to compare.
t = np.linspace(-5, 5, 500)
sigmas = [0.5, 1.0, 1.5, 2.0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Intent: Initialize the plot using the object-oriented subplots interface.
fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')

# Intent: Loop through each sigma, calculate the Gaussian curve, and plot it.
for s, color in zip(sigmas, colors):
    # Gaussian formula: y = exp(-t^2 / (2*sigma^2))
    y = np.exp(-t**2 / (2 * s**2))
    ax.plot(t, y, lw=2, label=rf'$\sigma = {s}$', color=color)
    ax.fill_between(t, y, alpha=0.1, color=color)

# Intent: Add professional styling including LaTeX labels and a grid.
ax.set_title('Gaussian Pulse Width Comparison', fontsize=14)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Normalized Amplitude')
ax.legend(title='Pulse Width')
ax.grid(True, linestyle='--', alpha=0.6)

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules
#    is shown in this example:
#
#    - `matplotlib.axes.Axes.plot`
#    - `matplotlib.axes.Axes.fill_between`
#    - `matplotlib.axes.Axes.set`
#    - `matplotlib.pyplot.subplots`
#
# .. tags::
#
#    plot-type: line
#    level: beginner