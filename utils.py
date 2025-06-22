"""Utilities module.

Glossary:
- QUBO: Quadratic Unconstrained Binary Optimization, matrix formulation for portfolio.
- Backend: Quantum or classical hardware where circuits are executed.
- Shots: Number of circuit executions for sampling results.
- Seed: Random seed for reproducibility.

Provides helper functions for configuration loading, saving results, logging
setup, and solution validation.
"""

import json
import logging
import os
from typing import Any, Dict

try:
    import yaml
except Exception:  # pragma: no cover - allow running without PyYAML
    yaml = None


def _simple_yaml_load(text: str) -> Dict[str, Any]:
    """Very small YAML loader supporting a subset used in tests."""
    def parse_value(value: str):
        value = value.strip().strip('"').strip("'")
        if value.replace('.', '', 1).isdigit():
            return float(value) if '.' in value else int(value)
        return value

    result: Dict[str, Any] = {}
    lines = [ln.rstrip('\n') for ln in text.splitlines() if ln.strip()]
    i = 0
    while i < len(lines):
        line = lines[i]
        if ':' not in line:
            i += 1
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()
        if key in {'assets', 'covariance_matrix'}:
            items = []
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith('-'):
                item_line = lines[i].lstrip()[1:].strip()
                if key == 'assets':
                    item: Dict[str, Any] = {}
                    if item_line:
                        k2, v2 = item_line.split(':', 1)
                        item[k2.strip()] = parse_value(v2)
                    i += 1
                    while i < len(lines) and lines[i].startswith(' ' * 4):
                        sub = lines[i].strip()
                        k2, v2 = sub.split(':', 1)
                        item[k2.strip()] = parse_value(v2)
                        i += 1
                    items.append(item)
                else:
                    row = eval(item_line)
                    items.append([parse_value(str(x)) for x in row])
                    i += 1
            result[key] = items
        else:
            result[key] = parse_value(val)
            i += 1
    return result


def setup_logging(log_file: str = "logs/pipeline.log") -> None:
    """Configure structured logging to both file and console."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )


def log_section(title: str) -> None:
    """Output a formatted section header for logs."""
    border = "=" * 10
    logging.info("%s %s %s", border, title, border)


def load_config(path: str = "config.yaml") -> Dict[str, Any]:
    """Load YAML configuration file."""
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    if yaml is not None:
        config = yaml.safe_load(text)
    else:
        config = _simple_yaml_load(text)
    logging.debug("Configuration loaded: %s", config)
    return config


def save_json(data: Dict[str, Any], path: str) -> None:
    """Save dictionary as JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    logging.debug("Saved JSON results to %s", path)


def save_text(report: str, path: str) -> None:
    """Save plain text report."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)
    logging.debug("Saved text report to %s", path)


def validate_solution(classical: Dict[str, Any], quantum: Dict[str, Any]) -> bool:
    """Dummy validation comparing classical and quantum results."""
    return classical.get("selected") == quantum.get("selected")
