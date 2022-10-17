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
	

#User Story 12
#This function is to show the data if the Mother is less than 60 years older than her children and father should be less than 80 years older than his children

def parentsNotTooOld(individualList, familyList):
    list1 = []
    for i in familyList:
        if(i[5] != []):
            mother_age = getAgeByID(individualList, i[2])
            father_age = getAgeByID(individualList, i[1])
            for j in i[5]:
                child_age = getAgeByID(individualList, j)
                if(mother_age - child_age >= 60):
                    list1.append(i[2])
                    print( + i[2] + " Mother is 60 years or more older than her child " + j)
                if(father_age - child_age >= 80):
                    list1.append(i[1])
                    print(+ i[1] + " Father is 80 years or more older than his child " + j)
    if(len(list1) == 0):
        print("Both mother and father are not too old")
    else:
        print("List of aged parents when  compared to their children: ")
        print(list1)


        

def getAgeByID(ind_list, id):
    d_flag = 0
    for i in ind_list:
        if(i[0] == id):
            b_date = i[3]
            m = b_date.split('-')
            b_year = int(m[0])
            b_month = int(m[1])
            b_date = int(m[2])
            if(i[4] != 0):
                d_date = i[4]
                d_flag = 1
    if(d_flag == 1):
        m = d_date.split('-')
        d_year = int(m[0])
        d_month = int(m[1])
        d_date = int(m[2])
        return d_year - b_year - ((d_month, d_date) < (b_month, b_date))
    c_date = currentDate().split('-')
    c_year = int(c_date[0])
    c_month = int(c_date[1])
    c_date = int(c_date[2])
    return c_year - b_year - ((c_month, c_date) < (b_month, b_date))

	
#UserStory 13
#This function is to show the data if the Birth dates of siblings are more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)

def SiblingsSpacing(famListData, indiListData):
    for i in famListData:
        if(i[5] != [] and len(i[5]) > 1):
            siblingPairs = list(iter.combinations(i[5], 2))
            for j in siblingPairs:
                siblings_months = abs(difference_months(getBirthDateByID(indiListData, j[0]), getBirthDateByID(indiListData, j[1])))
                siblings_days = abs(difference_days(getBirthDateByID(indiListData, j[0]), getBirthDateByID(indiListData, j[1])))
                if(siblings_months <= 8 and siblings_days >= 3):
                    dateList.append(j)
                    print("Siblings " + j[0] + " and " + j[1] + " have their birth dates eight months apart")
                if(siblings_months == 0 and siblings_days >= 2):
                    dateList.append(j)
                    print("Siblings " + j[0] + " and " + j[1] + " have their birth days 2 or more days apart")
    if(len(dateList)==0):
        print("All the Siblings have correct spacing")
    else:
        print("The following Sibling pairs have bad birth date spacings")
        print(dateList)

#calculate difference in months
def difference_months(dateData1, dateData2):
    temp1 = dateData1.split('-')
    temp2 = dateData2.split('-')
    ndateData1 = datetime.date(int(temp1[0]), int(temp1[1]), int(temp1[2]))
    ndateData2 = datetime.date(int(temp2[0]), int(temp2[1]), int(temp2[2]))
    return int((ndateData1 - ndateData2).days / 30.4)

#calculate difference in days
def difference_days(dateData1, dateData2):
    temp1 = dateData1.split('-')
    temp2 = dateData2.split('-')
    ndateData1 = datetime.date(int(temp1[0]), int(temp1[1]), int(temp1[2]))
    ndateData2 = datetime.date(int(temp2[0]), int(temp2[1]), int(temp2[2]))
    return abs(int((ndateData1 - ndateData2).days))
	


	

#User Story 15
#This function is to show the data if the are fewer than 15 siblings in a family

def lessThan15Siblings(famListData):
    siblingList = []
    for i in famListData:
        if(len(i[5]) >= 15):
            siblingList.append(i[0])
            print("Family with id " + i[0] + " has 15 or more siblings.")
    if(len(siblingList)==0):
        print("No families with 15 or more siblings.")
    else:
        print("Families with 15 or more siblings: ")
        print(siblingList)
        
#User Story 16
#This function is to show the data if the all male members of a family should have the same last name

def maleLastNames(list_indi, list_fam):
    list1 = []
    for j in list_fam:
        male_names = []
        male_names.append(getLastNameByID(list_indi, j[1]))
        if(j[5] != []):
            for k in j[5]:
                if(getSexByID(list_indi, k) == 'M'):
                    male_names.append(getLastNameByID(list_indi, k))
        if(len(set(male_names)) != 1):
            list1.append(j[0])
            print('"Family ' + j[0] + ' has one or more male members with different last name(s).')
    if(len(list1)==0):
        print("Males in all families have the same last name.")
    else:
        print("Families which have one or more male members with different last name(s): ")
        print(list1)


def getSexByID(list_indi, id):
    for i in list_indi:
        if(i[0] == id):
            return i[2]

#parsing the gedcom file 
def getcomParse(file_name):
    f = open(file_name,'r')
    indiValue = 0
    famValue = 0
    indiListData = []
    famListData = []
    indiData = individualList()
    famData = familyList()
    for line in f:
        s = line.split()
        if(s != []):
            if(s[0] == '0'):
                if(indiValue == 1):
                    indiListData.append(indiData)
                    indiData = individualList()
                    indiValue = 0
                if(famValue == 1):
                    famListData.append(famData)
                    famData = familyList()
                    famValue = 0
                if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(s[2] == 'INDI'):
                        indiValue = 1
                        indiData[0] = (s[1])
                    if(s[2] == 'FAM'):
                        famValue = 1
                        famData[0] = (s[1])
            if(s[0] == '1'):
                if(s[1] == 'NAME'):
                    indiData[1] = s[2] + " " + lastName(s[3])
                if(s[1] == 'SEX'):
                    indiData[2] = s[2]
                if(s[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = s[1]
                if(s[1] == 'FAMS'):
                    indiData[5].append(s[2])
                if(s[1] == 'FAMC'):
                    indiData[6] = s[2]
                if(s[1] == 'HUSB'):
                    famData[1] = s[2]
                if(s[1] == 'WIFE'):
                    famData[2] = s[2]
                if(s[1] == 'CHIL'):
                    famData[5].append(s[2])
            if(s[0] == '2'):
                if(s[1] == 'DATE'):
                    date = s[4] + " " + s[3] + " " + s[2]
                    if(date_id == 'BIRT'):
                        indiData[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        indiData[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        famData[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        famData[4] = convertDateFormat(date)
    return indiListData, famListData


def main(file_name):
    indiListData, famListData = getcomParse(file_name)
    indiListData.sort()
    famListData.sort()
    

    for i in indiListData:
        table = PrettyTable(["ID", "Name" , "Sex", "Birth Date", "Death Date" , "Child" , "Spouse"])
        table.add_row([i[0] , i[1], i[2],i[3], i[4] , i[5] , i[6]])
        print (table)
    for i in famListData:
        table1 = PrettyTable(["ID", "Husband's Name" , "Wife's Name"])
        table1.add_row([i[0] , getNameUsingID(indiListData,i[1]) , getNameUsingID(indiListData,i[2]) ])
        print (table1)

    birthBeforeDeathOfParents(indiListData, famListData)
    marriageAfter14(indiListData, famListData)
    noBigamy(indiListData, famListData)
    parentsNotTooOld(indiListData, famListData)
    SiblingsSpacing(famListData, indiListData)
    multipleBirthslessThan5(indiListData, famListData)
    lessThan15Siblings(famListData)
    maleLastNames(indiListData, famListData)
    
    

fileInput= r'C:\Users\dheer\Desktop\Agile\Family.ged'
main(fileInput)



  
