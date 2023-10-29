#LIA - Independent Alleles by Teodora Kovacevic

import math

def independent():
    k = 5 
    N = 9  
    prob1 = 0
    for i in range(N, 2 ** k + 1):  #CDF value extraction
        prob = (math.factorial(2 ** k) / (math.factorial(i) * math.factorial(2 ** k - i))) * (0.25 ** i) * (0.75 ** (2 ** k - i))
        prob1 += prob
    print(prob1)

independent()