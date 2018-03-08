from django import db
from test1.models import *


FINGER_TMP_Count = FINGER_TMP.objects.filter(Pin=1).filter(TMP=2).count()
print(FINGER_TMP_Count)
ATT_LOG = ATT_LOG.objects.all()
print(ATT_LOG)



