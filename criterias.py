import copy

from project import Project

def getWaldEffective(projects):
    mins = dict.fromkeys(projects)
    for project in mins:
        mins[project] = min(project.states)
    maxmin = max(mins.values())
    wald_effective = [k for k, v in mins.items() if v == maxmin]
    for project in wald_effective:
        project.wald_optimal = True
    return wald_effective

def getSavidgeOptimal(projects):
    risk_matrix = copy.deepcopy(projects)
    for i in range(0,4):
        max_cur_state = max(map(lambda x: x.states[i],projects))
        for project_copy in risk_matrix:
            project_copy.states[i] = max_cur_state - project_copy.states[i]
    maxes = dict.fromkeys(risk_matrix)
    for project in maxes:
        maxes[project] = max(project.states)
    minmax = min(maxes.values())
    savidge_effective = [k for k, v in maxes.items() if v == minmax]
    for project in savidge_effective:
        project.savidge_optimal = True
    return  savidge_effective







