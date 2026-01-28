# Omega-Field-Theory
Reference implementations and numerical codes for Omega Gravity: a conserved vacuum-charge field theory unifying dark matter and dark energy, including Boltzmann-solver modifications and reproducible figure scripts.


This repository contains the numerical codes and reference implementations associated with the paper

**“Omega Gravity: A Conserved Vacuum Charge Unifying Dark Matter and Dark Energy”**  
Dewan Sajid Islam

The code base provides all scripts required to reproduce the figures presented in the manuscript, as well as additional reference implementations illustrating the theoretical reduction, stability, and perturbative behavior of the Omega-charge field.

---

## Scientific Context

The Omega-field theory introduces an exactly conserved vacuum charge arising from a shift-gauge symmetry in a covariant field-theoretic framework. The theory naturally gives rise to both dark matter–like clustering and dark energy–like cosmic acceleration as different dynamical regimes of a single sector.

A controlled reduction to standard ΛCDM cosmology is recovered in the weak-coupling and long-wavelength limits, while novel, testable deviations appear at intermediate scales.

---

## Repository Overview

This repository enables:

- Reproduction of all figures appearing in the manuscript
- Verification of the toy-model dispersion relation and clustering regime
- Independent validation of linear perturbations using modified Boltzmann solvers

The repository is organized to maintain a clear correspondence between the manuscript and the numerical implementations.

---

## Directory Structure

- `figures/`  
  Python scripts used to generate each figure appearing in the manuscript.  
  Scripts are named to correspond directly to figure numbers.

- `toy_model/`  
  A fully worked 0+1D homogeneous truncation and linear perturbation toy model, including an exact dispersion relation and effective sound-speed calculation.

- `class_omega/`  
  Modifications to the CLASS Boltzmann solver implementing the Omega-field background and perturbation equations.

- `camb_omega/`  
  Independent CAMB-based equations and parameter files used for cross-validation.

- `environment/`  
  Python dependency information and reproducibility notes.

---

## Reproducing Results

All figure scripts are standalone and can be executed independently.

Example:
```bash
python figures/figure2_growth.py
```

This generates cs2_omega.pdf, which is identical to the figure used in the paper.
Boltzmann Solver Implementations
The Omega-field perturbation equations are implemented in both CLASS and CAMB:
The CLASS implementation modifies the background and perturbation modules to include the conserved Omega charge.
The CAMB implementation serves as an independent consistency check.
These implementations demonstrate agreement with ΛCDM in the appropriate limits and reproduce the clustering behavior discussed in the manuscript.

## Data and Code Availability

All scripts required to reproduce the figures and numerical results presented in the manuscript are publicly available in this repository.
Exploratory, intermediate, or diagnostic scripts not required for figure generation are available from the author upon reasonable request.

## License

This repository is released under the MIT License.
