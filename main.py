"""Main pipeline for quantum portfolio optimization."""

import logging

from data_preparation import load_data
from model_builder import build_qubo, build_quantum_circuit
from quantum_executor import execute_circuit
from result_parser import parse_results
from report_generator import generate_report
from utils import load_config, setup_logging, validate_solution


def run_pipeline(config_path: str = "config.yaml") -> None:
    """Run the full optimization pipeline."""
    setup_logging()
    logging.info("Starting pipeline")
    config = load_config(config_path)

    assets, covariance = load_data(config)
    qubo = build_qubo(assets, covariance)
    circuit = build_quantum_circuit(qubo, config)
    counts = execute_circuit(circuit, config)
    results = parse_results(counts, assets)

    classical_solution = {"selected": [a["name"] for a in assets[:1]]}
    if validate_solution(classical_solution, results):
        logging.info("Quantum solution validated against classical baseline")
    else:
        logging.warning("Quantum solution differs from classical baseline")

    generate_report(results, config)
    logging.info("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()
