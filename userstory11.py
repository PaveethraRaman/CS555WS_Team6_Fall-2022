import datetime
def currentDate():
    currDate = str(datetime.date.today())
    return currDate
#Converting date into a standard format
def convertDateFormat(date):
    temp = date.split()
    if(temp[1] == 'JAN'): temp[1] = '01';
    if(temp[1] == 'FEB'): temp[1] = '02';
    if(temp[1] == 'MAR'): temp[1] = '03';
    if(temp[1] == 'APR'): temp[1] = '04';
    if(temp[1] == 'MAY'): temp[1] = '05';
    if(temp[1] == 'JUN'): temp[1] = '06';
    if(temp[1] == 'JUL'): temp[1] = '07';
    if(temp[1] == 'AUG'): temp[1] = '08';
    if(temp[1] == 'SEP'): temp[1] = '09';
    if(temp[1] == 'OCT'): temp[1] = '10';
    if(temp[1] == 'NOV'): temp[1] = '11';
    if(temp[1] == 'DEC'): temp[1] = '12';
    if(temp[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp[2] = '0' + temp[2]
    return (temp[0] + '-' + temp[1] + '-' + temp[2])

todayDate = currentDate()
#get today's date



def getLastName(str):
    tem=''
    for i in str:
        if(i != '/'):
            tem += i
    return tem
def famList():
    p_list = [0 for i in range(6)]
    p_list[5] = []
    return p_list
def indiList():
    p_list = [0 for i in range(7)]
    p_list[5] = []
    return p_list

#User Story 11
#This function is to show the data if marriage has occured during marriage to another spouse

def getSpouseNameById(famListData, famId, spouseId):
    for i in famListData:
        if(i[0] == famId):
            if(i[1] == spouseId):
                return i[2]
            if(i[2] == spouseId):
                return i[1]

def getDivorceDateById(famListData, famId):
    for i in famListData:
        if(i[0] == famId):
            if(i[4] != 0):
                return i[4]
def getMarriageDateById(famListData, id):
    for i in famListData:
        if(i[0] == id):
            return i[3]
def getDeathDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            if(i[4] != 0):
                return i[4]


def noBigamy(indiListData, famListData):
    noBigamyList = []
    for i in indiListData:
        family = []
        t = []
        if(len(i[5]) > 1):
            selfId = i[0]
            for j in i[5]:
                t.append(getMarriageDateById(famListData, j))
                t.append(j)
                t.append(getSpouseNameById(famListData, j, selfId))
                t.append(getDivorceDateById(famListData, j))
                t.append(getDeathDateByID(indiListData, getSpouseNameById(famListData, j, selfId)))
                family.append(t)
                t = []
            family.sort()
            for z in range(1, len(family)):
                if(family[z-1][3] == None and family[z-1][4] == None):
                    noBigamyList.append(selfId)
                    print("Person with id " + selfId + " is married to person " + family[z][2] + " with family id " + family[z][1] + " while  still in marriage with person with id " + family[z-1][2] + " in family " + family[z-1][1])
                else:
                    if(family[z-1][3] != None):
                        if(family[z][0] < family[z-1][3]):
                            noBigamyList.append(selfId)
                            print("Person with id" + selfId + " is married to person " + family[z][2] + " with family id " + family[z][1] + " before filing divorce with spouse " + family[z-1][2] + " in family " + family[z-1][1])
                    if(family[z-1][4] != None):
                        if(family[z][0] < family[z-1][4]):
                            noBigamyList.append(selfId)
                            print("Person with id " + selfId + " is married to person " + family[z][2] + " with family id  " + family[z][1] + " before spouse's death" + family[z-1][2] + " in family " + family[z-1][1])
    if(len(noBigamyList) == 0):
        print("The individuals in the Family tree are not involved in Bigamy.")
    else:
        print("The individual(s) involved in Bigamy: ")
        print(noBigamyList)

def parseTheFile(fileName):
    f = open(fileName,'r')
    indiOn = 0
    famOn = 0
    indi = indiList()
    fam = famList()
    listIndi = []
    listFam = []  
    for line in f:
        str = line.split()
        if(str != []):
            if(str[0] == '0'):
                if(indiOn == 1):
                    listIndi.append(indi)
                    indi = indiList()
                    indiOn = 0
                if(famOn == 1):
                    listFam.append(fam)
                    fam = famList()
                    famOn = 0
                if(str[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(str[2] == 'INDI'):
                        indiOn = 1
                        indi[0] = (str[1])
                    if(str[2] == 'FAM'):
                        famOn = 1
                        fam[0] = (str[1])
            if(str[0] == '1'):
                if(str[1] == 'NAME'):
                    indi[1] = str[2] + " " + getLastName(str[3])
                if(str[1] == 'SEX'):
                    indi[2] = str[2]
                if(str[1] == 'FAMS'):
                    indi[5].append(str[2])
                if(str[1] == 'FAMC'):
                    indi[6] = str[2]
                if(str[1] == 'HUSB'):
                    fam[1] = str[2]
                if(str[1] == 'WIFE'):
                    fam[2] = str[2]
                if(str[1] == 'CHIL'):
                    fam[5].append(str[2])
                if(str[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = str[1]
            if(str[0] == '2'):
                if(str[1] == 'DATE'):
                    date = str[4] + " " + str[3] + " " + str[2]
                    if(date_id == 'BIRT'):
                        indi[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indi[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        fam[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        fam[4] = convertDateFormat(date)
    return listIndi, listFam

def main(fileName):
    listIndi, listFam = parseTheFile(fileName)
    listIndi.sort()
    listFam.sort()
    noBigamy(listIndi, listFam)

fileInput= r'C:\Users\dheer\Desktop\Agile\Family.ged'
main(fileInput)