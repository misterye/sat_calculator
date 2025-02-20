"""
ModCod configurations and calculations for satellite link efficiency
"""

# Modulation order mapping
MODULATION_ORDER = {
    "BPSK": 1,
    "QPSK": 2,
    "8PSK": 3,
    "16APSK": 4,
    "32APSK": 5,
    "64APSK": 6,
    "128APSK": 7,
    "256APSK": 8
}

# Default Reed-Solomon code rate
RS_CODE = 0.92

# Roll-off factor
ROLL_OFF = 0.05

# Available ModCod options
DOWNLINK_MODCODS = [
    "BPSK 1/5", "BPSK 11/45", "BPSK 4/15", "BPSK 1/3", "QPSK 2/9",
    "QPSK 11/45", "QPSK 1/4", "QPSK 4/15", "QPSK 13/45", "QPSK 14/45",
    "QPSK 1/3", "QPSK 2/5", "QPSK 9/20", "QPSK 7/15", "QPSK 1/2", "QPSK 11/20",
    "QPSK 8/15", "QPSK 3/5", "QPSK 2/3", "QPSK 32/45", "QPSK 3/4", "QPSK 4/5",
    "QPSK 5/6", "QPSK 8/9", "QPSK 9/10", "8PSK 7/15", "8PSK 8/15", "8PSK 3/5",
    "8PSK 26/45", "8PSK 23/36", "8PSK 2/3", "8PSK 25/36", "8PSK 13/18",
    "8PSK 32/45", "8PSK 3/4", "8PSK 5/6", "8PSK 8/9", "8PSK 9/10",
    "16APSK 1/2-L", "16APSK 7/15", "16APSK 8/15-L", "16APSK 5/9-L",
    "16APSK 8/15", "16APSK 3/5-L", "16APSK 26/45", "16APSK 3/5",
    "16APSK 28/45", "16APSK 23/36", "16APSK 2/3-L", "16APSK 2/3",
    "16APSK 25/36", "16APSK 13/18", "16APSK 32/45", "16APSK 3/4", "16APSK 7/9",
    "16APSK 4/5", "16APSK 5/6", "16APSK 77/90", "16APSK 8/9", "16APSK 9/10",
    "32APSK 2/3-L", "32APSK 2/3", "32APSK 32/45", "32APSK 11/15", "32APSK 3/4",
    "32APSK 7/9", "32APSK 4/5", "32APSK 5/6", "32APSK 8/9", "32APSK 9/10",
    "64APSK 32/45-L", "64APSK 11/15", "64APSK 7/9", "64APSK 4/5", "64APSK 5/6",
    "128APSK 3/4", "128APSK 7/9", "256APSK 29/45-L", "256APSK 2/3-L",
    "256APSK 31/45-L", "256APSK 32/45", "256APSK 11/15-L", "256APSK 3/4"
]

UPLINK_MODCODS = [
    "QPSK-7/20", "QPSK-2/5", "QPSK-9/20", "QPSK-1/2", "QPSK-11/20", "QPSK-3/5",
    "QPSK-13/20", "QPSK-7/10", "QPSK-3/4", "QPSK-4/5", "QPSK-17/20",
    "8PSK-7/15", "8PSK-1/2", "8PSK-8/15", "8PSK-17/30", "8PSK-3/5",
    "8PSK-19/30", "8PSK-2/3", "8PSK-7/10", "8PSK-11/15", "16APSK-2/5",
    "16APSK-17/40", "16APSK-9/20", "16APSK-19/40", "16APSK-1/2",
    "16APSK-21/40", "16APSK-11/20", "16APSK-23/40", "16APSK-3/5", "16APSK-5/8",
    "16APSK-13/20", "16APSK-27/40", "16APSK-7/10", "16APSK-29/40",
    "16APSK-3/4", "16APSK-31/40", "16APSK-4/5", "64APSK-31/60", "64APSK-8/15",
    "64APSK-11/20", "64APSK-17/30", "64APSK-7/12", "64APSK-3/5",
    "64APSK-37/60", "64APSK-19/30", "64APSK-13/20", "64APSK-2/3",
    "64APSK-41/60", "64APSK-7/10", "64APSK-43/60", "64APSK-11/15",
    "64APSK-3/4", "64APSK-23/30", "64APSK-47/60", "64APSK-4/5", "64APSK-49/60",
    "64APSK-5/6", "64APSK-17/20", "64APSK-13/15", "64APSK-53/6"
]


def parse_modcod(modcod_str: str) -> tuple[str, float]:
    """
    Parse ModCod string to get modulation type and code rate
    Example: "QPSK 3/4" -> ("QPSK", 0.75)
    """
    parts = modcod_str.replace("-", " ").split()
    modulation = parts[0]
    code_rate = parts[1]

    if "/" in code_rate:
        num, den = map(int, code_rate.split("/"))
        rate = num / den
    else:
        rate = float(code_rate)

    return modulation, rate


def get_modulation_order(modulation: str) -> int:
    """Get the modulation order for a given modulation type"""
    return MODULATION_ORDER.get(modulation, 0)
