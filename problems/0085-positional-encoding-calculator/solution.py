import numpy as np

def pos_encoding(position: int, d_model: int):
	pos_encoding = [[0] * d_model for _ in range(position)]
	for row in range(position):
		for col in range(d_model):
			if col%2 == 0:
				pos_encoding[row][col] = np.sin(row/(10000)**(col/d_model))
			else:
				pos_encoding[row][col] = np.cos(row/(10000)**((col-1)/d_model))
	pos_encoding = np.float16(pos_encoding)
	return pos_encoding