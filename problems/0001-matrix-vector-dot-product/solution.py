import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a)==0:
		return -1
	if len(a[0]) != len(b):
		return -1
	a = np.array(a)
	b = np.array(b)
	return a@b