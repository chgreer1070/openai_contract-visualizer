from __future__ import annotations

import pytest


def test_deterministic_mapping_to_m_l_h_s(classifier_module, synthetic_contract_input):
    classify_fn = getattr(classifier_module, "classify_type", None)
    if classify_fn is None:
        pytest.skip("classify_type function is not available")

    first = classify_fn(synthetic_contract_input)
    second = classify_fn(synthetic_contract_input)

    assert first == second
    assert first in {"M", "L", "H", "S"}
