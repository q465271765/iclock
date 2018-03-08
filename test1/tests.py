from io import StringIO


f = StringIO()


def writeStringIO():

    f.write('hi')
    f.write('python')
    print(f.getvalue())
    return f


def getStringIO():

    print('11'+f.getvalue())
    return f.getvalue

writeStringIO()
getStringIO
