def adjustNumberInRange(x: float) -> float:
    """Adjust number into range (0,100)"""
    if x <= 0:
        return 1e-12
    if x >= 100:
        return 100 - 1e-12
    return x
