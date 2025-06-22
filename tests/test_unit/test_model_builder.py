from model_builder import build_qubo


def test_build_qubo():
    assets = [{'name': 'A'}, {'name': 'B'}]
    cov = [[1, 0], [0, 1]]
    qubo = build_qubo(assets, cov)
    assert len(qubo) == 2 and len(qubo[0]) == 2
