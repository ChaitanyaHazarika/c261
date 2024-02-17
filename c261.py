def visitors():
    counterReadFile = open('count.txt', 'r')
    visitorsCount = int(counterReadFile.read())
    counterReadFile.close()
    visitorsCount += 1
    counterWriteFile  = open('count.txt', 'w')
    counterWriteFile.write(str(visitorsCount))
    counterWriteFile.close()


    print('Total Visitors: ', visitorsCount)

visitors()

def covidStats():
    countryName = input('Enter Country Nam: ')
    coronaData = 'https://covidstats-sdbd.onrender.com/?country=' + countryName
    print(coronaData)


covidStats()

