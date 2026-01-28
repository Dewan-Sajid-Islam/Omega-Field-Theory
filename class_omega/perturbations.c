#include "perturbations.h"

/* ============================================================
   Omega-field perturbations (reference implementation)
   ============================================================ */

int perturbations_omega_evolve(
    struct perturbations *ppt,
    double k,
    double a,
    double *delta_omega,
    double *theta_omega
) {

  double meff2;
  meff2 = 12.0 * ppt->omega_f1 * ppt->omega_phi0 * ppt->omega_phi0;

  /* Effective sound speed squared */
  double cs2 = (k*k/a/a) / (k*k/a/a + meff2);

  *delta_omega = -cs2 * (*delta_omega);
  *theta_omega = 0.0;

  return _SUCCESS_;
}
