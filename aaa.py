def sumFromAtoB(a, b):
    return a + b
def sortingTenValues(values):
    return sorted(values)
# 2차 방정식을 계산하는 프로그램
def calculateSecondEquation(a, b, c):
    result = b*b - 4*a*c
    if result > 0:
        return "2개의 실근"
    elif result == 0:
        return "1개의 실근"
    else:
        return "2개의 허근"
