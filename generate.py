from random import randint

class Subject():

    def __init__(self, name, periods_per_week, span):
        self.name = name
        self.periods_per_week = periods_per_week
        self.span = span

class Population():
    def __init__(self,subject_obj_list):
        self.chromosome = []
        self.subject_obj_list = subject_obj_list
        total_periods = 15
        number_of_subject = 5

        for i in range(100):
            self.chromosome.append(Chromosome(subject_obj_list, total_periods, number_of_subject))
        
        self.chromosome[0].printTable()


class Chromosome():

    def __init__(self, subjects_obj_list, total_periods, number_of_subject):
        self.subjects_obj_list = subjects_obj_list
        self.total_periods = total_periods
        self.number_of_subject = number_of_subject
        self.gene = []

        remaining_periods = self.total_periods
        while remaining_periods > 0:
            r = randint(0,number_of_subject-1)
            if subjects_obj_list[r].periods_per_week > 0:
                for i in range(subjects_obj_list[r].span):
                    self.gene.append(Gene(subjects_obj_list[r].name))
                remaining_periods -= 1
            else:a
                self.gene.append(Gene("N/A"))

    def getFitness(self):
        fitness = 1
        for i in range(self.total_periods):
            pass

    def printTable(self):
        for i in range(self.total_periods):
            print(self.gene[i].subject, end=" ")
            if i% 7 == 0:
                print()

class Gene():

    def __init__(self, subject):
        self.subject = subject
    
    def getSubject(self):
        return self.subject

def main():
    subject_name = ["OOAD","MC","IP","CD","ST"]
    subject_hours = [3,3,3,3,3]

    subject_obj_list = []
    for i in range(5):
        s = Subject(subject_name[i], subject_hours[i], 1)
        subject_obj_list.append(s)
    
    for i in subject_obj_list:
        print(i.name)

    p = Population(subject_obj_list)

main()
