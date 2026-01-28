! ============================================================
! Omega-field reference equations for CAMB
! ============================================================
! This file provides a minimal reference implementation of the
! Omega-field background and perturbation contributions.
! It is intended for cross-validation and pedagogical purposes.
! ============================================================

module OmegaEquations
  implicit none
  real(8) :: omega_phi0
  real(8) :: omega_f1
contains

  function omega_meff2(phi) result(meff2)
    real(8), intent(in) :: phi
    real(8) :: meff2
    meff2 = 12.d0 * omega_f1 * phi * phi
  end function omega_meff2

end module OmegaEquations
