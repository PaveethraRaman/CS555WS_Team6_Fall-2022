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
    CorrespondingEntries(famListData, indiListData)
    

fileInput= r'C:\Users\dheer\Desktop\Agile\Family.ged'
main(fileInput)