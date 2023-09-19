import copy

gurvitz_coef = 0.6
bayes_coef = [0.1, 0.4, 0.4, 0.1]

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
    names = list(map(lambda x: x.name,savidge_effective))
    orig_projects = list(map(lambda x: x if (x.name in names) else None,projects))
    filtered = list(filter(lambda x: x is not None,orig_projects))
    for i in range(len(filtered)):
        filtered[i].savidge_optimal = True
    return filtered

def getGurvitzOptimal(projects):
    gurvitz_dict = dict.fromkeys(projects)
    for project in gurvitz_dict:
        gurvitz_dict[project] = min(project.states) * gurvitz_coef + max(project.states) * (1 - gurvitz_coef)
    gurvitz_effective = [k for k, v in gurvitz_dict.items() if v == max(gurvitz_dict.values())]
    for project in gurvitz_effective:
        project.gurvitz_optimal = True
    return gurvitz_effective

def getBayesOptimal(projects):
    bayes_dict = dict.fromkeys(projects)
    for project in bayes_dict:
        bayes_dict[project] = 0
        for i in range(len(project.states)):
            bayes_dict[project] += project.states[i] * bayes_coef[i]
    bayes_effective = [k for k, v in bayes_dict.items() if v == max(bayes_dict.values())]
    for project in bayes_effective:
        project.bayes_optimal = True
    return bayes_effective

def getLaplasOptimal(projects):
    laplas_dict = dict.fromkeys(projects)
    for project in laplas_dict:
        laplas_dict[project] = sum(project.states)/len(project.states)
    laplas_effective = [k for k, v in laplas_dict.items() if v == max(laplas_dict.values())]
    for project in laplas_effective:
        project.laplas_optimal = True
    return laplas_effective







