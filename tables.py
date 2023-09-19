from prettytable import PrettyTable
import re

def draw_projects_table(projects):
    projects_table = PrettyTable()
    projects_table.field_names = [" ","Z1","Z2","Z3","Z4"]
    for i in range(len(projects)):
        row = []
        row.append(projects[i].name)
        for j in range(len(projects[i].states)):
            row.append(projects[i].states[j])
        projects_table.add_row(row)
    print(projects_table)

def drawVotingTable(projects):
    voting_table = PrettyTable()
    voting_table.field_names = [" ","Вальд","Сэвидж","Гурвиц","Байес","Лаплас"]
    for i in range(len(projects)):
        row = []
        row.append(projects[i].name)
        attributes = vars(projects[i])
        for attribute in attributes:
            if re.search(r'optimal',attribute):
                if attributes[attribute] == True:
                    row.append("+")
                else:
                    row.append(" ")
        voting_table.add_row(row)
    print(voting_table)
