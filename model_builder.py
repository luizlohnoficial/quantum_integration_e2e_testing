"""Model builder for portfolio optimization.

Creates QUBO representation and quantum circuit using Qiskit.
"""

from typing import Any, Dict, List

import logging


def build_qubo(assets: List[Dict[str, Any]], covariance: List[List[float]]) -> List[List[float]]:
    """Create a toy QUBO matrix."""
    logging.debug("Building QUBO matrix")
    num_assets = len(assets)
    qubo = [[0.0 for _ in range(num_assets)] for _ in range(num_assets)]
    for i in range(num_assets):
        for j in range(num_assets):
            qubo[i][j] += covariance[i][j]
    logging.info("QUBO matrix dimension: %dx%d", num_assets, num_assets)
    logging.debug("QUBO matrix built: %s", qubo)
    logging.debug("QUBO build complete")
    return qubo


def build_quantum_circuit(qubo: List[List[float]], config: Dict[str, Any]):
    """Build a simple quantum circuit from QUBO using Qiskit."""
    logging.debug("Building quantum circuit")
    try:
        from qiskit import QuantumCircuit
    except Exception as exc:  # pragma: no cover - qiskit optional
        logging.error("Qiskit not available: %s", exc)
        raise

    num_qubits = qubo.shape[0]
    circuit = QuantumCircuit(num_qubits, num_qubits)
    for qubit in range(num_qubits):
        circuit.h(qubit)
    circuit.measure(range(num_qubits), range(num_qubits))
    logging.info("Quantum circuit created with %d qubits", num_qubits)
    logging.debug("Quantum circuit build complete")
    return circuit
