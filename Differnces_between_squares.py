# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 16:48:51 2016

@author: Kaya
"""

import numpy as np
import matplotlib.pyplot as plt

sqrs=[]
for i in range(20):
    sqrs.append(i**30)
diff=np.subtract(np.array(sqrs[1:-1]),np.array(sqrs[0:-2]))

plt.plot(diff)
plt.show()