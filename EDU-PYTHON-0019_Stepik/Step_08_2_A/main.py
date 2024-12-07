import os
import logging.config
import yaml
from module_1 import main

print(os.getcwd())

with open('EDU-PYTHON-0019_Stepik/Step_08_2_A/logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

main()