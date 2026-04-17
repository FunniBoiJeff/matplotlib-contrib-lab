"""
=====================================
Gaussian Pulse Widths
=====================================

Demonstrate how the temporal width of a Gaussian pulse affects its shape.
This example plots several Gaussian pulses with different standard deviations
(σ) on the same time axis and highlights the area under one pulse.
"""

import numpy as np
import matplotlib.pyplot as plt

# time base
t = np.linspace(-2.0, 2.0, 1000)
# pulse centers and widths to compare
sigmas = [0.05, 0.2, 0.5]
amplitude = 1.0

fig, ax = plt.subplots(figsize=(8, 4))
for sigma in sigmas:
    pulse = amplitude * np.exp(-0.5 * (t / sigma) ** 2)
    ax.plot(t, pulse, label=f"σ={sigma}")

# highlight the widest pulse area
sigma_highlight = sigmas[-1]
pulse_h = amplitude * np.exp(-0.5 * (t / sigma_highlight) ** 2)
ax.fill_between(t, 0, pulse_h, alpha=0.12, color="C2")

ax.set(xlabel='Time (s)', ylabel='Amplitude',
       title=r'Gaussian pulses: $A\,e^{-t^{2}/(2\sigma^{2})}$ (varying $\sigma$)')
ax.legend(loc='upper right')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

#############################################################################
#
# .. admonition:: References
#
#    The use of the following functions, methods and classes is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.plot`
#    - `matplotlib.axes.Axes.fill_between`
#    - `matplotlib.axes.Axes.set`
#    - `matplotlib.pyplot.subplots`

# %%
# .. tags::
#    plot-type: line
#    level: beginner
