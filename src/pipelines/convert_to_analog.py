# pipelines/convert_to_analog.py

import torch
import torch.nn as nn
from aihwkit.nn.conversion import convert_to_analog
from aihwkit.simulator.configs import SingleRPUConfig
import os


def convert_model_to_analog(model: nn.Module, rpu_config: SingleRPUConfig = None, inplace: bool = False, save_path: str = None):
    """
    Converts a standard PyTorch model to an analog-compatible model using AIHWKit.
    
    Args:
        model (nn.Module): The digital PyTorch model.
        rpu_config (SingleRPUConfig, optional): RPU config describing the analog hardware. Defaults to SingleRPUConfig().
        inplace (bool): If True, modifies the model in place.
        
    Returns:
        nn.Module: The converted analog model.
    """
    if rpu_config is None:
        rpu_config = SingleRPUConfig()

    analog_model = convert_to_analog(
        module=model,
        rpu_config=rpu_config,
        inplace=inplace,
        ensure_analog_root=True
    )
    # Optionally, you can program the analog weights if needed
    # analog_model.program_analog_weights()
    # Save the converted model to a file
    if save_path and not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
        torch.save(analog_model.state_dict(), save_path)
        print(f"Analog model saved to {save_path}")

    # Return the converted model
    return analog_model









"""
import torch
from copy import deepcopy
from aihwkit.nn.conversion import convert_to_analog
from aihwkit.simulator.configs import InferenceRPUConfig

def save_analog_model(digital_model_path: str, analog_model_path: str, rpu_config=None):
    # Load your trained digital model (assumes torch.save was used)
    digital_model = torch.load(digital_model_path)
    
    # Use a default inference configuration if none provided
    if rpu_config is None:
        rpu_config = InferenceRPUConfig()
    
    # Convert the digital model to an analog model.
    # Set inplace=False to preserve the original digital model.
    analog_model = convert_to_analog(deepcopy(digital_model), rpu_config, inplace=False, verbose=True)
    
    # Optionally, you might want to "program" the analog weights
    analog_model.program_analog_weights()
    
    # Save the converted analog model to the designated folder
    torch.save(analog_model.state_dict(), analog_model_path)
    print(f"Analog model saved to {analog_model_path}")

# Example usage:
digital_model_path = "path/to/trained_digital_model.pth"
analog_model_path = "path/to/saved_analog_model.pth"
save_analog_model(digital_model_path, analog_model_path)

"""