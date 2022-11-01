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

#User story 21 
def Individual_gender_verification(husband_id, wife_id, indiList):
    husband_gender= False
    wife_gender = False
    
    for i in range(len(indiList)):
        individual = indiList[i]
        if(individual[0] == husband_id):
            if(individual[2]=='M'):
                husband_gender = True

        if(individual[0] == wife_id):
            if(individual[2] == 'F'):
                wife_gender = True
    
    return husband_gender& wife_gender

def CorrectGenderForRole(individual_list, family_list):
    incorrectGenderFamilies = []
    length_of_family_list = len(family_list)
    for i in range(length_of_family_list):
        fam = family_list[i]
        hus = fam[1]
        wife1 = fam[2]
        if(not(Individual_gender_verification(hus, wife1, individual_list))):
            incorrectGenderFamilies.append(fam)
    
    if(len(incorrectGenderFamilies)>0):
        print("Incorrect gender families")
        print(incorrectGenderFamilies)
    else:
        print("There are no families with incorrect gender")

#User story 22 
def UniqueIDS(individual_list, family_list):
    non_unique_individual_ids = []
    non_unique_family_ids = []
    all_individial_ids = GetAllIDsList(individual_list)
    all_family_ids = GetAllIDsList(family_list)

    for i in range(len(all_individial_ids)):
        id_to_count = individual_list[i][0]
        if (all_individial_ids.count(id_to_count) > 1):
            non_unique_individual_ids.append(id_to_count)
    
    
    for i in range(len(all_family_ids)):
        id_to_count = individual_list[i][0]
        if (all_family_ids.count(id_to_count) > 1):
            non_unique_family_ids.append(id_to_count)

    if(len(non_unique_family_ids)>1):
        print("Non unique Family IDS =", non_unique_family_ids)
    else:
        print("There are no non unique family ids")
    
    if(len(non_unique_individual_ids)>1):
        print("Non unique individual IDS =", non_unique_individual_ids)
    else:
        print("There are no non unique individual ids")
	
#User story 23
def UniqueNameAndBirthDate(individual_list):
    non_unique = []
    length_of_individual_list = len(individual_list)

    for i in range(length_of_individual_list):
        individual = individual_list[i]
        name = individual[1]
        birthdate = individual[3]

        count = 0

        for j in range(length_of_individual_list):
            if (individual == individual_list[j][1]):
                if(birthdate == individual_list[j][3]):
                    count  = count + 1
                else:
                    count = count+1
            
        if count > 1:
            non_unique.appen(individual[1])
    
    if(len(non_unique)>0):
        print("Individual with more than ine birthdate")
        print(non_unique)
    else:
        print("There are no individuals with more than one birth date and name")

#User story 24
def UniqueSpouse(family_list, indiList):
    non_unique = []
    length_of_family_list = len(family_list)

    for i in range(length_of_family_list):
        count = 0
        family = family_list[i]

        spouse = family[2]
        family_id = family[0]

        for j in range(length_of_family_list):
            fam = family_list[j]
            if(fam[2] == spouse):
                if(fam[0] == family_id):
                    count = count + 1
                else:
                    count = count+1
        
        if(count>1):
            spouse_name = getNameFromID(spouse, indiList)
            non_unique.append([family_id, spouse_name])
    
    if(len(non_unique)>0):
        print("Spouses beloging to different families are")
        for x in range(len(non_unique)):
            print('Family = ', non_unique[x][0], "Spouse = ", non_unique[x][1])
    else:
        print("Each spouse is belonging to a single family")


