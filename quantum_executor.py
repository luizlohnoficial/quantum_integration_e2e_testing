"""Quantum execution utilities.

Supports local simulator and placeholders for real backends.
"""

from typing import Any, Dict

import logging


def execute_circuit(circuit, config: Dict[str, Any]):
    """Execute the circuit on a simulator or real backend."""
    backend = config.get("backend", "simulator")
    shots = config.get("shots", 1024)
    logging.debug("Executing on backend %s with %d shots", backend, shots)

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
        return counts
    else:
        logging.warning("Backend %s not implemented, returning empty result", backend)
        return {}
