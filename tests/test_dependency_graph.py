from __future__ import annotations

import pytest


def test_node_edge_construction_correctness(models_module, synthetic_contract_input):
    graph_cls = getattr(models_module, "DependencyGraph", None)
    if graph_cls is None:
        pytest.skip("DependencyGraph model is not available")

    dep_payload = synthetic_contract_input["dependencies"]
    graph = graph_cls(**dep_payload)

    assert len(getattr(graph, "nodes")) == len(dep_payload["nodes"])
    assert len(getattr(graph, "edges")) == len(dep_payload["edges"])

    node_ids = {node.id for node in graph.nodes}
    for edge in graph.edges:
        assert edge.source in node_ids
        assert edge.target in node_ids
