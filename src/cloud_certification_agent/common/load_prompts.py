import os

import yaml


def load_agent_config(name: str):
    package = os.path.dirname(os.path.abspath(__file__))
    prompt_file = f"{package}/../prompts/{name}.yaml"
    try:
        with open(prompt_file, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"An error ocurred in load_agent_config: {e}")
        raise ValueError()
