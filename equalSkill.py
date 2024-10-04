def dividePlayers(skill):
    """
    :type skill: List[int]
    :rtype: int
    """
    skill = sorted(skill)
    average_skill = sum(skill) / (len(skill) / 2)
    if average_skill.is_integer():
        return -1
    else:
        point_1 = 0
        point_2 = -1
        teams = []
        for x in range(int(len(skill) / 2)):
            if skill[point_1] + skill[point_2] != average_skill:
                return -1
            teams.append(skill.pop(point_1) * skill.pop(point_2))
        return(sum(teams))


print(dividePlayers([1,1,2,3]))
