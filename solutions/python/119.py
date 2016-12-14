def calculate_tip(amount, rating):
    try:
        from math import ceil
        return ceil(amount * { 
            'terrible': 0.0, 
            'poor': 0.05, 
            'good': 0.1, 
            'great': 0.15, 
            'excellent': 0.2 
        }[rating.lower()])
    except KeyError:
        return 'Rating not recognised'