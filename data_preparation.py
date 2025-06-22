"""Data preparation for quantum portfolio optimization.

Loads asset data and covariance matrix from configuration.
"""

from typing import Any, Dict, List, Tuple

import logging


def load_data(config: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[List[float]]]:
    """Return assets list and covariance matrix from config."""
    assets = config.get("assets", [])
    covariance = config.get("covariance_matrix", [])
    logging.debug("Assets: %s", assets)
    logging.debug("Covariance matrix: %s", covariance)
    return assets, covariance
