def whatCentury(yearString):
    year = int(yearString)
    century = year // 100 + (year % 100 != 0)
    return(str(century) + ('th' if 10 < century < 20 
        else ['th','st','nd','rd','th','th','th','th','th','th'][century % 10]))    def whatCentury(year):
    year = int(year)
    century = year // 100 + (year % 100 != 0)
    endings = ['th', 'st', 'nd', 'rd'] + 15 * ['th']
    return str(century) + endings[century % (10 if century > 20 else 20)]