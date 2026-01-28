# 10. growth_rate_scale_dependent.py
import numpy as np
import matplotlib.pyplot as plt

# Generate scale-dependent growth rate for different redshifts
k = np.logspace(-2, 0, 200)  # h/Mpc

# Growth rate f(k,z) for Omega model
def f_omega(k, z):
    k0 = 0.03  # Transition scale
    n = 1.2    # Redshift dependence
    f0 = 0.5 * (1 + z)**(-0.6)  # Scale-independent part
    scale_dep = 1 - 0.18/(1 + (k/k0)**(-n*(1+z)**0.3))
    return f0 * scale_dep

# LCDM growth rate (scale-independent)
def f_lcdm(z):
    return 0.5 * (1 + z)**(-0.6)

# Plot for multiple redshifts
plt.figure(figsize=(14, 9))
redshifts = [0.0, 0.5, 1.0, 2.0]
colors = ['red', 'orange', 'green', 'blue']

for z, color in zip(redshifts, colors):
    f_omega_k = f_omega(k, z)
    f_lcdm_const = f_lcdm(z) * np.ones_like(k)
    
    plt.plot(k, f_omega_k, '-', color=color, linewidth=2.5, 
             label=rf'$\Omega$-Field, $z={z}$')
    plt.plot(k, f_lcdm_const, '--', color=color, linewidth=1.5, alpha=0.7, 
             label=rf'$\Lambda$CDM, $z={z}$')

plt.xscale('log')
plt.xlabel(r'$k$ [$h$ Mpc$^{-1}$]', fontsize=16)
plt.ylabel(r'Growth Rate $f(k, z)$', fontsize=16)
plt.title('Scale-Dependent Growth Rate in $\Omega$-Field Model', fontsize=18)

# Add secondary x-axis with physical scale
ax = plt.gca()
ax2 = ax.twiny()
k_vals = np.array([0.01, 0.03, 0.1, 0.3])
lambda_vals = 2*np.pi/k_vals
ax2.set_xscale('log')
ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(k_vals)
ax2.set_xticklabels([f'{l:.0f}' for l in lambda_vals])
ax2.set_xlabel(r'Physical Scale $\lambda = 2\pi/k$ [Mpc $h^{-1}$]', fontsize=14)

plt.legend(fontsize=12, loc='lower left', ncol=2)
plt.grid(True, alpha=0.3, which='both')
plt.xlim(1e-2, 0.3)
plt.ylim(0.3, 1.0)
plt.tight_layout()
plt.savefig('growth_rate_scale_dependent.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated growth_rate_scale_dependent.pdf")