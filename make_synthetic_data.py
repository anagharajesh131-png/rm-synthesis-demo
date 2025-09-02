import numpy as np

# Frequency range: 700 MHz to 1800 MHz, step 10 MHz
freqs = np.arange(700e6, 1800e6 + 1, 10e6)

# Assume Stokes I = 1 Jy constant
I = np.ones_like(freqs)

# Create synthetic polarized signal with a rotation measure (RM)
RM = 50.0  # rad/m^2
lambda2 = (3e8 / freqs) ** 2
chi = RM * lambda2  # polarization angle

Q = np.cos(2 * chi) * 0.1  # 10% fractional polarization
U = np.sin(2 * chi) * 0.1

# Assume small constant errors
errI = np.full_like(freqs, 0.01)
errQ = np.full_like(freqs, 0.01)
errU = np.full_like(freqs, 0.01)

# Save to file (7 columns: freq, I, Q, U, errI, errQ, errU)
data = np.column_stack([freqs, I, Q, U, errI, errQ, errU])
np.savetxt("C:/Users/anagha rajesh/Desktop/RMtoolsTest/synthetic_data.txt", data, fmt="%.6e")

print("Synthetic data file created: synthetic_data.txt")
