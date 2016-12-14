cannons_ready = (lambda gunners: 
    'Fire!' if all(gunners[gunner] == 'aye' for gunner in gunners) 
    else 'Shiver me timbers!')