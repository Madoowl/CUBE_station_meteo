import datetime
import json
result = [(111, None,  16.8, 23.8), (111, None,  16.8, 23.8)]
#  , (111, 1, datetime.datetime(2021, 2, 11, 9, 38, 12, 315178), 16.2, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 9, 44, 55, 477170), 15.4, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 9, 45, 22, 236623), 15.7, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 47, 46, 780874), 15.4, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 48, 43, 583111), 15.1, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 51, 55, 323960), 14.4, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 9, 52, 24, 21316), 14.4, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 9, 52, 54, 797466), 14.4, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 55, 11, 36753), 14.6, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 9, 55, 36, 161823), 14.2, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 56, 5, 834632), 14.4, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 56, 32, 80582), 14.4, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 9, 57, 35, 762608), 14.6, 23.6), (111, 1, datetime.datetime(2021, 2, 11, 10, 1, 58, 611040), 14.7, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 10, 2, 22, 529661), 14.6, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 10, 2, 46, 754393), 14.4, 23.5), (111, 1, datetime.datetime(2021, 2, 11, 10, 3, 12, 248266), 14.5, 23.5)]

i =0
Ret = {}
for data in result:
    try:
        jData = json.dumps(data)
        Ret[i] = jData
        i += 1
    except:
        pass
print(Ret)

# class Req(pData):
#     pass