#Probabbility that atleast one woman is chosen
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import random
from scipy.special import comb
list_people =(list)(range(1,9)) #let the numbers 1,2,3 denote the women while the others denote men
simlen=int(1e5)

n=range(0,4)
def prob_women(k):
  success=0
  for i in range(simlen):
    count_woman=0
    random.shuffle(list_people)
    for j in range(0,4):
      if list_people[j] >=1 and list_people[j] <=3:
        count_woman +=1
        
    if count_woman ==k:
      success=success+1
  return (success/simlen )   
print("The simulated probability of atleast one woman being chosen is",prob_women(1)+prob_women(2)+prob_women(3))
print("The theoretical probability of atleast one woman being chosen is ",13/14)
psim=[]
panal=[]
for i in range(0,4):
  psim.append(prob_women(i))
  panal.append(comb(3,i)*comb(5,4-i)/comb(8,4))


#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='x',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor