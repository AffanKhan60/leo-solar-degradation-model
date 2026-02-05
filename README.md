# Solar Array Degradation Model (LEO)

This repository contains a small numerical model to estimate the degradation
of satellite solar arrays in Low Earth Orbit.

## Model idea
The available solar power is reduced once per year using:
- a constant baseline degradation term (UV exposure, thermal cycling)
- an additional radiation-related term that increases with altitude

The model computes relative power (P / P0) over the mission lifetime and
compares different LEO altitudes.

## Assumptions
- Degradation is applied in discrete yearly steps
- Radiation effects are stronger at higher altitudes
- Effects such as shielding, eclipses, and detailed dose modeling are neglected

## Tools
- NumPy for numerical calculations
- Matplotlib for plotting degradation trends

This model is intended as a first-order approximation and can be extended
using environment or telemetry data.
