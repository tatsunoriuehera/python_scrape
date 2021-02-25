import matplotlib.pyplot as plt
import numpy as np

#plot line chart
#plt.plot([3,4,2,1])
#plt.plot([321,62,167,41,35,414,260])
#plt.ylabel('some numbers')
#plt.show()

#plot bar chart
#left = np.array([1,2,3])
#height = np.array([100,200,300])
#plt.bar(left,height)
#plt.show()

#plot circle chart
x = np.array([100,200,300,400,500])
label = ["apple","banana","orange","grape","strawberry"]
plt.pie(x,labels=label)
plt.show()
