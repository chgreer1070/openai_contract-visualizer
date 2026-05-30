from __future__ import annotations

import importlib
import json
from pathlib import Path
from typing import Any

import pytest

FIXTURE_DIR = Path(__file__).parent / "fixtures"


def _try_import(*module_names: str):
    for name in module_names:
        try:
            return importlib.import_module(name)
        except ModuleNotFoundError:
            continue
    pytest.skip(f"None of the modules exist: {module_names}")


def _first_attr(module: Any, *names: str):
    for name in names:
        if hasattr(module, name):
            return getattr(module, name)
    pytest.skip(f"None of attributes exist in {module.__name__}: {names}")


@pytest.fixture(scope="session")
def synthetic_contract_input() -> dict[str, Any]:
    with (FIXTURE_DIR / "synthetic_contract_input.json").open("r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def dashboard_ready_output() -> dict[str, Any]:
    with (FIXTURE_DIR / "dashboard_ready_output.json").open("r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def models_module():
    return _try_import("src.models", "app.models", "contract_visualizer.models", "models")


@pytest.fixture(scope="session")
def classifier_module():
    return _try_import(
        "src.type_classification", "app.type_classification", "contract_visualizer.type_classification", "type_classification"
    )
