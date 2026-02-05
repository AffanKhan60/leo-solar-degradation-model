import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Solar array degradation model
# Author: Muhammad Affan Khan
# -------------------------------------------------

years = 10
time = np.arange(0, years + 1, 1)

# Initial relative power
P0 = 1.0

# Assumptions (from literature ranges):
# - UV + thermal cycling cause ~2% loss per year
base_degradation = 0.02  # 2% / year

# - Radiation damage increases with altitude
#   Values chosen to reflect stronger radiation at 700 km
radiation_degradation = {
    400: 0.01,   # ~1% / year at 400 km
    700: 0.025   # higher radiation exposure
}

plt.figure()

for altitude, rad_loss in radiation_degradation.items():
    power = np.zeros(len(time))
    power[0] = P0

    for i in range(1, len(time)):
        # Degradation applied once per year (discrete model)
        power[i] = power[i - 1] * (1 - base_degradation) * (1 - rad_loss)

    plt.plot(time, power, marker='o', label=f"{altitude} km")

plt.xlabel("Time [years]")
plt.ylabel("Relative solar array power (P / P0)")
plt.title("Solar Array Degradation in LEO")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
