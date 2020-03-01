import numba as nb
import numpy as np
import timeit

@nb.jit(nopython=True)
def smooth_jit(array):
  sarray = np.empty_like(array)
  for index in range(1, len(array)-1):
    sarray[index] = (0.5*array[index-1] + array[index] + 0.5*array[index+1])/2
  return sarray


def smooth(array):
  sarray = np.empty_like(array)
  for index in range(1, len(array)-1):
    sarray[index] = (0.5*array[index-1] + array[index] + 0.5*array[index+1])/2
  return sarray

array = np.random.rand(1000)
print(np.round(timeit.timeit("smooth(array)", globals={"smooth":smooth, "array":array}, number=1000),2))
print(np.round(timeit.timeit("smooth_jit(array)", globals={"smooth_jit":smooth_jit, "array":array}, number=1000),2))
