import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

logging.debug(a.shape)
logging.debug(a)

logging.debug(a.dtype)

# startindex, endindex,step
logging.debug(a[1, 0:4:3])
logging.debug(a[1: ])

