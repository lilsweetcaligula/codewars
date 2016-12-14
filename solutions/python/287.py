replicate = (lambda times, number:
    [number] + replicate(times - 1, number) if times > 0 else [])def replicate(times, number, buffer = None):
    buffer = buffer if buffer != None else []
    if times > 0:
        buffer.append(number)
        return replicate(times - 1, number, buffer)
    return buffer
        