collecte = [{'delay': 5, 'hum': 18.2577, 'temp': 25.0832},
           {'delay': 5, 'hum': 17.1133, 'temp': 25.0725},
           {'delay': 5, 'hum': 17.1743, 'temp': 25.0618},
           {'delay': 5, 'hum': 17.1133, 'temp': 25.051}]
print(collecte)
cltHumidity = 0.0
cltTemperature = 0.0
i = 0

while i <= (len(collecte) - 1):
    # direct access to specific key to get corresponding values
    cltHumidity += collecte[i].get('hum')
    cltTemperature += collecte[i].get('temp')
    i += 1
moyHumidity = round(cltHumidity / len(collecte), 1)
moyTemp = round(cltTemperature / len(collecte), 1)

print(moyTemp)
print(moyHumidity)
