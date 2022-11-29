#userstory 29

def DeceasedIndividuals(indiList):
    length_of_indiList = len(indiList)
    died_persons = []

    for i in range(0, length_of_indiList):
        individual = indiList[i]
    
        if ( individual[4] != 0):
            died_persons.append(individual[0])
    
    print("Deceased Individuals are")
    for i in range(len(died_persons)):
        print(getNameFromID(died_persons[i], indiList))
    
#userstory 30 
def LivingMarried(famList, indiList):
    length_of_famList = len(famList)
    length_of_indiList = len(indiList)

    alive_individuals = set()


    for i in range(0, length_of_famList):
        family = famList[i]
        indi1 = family[1]
        indi2 = family[2]

        person1_alive = isAlive(indi1, indiList)
        person2_alive = isAlive(indi2, indiList)
        
        if (person1_alive):
            alive_individuals.add(indi1)
        if (person2_alive):
            alive_individuals.add(indi2)
    
    print("Alive married individuals")
    for person in alive_individuals:
        print(getNameFromID(person, indiList))
