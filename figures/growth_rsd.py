# 4. growth_rsd.py
import numpy as np
import matplotlib.pyplot as plt

# Generate scale-dependent growth rate at z=0.5
k = np.logspace(-2, 0, 100)  # h/Mpc
# LCDM growth rate (scale-independent)
f_lcdm = 0.78 * np.ones_like(k)
# Omega field growth rate (scale-dependent)
f_omega = 0.78 * (1 - 0.12/(1 + (k/0.03)**(-1.5)))
# fσ8 observable
sigma8_lcdm = 0.82
sigma8_omega = 0.76
fsigma8_lcdm = f_lcdm * sigma8_lcdm
fsigma8_omega = f_omega * sigma8_omega
# DESI forecast errors
sigma = 0.03 * np.ones_like(k)

plt.figure(figsize=(12, 8))
plt.plot(k, fsigma8_lcdm, '--', color='blue', linewidth=2.5, 
         label=r'$\Lambda$CDM', alpha=0.8)
plt.plot(k, fsigma8_omega, '-', color='red', linewidth=3, 
         label=r'$\Omega$-Field')
plt.fill_between(k, fsigma8_omega - sigma, fsigma8_omega + sigma, 
                 alpha=0.2, color='red', label='DESI forecast 1$\sigma$')

plt.xscale('log')
plt.xlabel(r'$k$ [$h$ Mpc$^{-1}$]', fontsize=16)
plt.ylabel(r'$f\sigma_8(k)$ at $z=0.5$', fontsize=16)
plt.title('Scale-dependent Growth from RSD', fontsize=18)
plt.legend(fontsize=14, loc='upper right')
plt.grid(True, alpha=0.3, which='both')
plt.xlim(1e-2, 0.3)
plt.ylim(0.5, 0.9)
plt.tight_layout()
plt.savefig('growth_rsd.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated growth_rsd.pdf")