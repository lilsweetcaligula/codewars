def find_needle(haystack, target = "needle"):
    try:
        return "found the {0} at position {1}".format(target, haystack.index(target))
    except ValueError:
        return ""