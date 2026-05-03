from __future__ import annotations

import pytest


def test_model_instantiation_for_required_schemas(models_module, synthetic_contract_input, dashboard_ready_output):
    contract_cls = getattr(models_module, "Contract", None)
    recovery_cls = getattr(models_module, "RecoveryMechanics", None)
    seam_cls = getattr(models_module, "SeamRisk", None)

    if not all([contract_cls, recovery_cls, seam_cls]):
        pytest.skip("Required schema classes Contract/RecoveryMechanics/SeamRisk are not available")

    contract = contract_cls(**synthetic_contract_input)
    recovery = recovery_cls(**dashboard_ready_output["recovery_mechanics"])
    seam_risk = seam_cls(**dashboard_ready_output["seam_risk"])

    assert contract is not None
    assert recovery is not None
    assert seam_risk is not None


def test_type_m_validator_fails_when_mandatory_fields_missing(models_module):
    type_m_cls = getattr(models_module, "TypeM", None)
    if type_m_cls is None:
        pytest.skip("TypeM model is not available")

    with pytest.raises(Exception):
        type_m_cls()
