import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "config" / "config.yaml"


def get_config(path):
    with open(path) as conf:
        parsed_config = yaml.safe_load(conf)
        return parsed_config


config = get_config(config_path)
