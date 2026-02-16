from math import pi
import numpy as np

fc = 35_000
w0 = 2 * pi * fc
Q = .5412
#Gain is set 1

a1 = w0 / Q
a0 = w0**2

E6 = np.array([
    100e-12, 150e-12, 220e-12, 330e-12,
    470e-12, 680e-12,
    1e-9, 1.5e-9, 2.2e-9, 3.3e-9,
    4.7e-9, 6.8e-9, 10e-9
])

for C1 in E6:
    for C2 in E6:
        for C3 in E6:

            R2 = (C1 + C2 + C3) / (a1 * C2 * C3)
            R1 = 1 / (a0 * R2 * C2 * C3)

            if 1e3 < R1 < 1e6 and 1e3 < R2 < 1e6 and C1 > 470e-12 and C2 > 470e-12 and C3 > 470e-12 and (C1==C3):
              print(
                    f"C1={C1*1e12:4.0f}p "
                    f"C2={C2*1e12:4.0f}p "
                    f"C3={C3*1e12:4.0f}p | "
                    f"R1={R1:7.1f} "
                    f"R2={R2:7.1f}"
                )
