# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')

def ipv4__parser(ip_addr, mask):
    import operator
    separator = '.'
    ip_bytes, mask_bytes = (
        list(map(int, data.split(separator))) for data in (ip_addr, mask))
    net_addr_bytes  = map(operator.and_, ip_bytes, mask_bytes)
    host_addr_bytes = map(operator.sub, ip_bytes, net_addr_bytes)
    return(
            separator.join(map(str, net_addr_bytes)), 
            separator.join(map(str, host_addr_bytes)))