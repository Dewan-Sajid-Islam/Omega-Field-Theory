#include "input.h"
#include "background.h"

int input_read_parameters_omega(
    struct file_content *pfc,
    struct precision *ppr,
    struct background *pba
) {

  class_read_double("omega_phi0", pba->omega_phi0);
  class_read_double("omega_f1",   pba->omega_f1);

  return _SUCCESS_;
}
