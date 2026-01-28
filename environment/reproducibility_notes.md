# Reproducibility Notes

This repository accompanies the paper  
**“Omega Gravity: A Conserved Vacuum Charge Unifying Dark Matter and Dark Energy.”**

The purpose of the numerical material provided here is to enable transparent,
independent reproduction of all figures and qualitative results presented in
the manuscript.

---

## Software Environment

All Python-based figures were generated using:

- Python ≥ 3.9
- NumPy
- SciPy
- Matplotlib

Exact package versions are not critical for reproducing the results, as all
figures rely on analytic expressions and numerically stable operations.

---

## Boltzmann Solvers

Modified versions of the CLASS and CAMB Boltzmann solvers are provided as
**reference implementations** of the Omega-field background and perturbation
equations.

These implementations are intended to:

- Demonstrate how the Omega-field equations enter standard cosmological solvers
- Verify reduction to ΛCDM in the appropriate limits
- Cross-check perturbative stability and clustering behavior

They are **not** intended as optimized production codes.

---

## Floating-Point Differences

Minor numerical differences may occur across systems due to compiler options
and floating-point rounding. These do not affect any qualitative conclusions
or physical interpretations.

---

## Contact

If any difficulty is encountered in reproducing results, the author can be
contacted for clarification or additional details.
