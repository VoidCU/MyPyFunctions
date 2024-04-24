from datetime import date,timedelta
import numpy as np

def BStoAD(bsdate): #bsdate in the format of 'day/month/year' BS date from 2072-01-01 to 2082-1-1 only
    days_in_month_before_2082_baishak_1=np.array([31,29,30,29,30,30,30,31,32,31,32,31,30,30,29,29,30,30,30,31,32,31,32,31,30,30,29,30,29,30,31,31,31,32,31,31,30,30,29,30,29,30,31,31,32,31,31,31,31,29,30,29,30,30,30,31,32,31,32,31,30,30,29,29,30,30,30,31,32,31,32,31,30,30,29,30,29,30,31,31,31,32,31,31,30,30,29,30,29,30,31,31,32,31,31,31,31,30,29,29,30,30,30,31,32,31,32,31,30,30,29,30,29,30,30,31,32,31,32,31])
    date1=date(2025,4,14)
    y=0
    y+=(2081-int(bsdate.split('/')[2]))*12
    y+=12-int(bsdate.split('/')[1])
    y=days_in_month_before_2082_baishak_1[0:y].sum()-int(bsdate.split('/')[0])+days_in_month_before_2082_baishak_1[y]+1
    date2=date1-timedelta(days=int(y))
    return date2.strftime('%Y-%m-%d') #returns date in the format of 'year-month-day' AD

#Example
print(BStoAD('1/1/2072')) #2015-04-14
