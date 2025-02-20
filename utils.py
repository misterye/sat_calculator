import numpy as np

def watts_to_dbm(watts: float) -> float:
    """
    Convert watts to dBm
    Formula: P(dBm) = 10*Log10(P(W)) + 10*Log10(1000)
    """
    if watts <= 0:
        raise ValueError("Power in watts must be greater than 0")
    return 10 * np.log10(watts) + 30

def dbm_to_watts(dbm: float) -> float:
    """
    Convert dBm to watts
    Formula: P(W) = 10^((P(dBm)/10)-3)
    """
    return 10 ** ((dbm / 10) - 3)

def validate_input(value: str, input_type: str) -> tuple[bool, str]:
    """
    Validate input values
    Returns: (is_valid, error_message)
    """
    if not value:
        return False, "Please enter a value"
    
    try:
        num = float(value)
        if input_type == 'watts' and num <= 0:
            return False, "Power in watts must be greater than 0"
        return True, ""
    except ValueError:
        return False, "Please enter a valid number"
