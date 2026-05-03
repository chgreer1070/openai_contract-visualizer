from __future__ import annotations

import pytest


def test_seam_risk_object_generation_with_severity_and_owner(models_module, dashboard_ready_output):
    seam_cls = getattr(models_module, "SeamRisk", None)
    if seam_cls is None:
        pytest.skip("SeamRisk model is not available")

    payload = dashboard_ready_output["seam_risk"]
    obj = seam_cls(**payload)

    assert getattr(obj, "severity") in {"M", "L", "H", "S"}
    assert bool(getattr(obj, "owner"))
