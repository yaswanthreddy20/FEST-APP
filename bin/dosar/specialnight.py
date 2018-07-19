import os
from dosar import settings
# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "dosar.settings"

from web.models import Special_nights
f = file(r'C:\Python27\Lib\site-packages\django\bin\dosar\waves.csv')
for l in f.readlines():
    l= l.split(',')
    print l
    b = Special_nights(college_id=l[0])
    b.save()
