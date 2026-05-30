from __future__ import annotations

import pytest


def test_recovery_mechanics_object_creation_and_required_fields(models_module, dashboard_ready_output):
    recovery_cls = getattr(models_module, "RecoveryMechanics", None)
    if recovery_cls is None:
        pytest.skip("RecoveryMechanics model is not available")

    payload = dashboard_ready_output["recovery_mechanics"]
    obj = recovery_cls(**payload)

    for field in ("enabled", "window_days", "owner"):
        assert hasattr(obj, field), f"Missing required field '{field}' on RecoveryMechanics"
