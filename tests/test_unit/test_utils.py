import os
from utils import load_config, save_json

def test_load_config(tmp_path):
    cfg_content = 'key: value'
    cfg = tmp_path / 'config.yaml'
    cfg.write_text(cfg_content)
    result = load_config(str(cfg))
    assert result['key'] == 'value'


def test_save_json(tmp_path):
    path = tmp_path / 'out.json'
    data = {'a': 1}
    save_json(data, str(path))
    assert path.exists()
