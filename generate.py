from random import randint

class Subject():

    def __init__(self, name, periods_per_week, span):
        self.name = name
        self.periods_per_week = periods_per_week
        self.span = span

class Population():
    def __init__(self):
        self.chromosome = []

        for i in range(100):
            chromosome.append(Chromosome(subjects_obj_list, total_periods, number_of_subject))


class Chromosome():

    def __init__(self, subjects_obj_list, total_periods, number_of_subject):
        self.subjects_obj_list = subjects_obj_list
        self.total_periods = total_periods
        self.number_of_subject = number_of_subject
        self.gene = []

        remaining_periods = self.total_periods
        while remaining_periods > 0:
            r = random.randint(0,number_of_subject)
            if subjects_obj_list[r].periods_per_week > 0:
                for i in range(subjects_obj_list[r].span):
                    self.gene.append(Gene(subjects_obj_list[r].name))
                remaining_periods -= 1

    def getFitness(self):
        fitness = 1
        for i in range(self.total_periods):

class Gene():
    
    def __init__(self, subject):
        self.subject = subject
    
    def getSubject(self):
        return self.subject

