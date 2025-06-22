import os
import logging
from utils import load_config, save_json

def test_load_config(tmp_path):
    logger = logging.getLogger(__name__)
    logger.info("Testing load_config")
    cfg_content = 'key: value'
    cfg = tmp_path / 'config.yaml'
    cfg.write_text(cfg_content)
    result = load_config(str(cfg))
    logger.debug("Config result: %s", result)
    assert result['key'] == 'value'


def test_save_json(tmp_path):
    logger = logging.getLogger(__name__)
    logger.info("Testing save_json")
    path = tmp_path / 'out.json'
    data = {'a': 1}
    save_json(data, str(path))
    logger.debug("Saved json exists: %s", path.exists())
    assert path.exists()
