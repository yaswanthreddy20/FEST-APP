import os
import datetime
from dosar import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "dosar.settings"
fest_code = '14WV'
from web.models import Participants

f= file(r'C:\Python27\Lib\site-packages\django\bin\dosar\list.csv')
try:
	pre_id = Participants.objects.all().order_by("-id")[0].id+1
except:
	pre_id=1
pre_id=("%4.0f"%pre_id).replace(' ','0')
for l in f.readlines():
	l = l.split(',')
	print l
	b = Participants(name=l[0],college=l[1],city = l[2],accomm=l[3],events=l[4],mobile=l[5],payment=l[6],reg_date=datetime.datetime.now(),fest_id=fest_code+str(pre_id)+'P' )
	b.save()