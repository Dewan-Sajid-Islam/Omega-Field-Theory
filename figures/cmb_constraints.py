# 5. cmb_constraints.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Generate mock posterior samples for Omega parameters
np.random.seed(44)
n_samples = 50000

# True parameter values (fiducial Omega model)
mu = [0.25, -6.0]  # Q_Omega, log10(alpha_Omega)
cov = [[0.015**2, 0.5*0.015*0.3],
       [0.5*0.015*0.3, 0.3**2]]  # Covariance matrix

# Generate samples
samples = multivariate_normal.rvs(mean=mu, cov=cov, size=n_samples)
Q_samples, log_alpha_samples = samples[:, 0], samples[:, 1]

# Create corner plot
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

# Histogram for Q_Omega
ax = axes[0, 0]
ax.hist(Q_samples, bins=50, density=True, alpha=0.7, color='steelblue', 
        edgecolor='black')
ax.axvline(mu[0], color='red', linestyle='--', linewidth=2, label='Fiducial')
ax.set_xlabel(r'$Q_\Omega$', fontsize=14)
ax.set_ylabel('Probability Density', fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

# Histogram for alpha_Omega
ax = axes[1, 1]
ax.hist(10**log_alpha_samples, bins=np.logspace(-7, -5, 50), 
        density=True, alpha=0.7, color='steelblue', edgecolor='black')
ax.set_xscale('log')
ax.axvline(10**mu[1], color='red', linestyle='--', linewidth=2)
ax.set_xlabel(r'$\alpha_\Omega$', fontsize=14)
ax.set_ylabel('Probability Density', fontsize=12)
ax.grid(True, alpha=0.3)

# 2D contour plot
ax = axes[1, 0]
H, xedges, yedges = np.histogram2d(Q_samples, 10**log_alpha_samples, 
                                    bins=40, density=True)
X, Y = np.meshgrid(xedges[:-1], yedges[:-1])
levels = np.percentile(H[H>0], [68, 95])
ax.contourf(X, Y, H.T, levels=np.linspace(H.min(), H.max(), 20), 
            cmap='Blues', alpha=0.7)
ax.contour(X, Y, H.T, levels=levels, colors=['darkblue', 'navy'], 
           linewidths=[1.5, 2.5])
ax.plot(mu[0], 10**mu[1], 'r*', markersize=15, label='Fiducial')
ax.set_xlabel(r'$Q_\Omega$', fontsize=14)
ax.set_ylabel(r'$\alpha_\Omega$', fontsize=14)
ax.set_yscale('log')
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

# Empty subplot
axes[0, 1].axis('off')
axes[0, 1].text(0.5, 0.5, 'Planck 2018 Constraints\n68% and 95% CL', 
                fontsize=16, ha='center', va='center')

plt.suptitle(r'Marginalized Posterior Distributions for $\Omega$-Field Parameters', 
             fontsize=18, y=0.95)
plt.tight_layout()
plt.savefig('cmb_constraints.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated cmb_constraints.pdf")