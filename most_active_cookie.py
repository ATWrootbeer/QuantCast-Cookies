import csv 
import sys

#grabs the most seen cookies in the dict or returns None
def mostActiveCookies(dict):
    bestCookies=None
    highestSeen=0
    #print(time)
    for key in dict.keys():
        cookie=key
        seen=dict[key]
        if(bestCookies==None or highestSeen<seen):
            bestCookies=[cookie]
            highestSeen=seen
        elif(highestSeen==seen):
            bestCookies.append(cookie)
    return(bestCookies)

#0 True if date is strictly less than goalDate false otherwise
def compareDates(Year,Month,Day,goalYear,goalMonth,goalDay):
    if(Year<goalYear):
        return True
    elif(Year>goalYear):
        return True
    else:
        if(Month<goalMonth):
            return True
        elif(Month>goalMonth):
            return False
        else:
            if(Day<goalDay):
                return True
            return False
  
#scans the csv file and only cares about cookies on goalDate
#Should end early if the goalDate is later than the current date 
def mostRecentCookies(filename,goalDate):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        dates=dict()
        reachedGoal=0
        [goalYear,goalMonth,goalDay]=goalDate.split("-")
        for row in reader:
            dateTime=row[1].split("T")
            date=dateTime[0]
            cookie=row[0]
            [Year,Month,Day]=date.split("-")
            #once the dates passes the goalDate, all future lines are not needed
            if(compareDates(Year,Month,Day,goalYear,goalMonth,goalDay)):break
            if(Year!=goalYear or Month!=goalMonth or Day!=goalDay): continue
            val=dates.get(cookie,0)
            dates[cookie]=val+1
    Cookies=mostActiveCookies(dates)
    if(Cookies==None): 
        print("no cookies were found on " + goalDate)
        return
    for cookie in Cookies:
        print(cookie)
    
def process(filename, command):
    if(command=="-d"):
        date=sys.argv[3]
        mostRecentCookies(filename,date)
    return
       
def main():
    script = sys.argv[0]
    filename=sys.argv[1]
    command=sys.argv[2]
    assert command in ["-d"],"command" + command + "is not defined"
    process(filename,command)

if __name__ == '__main__':
   main()