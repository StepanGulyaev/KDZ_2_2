from project import Project
from tables import *
from criterias import *

x1 = Project("X1",[5,2,8,5])
x2 = Project("X2",[4,5,9,4])
x3 = Project("X3",[4,1,7,7])
x4 = Project("X4",[4,6,9,7])
x5 = Project("X5",[1,3,4,3])
x6 = Project("X6",[0,2,3,2])
x7 = Project("X7",[1,2,4,2])
x8 = Project("X8",[4,3,1,0])

projects = []
projects.extend([x1,x2,x3,x4,x5,x6,x7,x8])

if __name__ == '__main__':
    draw_projects_table(projects)
    print("Вальд-эффективные решения: ",end='')
    print(*map(lambda x: x.name,getWaldEffective(projects)), sep=",")
    print("Сэвидж-эффективные решения: ",end='')
    print(*map(lambda x: x.name, getSavidgeOptimal(projects)), sep=",")


    for project in projects:
        print(project.numOptimalCriteria())

