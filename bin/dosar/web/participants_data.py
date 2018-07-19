#from dosar import settings
from models import Participants

f= file('C:\Python27\Lib\site-packages\django\bin\dosar\list.csv')
for l in f.readlines():
    l = l.split(',')
    print l
