"""
This file tests the response module
"""

import quest
import pytest
import numpy as np

def test_response():

    rhf_options = \
    {
        'e_conv': 1.e-8,
        'd_conv': 1.e-8,
        'diis': True,
        'max_diis': 7,
        'max_iter': 100,
    }

    mol_str = quest.mollib["h2o"]
    basis = 'cc-pVDZ'

    molecule = quest.Molecule(mol_str, basis)
    wfn = quest.Wavefunction(molecule, rhf_options)

    scf_energy = quest.scf_module.compute_rhf(wfn)
 
    polarizability = quest.response.response(wfn)
    print(polarizability)

    test_polarizability = np.array([[2.97055439, 0.000, 0.000], [0.000, 10.5001391, 0.000], [0.000, 0.000, 6.64751258]])

    assert np.allclose(test_polarizability, polarizability)

    pass
