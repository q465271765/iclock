from django.shortcuts import render
from django.http import HttpResponse
from test1.models import iclock, ATT_LOG, OP_LOG, USER_INFO, FINGER_TMP, ATT_ALL, Device_Command
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from functools import lru_cache
from test1.cache import Cache

# Create your views here.


def index(request):
        Device = Device_Command.objects.all()

        return render(request, 'index.html', {'Device': Device})


def uploadUserInfo(request):
    SN = request.GET['SN']
    language = request.GET['language']
    iclock.objects.create(SN=SN, language=language)

    return HttpResponse(str(SN+language))


@csrf_exempt
def devicecmd(request):

    d = {'ID': 'iiii', 'SN': '3292165100004', 'Return': 'VVVV', 'CMD': 'CHECK',
         'FILENAME': 'shellout.txt', 'Content': 'ssss'}

    if request.method == 'POST':
        SN = request.POST.get('SN')
        return HttpResponse(d)

cache = Cache()
global ID
ID = 1


def requestdate(*args):
    ID, Pin, Fid, CMD = args

    date = {'C:ID'+str(ID)+': DATA '+CMD+' PIN='+Pin+'.FID='+Fid}
    return date


def setrequest(request):
    Pin = str(request.GET.get('PIN'))
    Fid = str(request.GET.get('FID'))
    CMD = str(request.GET.get('CMD'))
    global ID
    ID = ID+1
    date = requestdate(ID, Pin, Fid, CMD)
    print('setrequest'+str(ID))
    cache.set(str(ID), date)
    print(cache.get(str(ID)))
    return HttpResponse('ok')


# def getrequest(request):
#     d = {'GET OPTION FROM': '3292165100005', 'Stamp': '82983982', 'OpStamp': '9238883', 'PhotoStamp': '9238833',
#          'ErrorDelay': '60', 'Delay': '30', 'TransTimes': '00:00;14:05', 'TransInterval': '1',
#          'TransFlag': 'AttLog', 'Realtime': '1', 'Encrypt': '0', 'ServerVer': '3.4.1 2010-06-07',
#          'ATTLOGStamp': '82983982 '}
#     c = {'C:ID125:DATA QUERY FINGERTMP PIN=1.FID=1'}
#     NUM = request.GET.get('NUM')
#     data = cache.get(NUM)
#     print(data)
#     return HttpResponse(c)


def getrequest(response):
    SN = response.GET.get('SN')
    cdata = cache.get(str(ID))
    print("getrequest" + str(cdata))
    if str(SN) in str(cdata):
        return HttpResponse(cdata)
    else:
        return HttpResponse('OK')




@csrf_exempt
def cdata(response):

        SN = response.GET.get('SN')
        if response.method == "GET":
            option = response.GET.get('options')
            if option == 'all':
                all = ATT_ALL.objects.filter(SN=SN)
                print(connection.queries)
            return HttpResponse(all)
        if response.method == "POST":
            body = str(response.body).split('\\t')
            table = response.GET.get('table')
            Stamp = response.GET.get("language")

        if table == 'ATTLOG':
                User_PIN = body[0].replace("b'", '')
                Verify_Time = body[1]
                Status = body[2]
                WorkCode = body[3]
                Verify_Type = body[4]
                Att_Info_Count = ATT_LOG.objects.filter(User_PIN=User_PIN).filter(Verify_Time=Verify_Time).count()
                if Att_Info_Count == 0:
                    try:
                        ATT_LOG.objects.create(SN=SN, User_PIN=User_PIN, Verify_Time=Verify_Time, Status=Status, Work_Code_ID=WorkCode, Verify_Type=Verify_Type)
                    except ATTLOGException:
                        raise 'INSERT ATTLOG ERROR'
                        return HttpResponse(-3)

        if table == 'OPERLOG': #上传日志
            if 'FP' in str(body): #指纹
                PIN, FID, Size,Valid, TMP = body
                PIN = PIN[PIN.find('=') + 1:]
                FID = FID[FID.find('=') + 1:]
                Size = Size[Size.find('=') + 1:]
                Valid = Valid[Valid.find('=') + 1:]
                TMP = TMP[TMP.find('=') + 1:]
                try:
                    Pin_Info_Count = USER_INFO.objects.filter(Pin=PIN).count()
                    if Pin_Info_Count == 0:
                        return HttpResponse(-9)
                    FINGER_TMP.objects.create(Pin=PIN, FID=FID, Size=Size, Valid=Valid, TMP=TMP)
                except OPERLOGException:
                    print('insert FINGER_TMP error')
                    return HttpResponse(-3)
            if 'USER' in str(body): #录入用户信息
                PIN, Name, Pri, Passwd, Card, Grp, TZ, Verify = body

                PIN = PIN[PIN.find('=') + 1:]
                Name = Name[Name.find('=') + 1:]
                Pri = Pri[Pri.find('=') + 1:]
                Passwd = Passwd[Passwd.find('=') + 1:]
                Card = Card[Card.find('=') + 1:]
                Grp = Grp[Grp.find('=') + 1:]
                TZ = TZ[TZ.find('=') + 1:]
                Verify = Verify[Verify.find('=') + 1:-3]
                try:
                        USER_INFO.objects.create(Pin=PIN, Name=Name, Pri=Pri, Pass_Word=Passwd, Card=Card, Acc_Group=Grp, Time_Zones=TZ, Verify=Verify)
                except OPERLOGException:
                    print('insert USER_INFO error')

            if 'OPLOG' in str(body):

                print('OPLOG')

        print(connection.queries)
        return HttpResponse('ok')


class ATTLOGException(Exception):
    pass


class OPERLOGException(Exception):
    pass
