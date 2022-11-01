import datetime
from prettytable import PrettyTable

dateList=[]
#getting name using IDs
def getNameUsingID(individualList, ID):
    for i in individualList:
        if(i[0] == ID):
            return i[1]
#For the individual list

def individualList():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist

	
#For the family list
def familyList():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

#get last name
def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp

#get today's date
def currentDate():
    currDate = str(datetime.date.today())
    
    return currDate

def GetAllIDsList(list1):
    all_ids = []
    for i in range(len(list1)):
        all_ids.append(list1[i][0])
    all_ids.sort()
    
    return all_ids

def getNameFromID(id, indiList):
    for y in range(len(indiList)):
        indi = indiList[y]

        if(indi[0] == id):
            return indi[1]

def GetNameDOB(id, indiList):
    for i in range(len(indiList)):
        if( indiList[i][0] == id):
            return [indiList[i][1], indiList[i][3]]


#Converting date into a standard format
def convertDateFormat(date):
    temp = date.split()
    if(temp[1] == 'JAN'): temp[1] = '01'
    if(temp[1] == 'FEB'): temp[1] = '02'
    if(temp[1] == 'MAR'): temp[1] = '03'
    if(temp[1] == 'APR'): temp[1] = '04'
    if(temp[1] == 'MAY'): temp[1] = '05'
    if(temp[1] == 'JUN'): temp[1] = '06'
    if(temp[1] == 'JUL'): temp[1] = '07'
    if(temp[1] == 'AUG'): temp[1] = '08'
    if(temp[1] == 'SEP'): temp[1] = '09'
    if(temp[1] == 'OCT'): temp[1] = '10'
    if(temp[1] == 'NOV'): temp[1] = '11'
    if(temp[1] == 'DEC'): temp[1] = '12'
    if(temp[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp[2] = '0' + temp[2]
    return (temp[0] + '-' + temp[1] + '-' + temp[2])

dateList = []
todayDate = currentDate()


#User story 17 
def NoMarriagesToDescendents(family_list):
    married_descendents = []
    length_of_families = len(family_list)

    for i in range(length_of_families):
        each_family = family_list[i]
        parents = [each_family[1], each_family[2]]
        descendents = each_family[5]
        
        for parent in parents:
            for child in descendents:
                for x in range(length_of_families):
                    fam = family_list[x]
                    if (fam[1] == parent) or (fam[2] == parent):
                        if (fam[1]==child) or (fam[2]==child):
                            married_descendents.append([parent,child])
        
    if(len(married_descendents)==0):
        print("No parents married their descendents")
    else:
            print("Parents married their descendents ", married_descendents)

#User story 18
def SiblingsNotMarry(familyList):

    siblings_married = []
    length_of_families = len(familyList)
    for i in range(length_of_families):
        family = familyList[i]

        siblings = family[-1]
       

        if(len(siblings)>1):
            for i in range(len(siblings)):
                sib1 = siblings[i]
                for j in range(i+1, len(siblings)):
                    sib2 = siblings[j]

                    for x in range(len(familyList)):
                        fam1 = familyList[x]
                        if(fam1[1]==sib1) or (fam1[2] == sib1):
                            if(fam1[1]==sib2) or (fam1[2] == sib2):
                                siblings_married.add([sib1, sib2])
    
    if(len(siblings_married) > 0):
        print("Siblings married")
        print(siblings_married)
    else:
        print("No siblings were married")
