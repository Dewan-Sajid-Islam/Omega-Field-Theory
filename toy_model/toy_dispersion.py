#!/usr/bin/env python3
# toy_dispersion.py  (Pydroid-safe, matplotlib>=3.8)

import matplotlib
matplotlib.use("Agg")  # Non-GUI backend for phones

import numpy as np
import matplotlib.pyplot as plt

# --- Fiducial parameters (reduced Planck units) ---
phi0 = 0.5
f1 = 1e-2
a = 1.0
# -------------------------------------------------

# Effective mass squared
m_eff2 = 12.0 * f1 * phi0**2

# k range (log-spaced)
k = np.logspace(-4, 2, 800)
k2_a2 = k**2 / a**2

# Effective sound speed squared
cs2 = k2_a2 / (k2_a2 + m_eff2)

# Plot
plt.figure(figsize=(6.4, 4.2))
plt.loglog(k, cs2)  # <-- FIXED
plt.axhline(1e-3, linestyle='--', linewidth=0.8)
plt.fill_between(
    k, cs2, 1e-3,
    where=(cs2 <= 1e-3),
    alpha=0.2,
    label=r'$c_{s,\Omega}^2 \leq 10^{-3}$'
)
plt.xlabel(r'Comoving wavenumber $k$')
plt.ylabel(r'Effective sound speed $c_{s,\Omega}^2(k)$')
plt.title(r'$\Omega$-field toy-model sound speed')
plt.legend(frameon=False)
plt.grid(True, which='both', ls='--', alpha=0.35)
plt.tight_layout()

plt.savefig("cs2_omega.pdf", dpi=300)
plt.close()

print("SUCCESS: cs2_omega.pdf generated")
print(f"m_eff^2 = {m_eff2:.3e}")