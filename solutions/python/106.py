def bar_triang(pointA, pointB, pointC, ndigits = 4): # points A, B and C will never be aligned
    xCoords = pointA[0], pointB[0], pointC[0]
    yCoords = pointA[1], pointB[1], pointC[1]
    x0, y0 = (round(sum(coords) / float(len(coords)), ndigits) for coords in (xCoords, yCoords))
    return [x0, y0] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)