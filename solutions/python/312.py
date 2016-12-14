def wallpaper(length,
              width,
              height,
              rollLength   = 10.0,
              rollWidth    = 0.52,
              surplusRatio = 0.15):
    
    from math import ceil
    rollSurfaceArea  = rollLength * rollWidth
    totalSurfaceArea = (
        (width != 0 and height != 0 and length != 0) 
            * (2 * length * height + 2 * width * height))
    rollCount = totalSurfaceArea / rollSurfaceArea
    return [
      'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
      'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
      'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
    ][ceil(rollCount + rollCount * surplusRatio)]