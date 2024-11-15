import yaml
import math
from typing import Dict
from enum import Enum

class CalculationType(Enum):
    DESIRED_REPLICAS = 1
    REQUESTED_RESOURCE_VALUE = 2

def load_config() -> Dict[str, Dict]:
    try:
        with open("config.yaml", 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")

def calculate_desired_replicas(inputs_values: Dict[str, Dict]) -> None:
    resource_usage = inputs_values["resource"]["usage"]
    resource_requested = inputs_values["resource"]["requested"]
    desired_metric = inputs_values["metric"]["desired"]
    current_replicas = inputs_values["replicas"]["current"]
    current_metric = (resource_usage / resource_requested) * 100
    desired_replicas = math.ceil(current_replicas * (current_metric / desired_metric))
    print(f"Desired replicas: {desired_replicas}")

def get_resource_requested(inputs_values: Dict[str, Dict]) -> None:
    resource_usage = inputs_values["resource"]["usage"]
    desired_metric = inputs_values["metric"]["desired"]
    current_replicas = inputs_values["replicas"]["current"]
    desired_replicas = inputs_values["replicas"]["desired"]
    resource_requested = (current_replicas * resource_usage * 100) / (desired_replicas * desired_metric)
    print(f"Resource requested: {resource_requested}")

def main() -> None:
    configs = load_config()
    calculation_type = CalculationType(configs["calculation_type"])
    input_values = configs["inputs"]
    match calculation_type:
        case CalculationType.DESIRED_REPLICAS:
            calculate_desired_replicas(input_values)
        case CalculationType.REQUESTED_RESOURCE_VALUE:
            get_resource_requested(input_values)
        case _:
            raise ValueError(f"Invalid calculation type: {calculation_type}")

if __name__ == "__main__":
    main()