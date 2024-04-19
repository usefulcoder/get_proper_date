def buildDate(today):
    day = today.day
    month = today.month
    year = today.year
    
    
    startDate = {
        "day" : 0,
        "month" : 0,
        "year" : year
    }

    endDate = {
        "day" : 0,
        "month" : 0,
        "year" : year
    }

    def formatItem(item):
        if item < 10:
            
            return f"0{item}"
        else:
           
            return f"{item}"


    if day - 3 < 0:
        tempMonth = month - 1
        if tempMonth == 0:
            tempMonth = 12
            startDate['year'] = year - 1
            endDate['year'] = year - 1

        if tempMonth in [1,3,5,7,8,10,12]:
            startDate['day'] = 30
            endDate['day'] = 31
            
        elif tempMonth in [4,6,9,11]:
            startDate['day'] = 29
            endDate['day'] = 30

        elif tempMonth in [2]:
            if calendar.isleap(year):
                startDate['day'] = 28
                endDate['day'] = 29
            else:
                startDate['day'] = 27
                endDate['day'] = 28
        if tempMonth <= 9:
            tempMonth = "0" + str(tempMonth)
        startDate['month'] = tempMonth
        endDate['month'] = tempMonth

    if day - 2 == 0:
        
        tempMonth = month - 1
        if tempMonth == 0:
            tempMonth = 12
            startDate['year'] = year - 1
        
        if tempMonth in [1,3,5,7,8,10,12]:
            startDate['day'] = 31
            
        elif tempMonth in [4,6,9,11]:
            startDate['day'] = 30
            
        elif tempMonth in [2]:
            if calendar.isleap(year):
                startDate['day'] = 29
                
            else:
                startDate['day'] = 28

        startDate['month'] = tempMonth        
        endDate['day'] = formatItem(day - 1)
        endDate['month'] = formatItem(month)
        endDate['year'] = year


    
    if day - 2 > 0:
       
        startDate['day'] = formatItem(day - 2)
        endDate['day'] = formatItem(day - 1)

        startDate['month'] = formatItem(month)
        endDate['month'] = formatItem(month)
    
    if startDate["day"] <= 9:
        startDate["day"] = "0" + startDate["day"]
    if endDate["day"] <= 9:
        endDate["day"] = "0" + endDate["day"]
    return [f"{startDate['year']}-{startDate['month']}-{startDate['day']}", f"{endDate['year']}-{endDate['month']}-{endDate['day']}"]