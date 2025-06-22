# Quantum Portfolio Optimization

This project demonstrates a simple pipeline for portfolio optimization using quantum computing concepts. It loads a configuration file, builds a QUBO model, executes a quantum circuit on a simulator, parses the results and generates reports.

## Requirements

See `requirements.txt` for required Python packages. The pipeline works without real quantum backends by default.

## Usage

```bash
python main.py
```
The configuration file `config.yaml` now includes a `risk_free_rate` parameter which reflects typical market risk-free returns.


## Tests

Run all tests using pytest:

```bash
pytest
```

## Generating Synthetic Market Data

A helper script `data_generator.py` creates a CSV file with 50,000 synthetic
market records. Each record contains typical fields used by financial markets:
asset symbol, date, open, high, low, close and traded volume. Run the script to
produce the dataset under `data/market_data.csv`:

```bash
python data_generator.py
```
