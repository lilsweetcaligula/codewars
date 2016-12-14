def to_seconds(time_string):
    import re
    match = re.match(
        r'\A(?P<hours>\d{2}):(?P<minutes>[0-5]\d):(?P<seconds>[0-5]\d)\Z', time_string)
    return (
            int(match.group('hours')) * 3600 
          + int(match.group('minutes'))  * 60
          + int(match.group('seconds')) if match else None)def to_seconds(time_string):
    import re
    match = re.match(
        r'\A(?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})\Z', 
        time_string)
    if match:
        hours, minutes, seconds = (int(value) for value in (
                match.group('hours'), 
                match.group('minutes'), 
                match.group('seconds')))
        if all(0 <= value < 60 for value in (minutes, seconds)):
            return hours * 3600 + minutes * 60 + seconds
    return None