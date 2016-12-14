def replace_all(obj, find, replace):
    conv = "".join if isinstance(obj, str) else lambda x : x
    return conv([item if item != find else replace for item in obj])