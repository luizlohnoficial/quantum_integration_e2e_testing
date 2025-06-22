"""Generate execution reports using a template."""

import logging
from typing import Any, Dict

from utils import save_json, save_text


def generate_report(results: Dict[str, Any], config: Dict[str, Any]) -> None:
    """Generate text and JSON reports from results."""
    logging.debug("Generating report with results: %s", results)
    with open("report_template.txt", "r", encoding="utf-8") as file:
        template = file.read()

    report_text = template.format(results=results)
    save_text(report_text, "report.txt")
    save_json(results, "report.json")
    logging.info("Reports generated")
    logging.debug("Report generation complete")
