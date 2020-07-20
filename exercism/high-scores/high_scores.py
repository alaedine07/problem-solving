def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True) #because it will sort from the smallest number
    return scores[0:3] #return the first 3
