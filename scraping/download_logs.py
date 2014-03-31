"""
    Public Safety Crime Logs scraping script by Jeremy Cohen '16'
"""

# http://web.princeton.edu/sites/publicsafety/includes/08apr17inc.pdf
import urllib2

years = ['06','07', '08', '09', '10', '11', '12', '13']
# months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months = ['sept']
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
        for day in range(1, daysPerMonth[month] + 1):
            uri = "http://web.princeton.edu/sites/publicsafety/includes/%s%s%dinc.pdf" % (year, month, day)
            print uri
            try:
                url = urllib2.urlopen(uri)
                filename = 'data/%s_%s_%d.pdf' % (year, month, day)
                f = open(filename, 'wb')
                f.write(url.read())
                f.close()
            except:
                print "ERROR!!"
                pass
