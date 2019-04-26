from datetime import datetime
  
def add_month(mDate, months):
    nYear = mDate.year + months / 12
    dMonth = months % 12
    if dMonth + mDate.month > 12:
        nYear += 1
    nMonth = (mDate.month + dMonth) % 12 or 12
    nDay = mDate.day
 
    try:
        return datetime(nYear, nMonth, nDay)
    except Exception, e:
        pass
    if nMonth == 2:
        nDay = 28
        if (nYear % 4 == 0 and  nYear % 100 != 0) or nYear % 400 == 0:
            nDay = 29
    else:
        nDay = 30
    return datetime(nYear, nMonth, nDay)
 
