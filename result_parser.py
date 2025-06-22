"""Parse quantum execution results into asset selections."""

from typing import Any, Dict, List

import logging


def parse_results(counts: Dict[str, int], assets: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Return selected assets based on highest count bitstring."""
    logging.debug("Parsing results: %s", counts)
    if not counts:
        logging.error("Empty counts; cannot parse results")
        return {"selected": []}

    best_string = max(counts, key=counts.get)
    selected = [asset["name"] for bit, asset in zip(reversed(best_string), assets) if bit == "1"]
    logging.debug("Best bitstring %s -> selected %s", best_string, selected)
    logging.debug("Result parsing complete")
    return {"selected": selected, "counts": counts}
