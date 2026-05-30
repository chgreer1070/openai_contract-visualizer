from __future__ import annotations

import pytest


def test_validation_status_and_error_warning_collection(models_module, dashboard_ready_output):
    report_cls = getattr(models_module, "ValidationReport", None)
    if report_cls is None:
        pytest.skip("ValidationReport model is not available")

    payload = dashboard_ready_output["validation_report"]
    report = report_cls(**payload)

    assert report.status in {"valid", "warning", "invalid"}
    assert isinstance(report.errors, list)
    assert isinstance(report.warnings, list)
