"""
    Public Safety Crime Logs scraping script by Jeremy Cohen '16'
"""

import os

years = ['06','07', '08', '09', '10', '11', '12', '13']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
daysPerMonth = {
    'jan' : 31,
    'feb' : 28,
    'mar' : 31,
    'apr' : 30,
    'may' : 31,
    'jun' : 30,
    'jul' : 31,
    'aug' : 31,
    'sept' : 30,
    'oct' : 31,
    'nov' : 30,
    'dec' : 31,
}

for year in years:
    for month in months:
        if year == '06' and month not in ['sep', 'oct', 'nov', 'dec']:
            continue
        for day in range(1, daysPerMonth[month] +1):
            pdf_filename = 'data/%s_%s_%d.pdf' % (year, month, day)
            text_filename = 'txt/%s_%s_%d.txt' % (year, month, day)
            print text_filename
            os.system("python pdf2txt.py %s > %s" % (pdf_filename, text_filename))