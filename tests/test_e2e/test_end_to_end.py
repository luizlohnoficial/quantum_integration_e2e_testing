from unittest import mock
import main


def test_end_to_end():
    with mock.patch('main.execute_circuit', return_value={'0': 10}):
        with mock.patch('main.build_quantum_circuit', return_value='c'):
            main.run_pipeline('config.yaml')
