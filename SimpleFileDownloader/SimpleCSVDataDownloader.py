from urllib import request
goog_url='http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=22&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def downloadCSVData(url):
    response=request.urlopen(url)
    file=response.read()
    file_str=str(file)
    lines=file_str.split('\\n')
    dest_url=r'goog.csv'
    csvFile=open(dest_url,'w')
    for line in lines:
        csvFile.writelines(line + '\n')
    csvFile.close()
    
    
downloadCSVData(goog_url)    

