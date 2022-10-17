#importing packages
import datetime
from prettytable import PrettyTable
import itertools as iter


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

#getting last name data by id
def getLastNameByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            temp_name = i[1].split(' ')
            return temp_name[1]
        
	
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
	
		
#function to get the birth date
def getBirthDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            return i[3]
			
#Function to get the death date
def getDeathDateByID(indiListData, id):
    for i in indiListData:
        if(i[0] == id):
            if(i[4] != 0):
                return i[4]

#Function to get the marriage details by id				
def getMarriageByID(list_individual, id, dateOfMarriage):
    marriageDate = dateOfMarriage.split('-')
    yearOfMarriage = int(marriageDate[0])
    monthOfMarriage = int(marriageDate[1])
    dateOfMarriage = int(marriageDate[2])
    for i in list_individual:
        if(i[0] == id):
            dateOfBirth = i[3]
    birthDate = dateOfBirth.split('-')
    yearOfBirth = int(birthDate[0])
    monthOfBirth = int(birthDate[1])
    dateOfBirth = int(birthDate[2])
    return yearOfMarriage - yearOfBirth - ((monthOfMarriage, dateOfMarriage) < (monthOfBirth, dateOfBirth))


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

#UserStory 09
# This function is to show the data if the child is born before death of mother and before 9 months after death of father
def birthBeforeDeathOfParents(indiListData, famListData):
    for i in famListData:
        if(i[5] != []):
            for j in i[5]:
			
                childBirthDate= getBirthDateByID(indiListData, j)
                motherDeathDate = getDeathDateByID(indiListData, i[2])
                fatherDeathDate = getDeathDateByID(indiListData, i[1])

                if(motherDeathDate != None):
                    if(childBirthDate > motherDeathDate):
                        dateList.append(j)
                        print("Individual" + j + "was born after death of mother" + i[2])
                        if(fatherDeathDate != None):
                            if(childBirthDate > fatherDeathDate):
                                dateList.append(j)
                                print("Individual" + j + "was born after death of father" + i[1])
    if(len(dateList) == 0):
        print("There is no childrem  born after death of their parent's ")
    else:
        print(" These children born after death of their parent's ")
        print(dateList)

  
