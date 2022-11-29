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

#UserStory 26

Individual_dict = {}

def IsIndividualInIndiList(individual, indiList):
    if(Individual_dict[individual] == False):
        for i in range(len(indiList)):
            indi = indiList[i]
            if(indi[0] == individual):
                Individual_dict[individual] = True
            


def CorrespondingEntries(familyList, indiList):

    length_of_famList = len(familyList)
    length_of_individual_list = len(indiList)

    #create a empty dictionary for all the individuals
    

    for i in range(0, length_of_individual_list):
        individual = indiList[i]
        individual_id = individual[0]
        # set individual to false
        Individual_dict[individual_id] = False
    

    # go through the family List
    for i in range(0, length_of_famList):
        family = familyList[i]

        parent1 = family[1]
        parent2 = family[2]

        children = family[5]

        IsIndividualInIndiList(parent1, indiList)
        IsIndividualInIndiList(parent2, indiList)

        for ch in range(len(children)):
            IsIndividualInIndiList(children[ch], indiList)

    
    #get all the keys of a dictionary
    indi_keys = list(Individual_dict.keys())

    individuals_not_in_any_families = []
    for i in range(0, len(indi_keys)):
        if(Individual_dict[indi_keys[i]] == False):
            individuals_not_in_any_families.append(indi_keys[i])   

    if(len(individuals_not_in_any_families)>0):
        print("Individuals not in any families are ")
        for indivi in individuals_not_in_any_families:
            print(indivi)
    else:
        print('There are no individuals that doesnot belong to any family')

# userstory 28

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
