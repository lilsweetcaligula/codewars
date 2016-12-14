def bareable(heat, humidity):
    return ((heat < 25 and humidity <= 0.5) or (25 <= heat <= 35 and humidity <= 0.4))