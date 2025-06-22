"""Quantum execution utilities.

Supports local simulator and placeholders for real backends.
"""

from typing import Any, Dict

import logging


def execute_circuit(circuit, config: Dict[str, Any]):
    """Execute the circuit on a simulator or real backend."""
    backend = config.get("backend", "simulator")
    shots = config.get("shots", 1024)
    logging.info("Backend: %s | Shots: %d", backend, shots)
    logging.debug("Circuit: %s", circuit)

    if backend == "simulator":
        try:
            from qiskit import Aer, execute
        except Exception as exc:  # pragma: no cover
            logging.error("Qiskit not available: %s", exc)
            raise
        sim = Aer.get_backend("qasm_simulator")
        job = execute(circuit, backend=sim, shots=shots)
        result = job.result()
        counts = result.get_counts()
        logging.debug("Execution counts: %s", counts)
        logging.info("Execution finished")
        return counts
    else:
        logging.warning("Backend %s not implemented, returning empty result", backend)
        return {}
