
# src/main.py
"""
# Main Script for Running Experiments with Hydra

This script serves as the entry point for running experiments using the Hydra framework. 
It utilizes a configuration file to manage experiment parameters and delegates the 
execution to the `run_experiment` function.

Functions:
    main(cfg: DictConfig): The main function decorated with `@hydra.main` to initialize 
    the Hydra configuration and execute the experiment.

Usage:
    - The script is executed as the main module.
    - It loads the configuration from the `../configs/default.yaml` file.
    - Calls the `run_experiment` function with the loaded configuration.
"""

# THE CODE (need to install HYDRA, OMEGACONF before using main.py - currently using each script separately)
"""
import hydra
from omegaconf import DictConfig
from run_task import run_task

@hydra.main(config_path="../configs", config_name="default", version_base=None)
def main(cfg: DictConfig):
    run_task(cfg)

if __name__ == "__main__":
    main()
"""