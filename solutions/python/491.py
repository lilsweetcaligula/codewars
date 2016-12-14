def goodVsEvil(good, evil):
    #TODO Go get'em boys...
    #Oorah!
    from operator import mul
    goodWorth, evilWorth = (
        sum(mul(*warriors) 
            for warriors in zip(map(int, side.split()), stats)) 
                for side, stats in 
                    ((good, (1, 2, 3, 3, 4, 10)), 
                    (evil, (1, 2, 2, 2, 3, 5, 10)))
    )
    if goodWorth > evilWorth:
        return 'Battle Result: Good triumphs over Evil'
    elif evilWorth > goodWorth:
        return 'Battle Result: Evil eradicates all trace of Good'
    return 'Battle Result: No victor on this battle field'