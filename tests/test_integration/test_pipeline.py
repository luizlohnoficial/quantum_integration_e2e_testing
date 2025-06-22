import builtins
from unittest import mock

import main


def test_pipeline_runs(monkeypatch):
    with mock.patch('main.execute_circuit', return_value={'0': 1}):
        with mock.patch('main.build_quantum_circuit', return_value='c'):
            main.run_pipeline('config.yaml')
