def get_pid():
    from socket import gethostname
    return gethostname()