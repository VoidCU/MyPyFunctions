def nep_date_eng(x): 
    """
    This function converts the date from Nepali to English date.
    order will be same as input format and space is replaced by '/'
    २३ वैशाख २०८० => 23/5/2023
    २०७९ १२ १२ => 2023/12/12 
    """
    replace_dict={
    'वैशाख':'1',
    'जेठ':'2',
    'असार':'3',
    'साउन':'4',
    'भदौ':'5',
    'असोज':'6',
    'कात्तिक':'7',
    'कार्तिक':'7',
    'मङ्सिर':'8',
    'मंसिर':'8',
    'पुस':'9',
    'पुष':'9',
    'माघ':'10',
    'फागुन':'11',
    'चैत':'12',
    '१':'1',
    '२':'2',
    '३':'3',
    '४':'4',
    '५':'5',
    '६':'6',
    '७':'7',
    '८':'8',
    '९':'9',
    '०':'0',
    ' ':'/'
    }
    x=x.strip()
    for i,j in replace_dict.items():
        x=x.replace(i,j)
    return x #return '26/7/2079'

