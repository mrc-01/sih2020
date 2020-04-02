def arrayEncode(data):
    StringList = list(str(x) for x in data)
    StringData = ",".join(StringList)
    return StringData

def arrayDecode(stringData):
    StringList = stringData.split(',')
    data = list(float(x) for x in StringList)
    return data
    
def generateUniqueID():
    import uuid 
    id = uuid.uuid1() 
    return id.hex

def sendSMS(number, message):
    import requests
        
    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message='{}'&language=english&route=p&numbers={}".format(message,number)
    headers = {
         'authorization': "DZK04NpM6lybjvSkzs5LmuVFQ7Ag1PCEqJrRcT2fdG9oxHOUeB3tM6BznlZaU9j24Gke7r0gmvNPcfCV",
         'Content-Type': "application/x-www-form-urlencoded",
         'Cache-Control': "no-cache",
     }
         
    response = requests.request("POST", url, data=payload, headers=headers)
         
    # print(response.text)
    # print(payload)