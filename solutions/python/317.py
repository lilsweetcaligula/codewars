rake_garden = (lambda garden: 
    " ".join(item if item in 'gravel, rock' else 'gravel' for item in garden.split()))