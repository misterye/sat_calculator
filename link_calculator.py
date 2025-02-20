"""
Link efficiency calculator for satellite communications
"""
from modcod import parse_modcod, get_modulation_order, RS_CODE, ROLL_OFF

def calculate_from_datarate(dr: float, modcod: str) -> dict:
    """
    Calculate link parameters from data rate
    
    Args:
        dr: Data rate in kbps
        modcod: ModCod string (e.g., "QPSK 3/4")
    
    Returns:
        Dictionary containing calculated parameters
    """
    modulation, viterbi_fec = parse_modcod(modcod)
    fact = get_modulation_order(modulation)
    
    # Calculate symbol rate
    sr = dr / (fact * viterbi_fec * RS_CODE)
    
    # Calculate bandwidth
    bd = sr * (1 + ROLL_OFF)
    
    # Calculate efficiency
    efficiency = dr / bd
    
    return {
        "data_rate": dr,
        "symbol_rate": sr,
        "bandwidth": bd,
        "efficiency": efficiency,
        "roll_off": ROLL_OFF
    }

def calculate_from_symbolrate(sr: float, modcod: str) -> dict:
    """
    Calculate link parameters from symbol rate
    
    Args:
        sr: Symbol rate in ksps
        modcod: ModCod string (e.g., "QPSK 3/4")
    
    Returns:
        Dictionary containing calculated parameters
    """
    modulation, viterbi_fec = parse_modcod(modcod)
    fact = get_modulation_order(modulation)
    
    # Calculate data rate
    dr = sr * (fact * viterbi_fec * RS_CODE)
    
    # Calculate bandwidth
    bd = sr * (1 + ROLL_OFF)
    
    # Calculate efficiency
    efficiency = dr / bd
    
    return {
        "data_rate": dr,
        "symbol_rate": sr,
        "bandwidth": bd,
        "efficiency": efficiency,
        "roll_off": ROLL_OFF
    }
