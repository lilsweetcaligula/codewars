def areYouPlayingBanjo(name):
    return [name + ' does not play banjo', name + ' plays banjo'][name.startswith('r') or name.startswith('R')]