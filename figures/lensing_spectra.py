# 3. lensing_spectra.py
import numpy as np
import matplotlib.pyplot as plt

# Generate realistic weak lensing convergence power spectra
ell = np.logspace(1, 4, 200)
# LCDM lensing power spectrum
C_lcdm = 1e-7 * (ell/100)**(-1.2) * np.exp(-ell/5000)
# Omega field lensing power spectrum (with scale-dependent suppression)
C_omega = C_lcdm * (1 - 0.15/(1 + (ell/800)**2.5))
# Forecast errors (Euclid-like)
sigma = 0.1 * C_lcdm * np.sqrt(1 + ell/1000)

plt.figure(figsize=(12, 8))
plt.loglog(ell, C_lcdm, '--', color='blue', linewidth=2.5, 
           label=r'$\Lambda$CDM', alpha=0.8)
plt.loglog(ell, C_omega, '-', color='red', linewidth=3, 
           label=r'$\Omega$-Field')
plt.fill_between(ell, C_omega - 2*sigma, C_omega + 2*sigma, 
                 alpha=0.2, color='red', label='Euclid forecast 2$\sigma$')

plt.xlabel(r'Multipole $\ell$', fontsize=16)
plt.ylabel(r'$C_\ell^{\kappa\kappa}$', fontsize=16)
plt.title('Weak Lensing Convergence Power Spectrum', fontsize=18)
plt.legend(fontsize=14, loc='upper right')
plt.grid(True, alpha=0.3, which='both')
plt.xlim(10, 10000)
plt.ylim(1e-10, 1e-6)
plt.tight_layout()
plt.savefig('lensing_spectra.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated lensing_spectra.pdf")