#include "background.h"

/* ============================================================
   Omega-field background contribution (reference)
   ============================================================ */

int background_omega_density(
    struct background *pba,
    double a,
    double *rho_omega
) {

  double phi = pba->omega_phi0;
  double f1  = pba->omega_f1;

  /* Effective kinetic-dominated energy density */
  *rho_omega = 0.5 * (12.0 * f1 * phi * phi);

  return _SUCCESS_;
}
