from ast import Or
import datetime
from xmlrpc.client import DateTime

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

def getNameFromID(id, indiList):
    for y in range(len(indiList)):
        indi = indiList[y]

        if(indi[0] == id):
            return indi[1]
    

def getDOB(indi, indiList):
    for i in range(len(indiList)):
        individual = indiList[i]

        if(individual[0] == indi):
            date_of_birth = individual[3]
            year,month,date = date_of_birth.split("-")
            return datetime.date(int(year),int(month),int(date))
    

def OrderSiblingsByAge(famList, indiList):
    length_of_famList = len(famList)

    for i in range(0, length_of_famList):
        family = famList[i]

        siblings = family[5]

        siblings_with_age = []
        
        if(len(siblings)>0):
            if(len(siblings)>1):

                for x in range(0, len(siblings)):
                    child = siblings[x]
                    child_DOB = getDOB(child, indiList)
                    siblings_with_age.append([child, child_DOB])
                
                for j in range(0, len(siblings)):
                    child1 = siblings_with_age[j]

                    for k in range(j+1, len(siblings)):
                        child2 = siblings_with_age[k]

                        if child1[1] > child2[1]:
                            siblings_with_age[j], siblings_with_age[k] = siblings_with_age[k], siblings_with_age[j]
                
            else:
                #there is only one child in fam
                child = siblings[0]
                childDOB = getDOB(child, indiList)
                siblings_with_age.append([child, childDOB])
            
        print("Siblings with Age in family ", family[0] )
        for i in range(len(siblings_with_age)):
            print("Name = ", getNameFromID(siblings_with_age[i][0], indiList),",","Date of Birth = ", siblings_with_age[i][1])



def isAlive(individual, indiList):
    
    for k in range(0, len(indiList)):
        indi = indiList[k]
        if ( individual ==  indi[0]):
            death_date = indi[4]
           
            if death_date != 0:
                return False
            else:
                return True

def getAge(DOB):
    #age =  todayDate- DOB
    today_year, today_month, today_date = todayDate.split("-")
    dob_year = DOB.year
    age = int(today_year) -  int(dob_year)
    return age
   


    
# Living Singles
def LivingSingles(famList, indiList):
    length_of_individual_list = len(indiList)
    length_of_family_list = len(famList)

    Singles = set()

    for i in range(0, length_of_individual_list):
        individual = indiList[i]

        individual_is_alive = isAlive(individual[0], indiList)
        individual_DOB = getDOB(individual[0], indiList)
        individual_age = getAge(individual_DOB)
        
        if((individual_is_alive) and individual_age > 30):

            isSingle = True
            for j in range(0, length_of_family_list):
                family = famList[j]
                parent1 = family[1]
                parent2 = family[2]
                
                if ((parent1 == individual[0]) or (parent2 == individual[0])):
                    isSingle = False
            
            if (isSingle == True):
                Singles.add(individual[0])
    
    print("Living Singles are")
    for person in Singles:
        print(person, getNameFromID(person, indiList))


def ListOrphans(famList, indiList):
    length_of_individual_list = len(indiList)
    length_of_family_list = len(famList)

    Orphans = set()

    for i in range(length_of_family_list):
        family = famList[i]

        parent1 = family[1]
        parent2 = family[2]

        children= family[5]

        parent1_isAlive = isAlive(parent1, indiList)
        parent2_isAlive = isAlive(parent2, indiList)

        if((parent1_isAlive == False) and (parent2_isAlive == False)):
            # both parents are not alive

            for c in range(0, len(children)):
                child = children[c]
                child_dob = getDOB(child, indiList)
                child_age = getAge(child_dob)
              
                if(child_age < 18):
                    Orphans.add(child)


    if(len(Orphans) > 0):
        print("Orphans are")
        for person in Orphans:
            print(getNameFromID(person, indiList))
    else:
        print("There are no orphans in the family tree")


def ListCouplesWithLargeAgeDiff(famList, indiList):
    length_of_individual_list = len(indiList)
    length_of_family_list = len(famList)


    couples_greater = []

    for i in range(0, length_of_family_list):
        family = famList[i]
        person1 = family[1]
        person2 = family[2]

        person1_dob = getDOB(person1, indiList)
        person2_dob = getDOB(person2, indiList)

        person1_age = getAge(person1_dob)
        person2_age = getAge(person2_dob)
        print(person1_age, person2_age)
        if((person1_age >= 2 * person2_age)):
            couples_greater.append([person1, person2])
        elif((person2_age >= 2*person1_age)):
            couples_greater.append([person1, person2])
    
    if(len(couples_greater)>0):
        print("Couples with twice age diff")
        for couple in couples_greater:
            print(couple)
    else:
        print("There are no couples with twice age difference")

#Recent Births
def RecentBirths(indiList):
    today_date = datetime.date.today()
    length_of_individual_list = len(indiList)

    RecentBirthIndividuals = set()
    for i in range(0, length_of_individual_list):
        individual = indiList[i]

        individual_DOB = getDOB(individual[0], indiList)
        difference = today_date - individual_DOB
        if( difference.days <30):
            RecentBirthIndividuals.add(individual[0])
    
    if(len(RecentBirthIndividuals) > 0):

        for person in RecentBirthIndividuals:
            print(getNameFromID(person, indiList))
    else:
        print("There are no persons born recently in 30days")



        

        



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
    # print("individual list -> ", indiListData);
    # print("Family List data -> ", famListData);
    RecentBirths(indiListData)
    

fileInput= r'C:\Users\dheer\Desktop\Agile\Family.ged'
main(fileInput)