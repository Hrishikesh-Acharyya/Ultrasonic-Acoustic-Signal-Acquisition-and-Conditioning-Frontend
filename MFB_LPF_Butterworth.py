from math import pi, sqrt
import numpy as np

fc = 58_000
w0 = 2 * pi * fc
Q = 0.5412
#Gain is set to -1, so R1 must equal R3
E6 = np.array([
    100e-12, 150e-12, 220e-12, 330e-12,
    470e-12, 680e-12,
    1e-9, 1.5e-9, 2.2e-9, 3.3e-9,
    4.7e-9, 6.8e-9, 10e-9
])


for C1 in E6:
    for C2 in E6:
        
        if C1 < 8 * (Q**2) * C2:  #Prevents imaginary solutions for R1
            continue

        # Quadratic equation coefficients derived for R1 from the Q factor and w0 and gain conditions
        a = (w0**2) * C1 * C2
        b = -(w0 * C1) / Q
        c = 2

        discriminant = b**2 - 4*a*c
        
        if discriminant >= 0:
            
            R1_val1 = (-b + sqrt(discriminant)) / (2 * a)
            R1_val2 = (-b - sqrt(discriminant)) / (2 * a)
            
    
            for R1 in [R1_val1, R1_val2]:
                R3 = R1 # R1 must equal R3 for a gain of -1
                R2 = 1 / ((w0**2) * R1 * C1 * C2)
                
                # Check for practical resistor ranges and minimum cap values
                if 1e3 < R1 < 1e6 and 1e3 < R2 < 1e6 and C1 > 220e-12 and C2 > 220e-12:
                    print(
                        f"C1={C1*1e12:4.0f}p  "
                        f"C2={C2*1e12:4.0f}p | "
                        f"R1={R1:7.1f}  "
                        f"R2={R2:7.1f}  "
                        f"R3={R3:7.1f}"
                    )