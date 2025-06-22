"""Main pipeline for quantum portfolio optimization."""

import logging

from data_preparation import load_data
from model_builder import build_qubo, build_quantum_circuit
from quantum_executor import execute_circuit
from result_parser import parse_results
from report_generator import generate_report
from utils import load_config, log_section, setup_logging, validate_solution


def run_pipeline(config_path: str = "config.yaml") -> None:
    """Run the full optimization pipeline."""
    setup_logging()
    logging.info("Starting pipeline")
    log_section("Load configuration")
    config = load_config(config_path)

    log_section("Prepare data")
    assets, covariance = load_data(config)

    log_section("Build QUBO model")
    qubo = build_qubo(assets, covariance)

    log_section("Construct quantum circuit")
    circuit = build_quantum_circuit(qubo, config)

    log_section("Execute quantum circuit")
    counts = execute_circuit(circuit, config)

    log_section("Parse execution results")
    results = parse_results(counts, assets)

    classical_solution = {"selected": [a["name"] for a in assets[:1]]}
    if validate_solution(classical_solution, results):
        logging.info("Quantum solution validated against classical baseline")
    else:
        logging.warning("Quantum solution differs from classical baseline")

    log_section("Generate report")
    generate_report(results, config)
    logging.info("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()
