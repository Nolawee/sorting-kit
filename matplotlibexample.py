import numpy as np
import matplotlib.pyplot as plt 
'''
plt.plot([1,2,5,7,8],[10,20,30,40], 'ro')
plt.axis([0,10,0,50])
'''

'''
plt.plot(,[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.ylabel('Time (seconds)')
plt.xlabel('Amount of elements (n)')
'''

# evenly sampled time at 200ms intervals
t = np.arange(0.,5.,0.2)

#red dashes, blue squares and green triangles
plt.plot([1,2,3,4],[1,54,76,295], 'r--', t,t**2, 'bs',t,t**3,'g^')
plt.title('worst vs. best case')



plt.show()