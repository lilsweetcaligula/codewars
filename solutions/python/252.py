
def bin_to_hex(binary_string):
    # return the hexadecimal representation of the 
    # numerical equivalent of binary_string
    lookup = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
        '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f',
    }
    chunk_size = 4
    binary_string = binary_string.rjust(
        len(binary_string) + chunk_size - len(binary_string) % chunk_size, '0')        
    return(''.join(
        lookup[binary_string[start:start + chunk_size]] 
            for start in range(0, len(binary_string), chunk_size))
                .lstrip('0') or '0')
        
    
def hex_to_bin(hex_string):
    # return the binary representation of the
    # numerical equivalent of hex_string
    lookup = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '6': '0110', '5': '0101', '7': '0111', 
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',  
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }
    return(''.join(
        map(lambda digit: lookup[digit.lower()], hex_string))
            .lstrip('0') or '0')