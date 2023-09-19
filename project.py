import re

class Project:
    def __init__(self, name: str, states: list):
        self.name = name
        self.states = states
        self.wald_optimal = False
        self.savidge_optimal = False
        self.gurvitz_optimal = False
        self.bayes_optimal = False
        self.laplas_optimal = False

    def numOptimalCriteria(self):
        numOptimalCriteria = 0
        attributes = vars(self)
        for attribute in attributes:
            if re.search(r'optimal',attribute) and (attributes[attribute] != False):
                numOptimalCriteria+=1
        return numOptimalCriteria









