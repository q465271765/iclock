from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)


class iclock(models.Model):

    SN = models.CharField(max_length=50)
    options = models.CharField(max_length=20)
    pushver = models.CharField(max_length=30)
    language = models.CharField(max_length=10)
    Stamp = models.CharField(max_length=30)

    def __str__(self):
        return self.SN+':'+self.language

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'


class ATT_LOG(models.Model):

    SN = models.CharField(max_length=50)
    User_PIN = models.CharField(max_length=50)
    Verify_Type = models.CharField(max_length=50)
    Verify_Time = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    Work_Code_ID = models.CharField(max_length=50)
    Sensor_NO = models.CharField(max_length=50)
    Att_Flag = models.CharField(max_length=50)
    CREATE_ID = models.CharField(max_length=50)
    MODIFY_TIME = models.CharField(max_length=50)
    SEND_FLAG = models.CharField(max_length=50)


class OP_LOG(models.Model):

    SN = models.CharField(max_length=50)
    admin = models.CharField(max_length=50)
    OP = models.CharField(max_length=50)
    OPTime = models.CharField(max_length=50)
    Object = models.CharField(max_length=50)
    Param1 = models.CharField(max_length=50)
    Param2 = models.CharField(max_length=50)
    Param3 = models.CharField(max_length=50)
    company = models.CharField(max_length=50)


class USER_INFO(models.Model):

    Pin = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Pri = models.CharField(max_length=50)
    Pass_Word = models.CharField(max_length=50)
    Card = models.CharField(max_length=50)
    Time_Zones = models.CharField(max_length=50)
    Acc_Group = models.CharField(max_length=50)
    Verify = models.CharField(max_length=50)

class FINGER_TMP(models.Model):

    Pin = models.CharField(max_length=50)
    FID = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    Valid = models.CharField(max_length=50)
    TMP = models.CharField(max_length=4000)


class ATT_ALL(models.Model):

    SN = models.CharField(max_length=50)
    ErrorDelay = models.CharField(max_length=50)
    Delay = models.CharField(max_length=50)
    TransTimes = models.CharField(max_length=50)
    TransInterval = models.CharField(max_length=50)
    TransFlag = models.CharField(max_length=50)
    Realtime = models.CharField(max_length=50)
    Encrypt = models.CharField(max_length=50)
    ServerVer = models.CharField(max_length=50)

    def __str__(self):
        return 'SN='+self.SN+'/tDelay='+self.Delay+'/tTransTimes='+self.TransTimes+'/tTransInterval='+self.TransInterval\
               +'/tTransFlag='+self.TransFlag+'/tRealtime='+self.Realtime+'/tRealtime='+self.Realtime\
                +'/tEncrypt=' + self.Encrypt+'/tServerVer='+self.ServerVer


class Device_Command(models.Model):
    CMD = models.CharField(max_length=50)

    def __str__(self):
        return self.CMD










