import pygame

def JudgeAccuracy(xs, ys, r, c, max_error):
    total_err = 0
    valid = True
    prct_correct = 0
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        diff = (x - c[0]) ** 2 + (y - c[1]) ** 2 - r ** 2
        if abs(diff) > max_error:
            valid = False
        else:
            total_err += abs(diff)
    if valid:
        prct_correct = 100 * (1 - (total_err / len(xs) * max_error))
    return valid, prct_correct 
            