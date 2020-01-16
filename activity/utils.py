def arrayEncode(data):
    StringList = list(str(x) for x in data)
    StringData = ",".join(StringList)
    return StringData

def arrayDecode(stringData):
    StringList = stringData.split(',')
    data = list(float(x) for x in StringList)
    return data
    


