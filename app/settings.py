import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "config" / "config.yaml"


def get_config(path):
    with open(path) as conf:
        return yaml.safe_load(conf)


config = get_config(config_path)
