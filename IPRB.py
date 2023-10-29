#IPRB - Mendel's First Law by Teodora Kovacevic


k = 26 #homo dominant
m = 21 #hetero
n = 17 #homo rec

population = k + m + n
devider = population*(population-1)

kk_cross = k*(k-1)/devider
km_cross = (2*k*m)/devider
kn_cross = 2*k*n/devider
mm_cross = 0.75*m*(m-1)/devider
mn_cross = m*n/devider

prob = kk_cross +km_cross+kn_cross+mm_cross+mn_cross
print(prob)
