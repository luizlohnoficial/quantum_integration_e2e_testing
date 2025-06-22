from unittest import mock
import logging
import main


def test_end_to_end():
    logger = logging.getLogger(__name__)
    logger.info("Testing end-to-end pipeline")
    with mock.patch('main.execute_circuit', return_value={'0': 10}):
        with mock.patch('main.build_quantum_circuit', return_value='c'):
            main.run_pipeline('config.yaml')
    logger.info("End-to-end test finished")
