import os
import yaml


def load_expected_data(file_path):
    with open(file_path, "r") as yaml_file:
        return yaml.safe_load(yaml_file)["expected_values"]


def get_expected_file_path(relative_path):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "..", "test-data", "ui", relative_path)
