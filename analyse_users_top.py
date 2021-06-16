# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
# import csv
from progressbar import ProgressBar

symbols = {
}


PLOT_LABEL_FONT_SIZE = 14


def getColors(n):
	"""
	Генирирует n цветов и возвращает массив
	"""
	COLORS = []
	cm = plt.cm.get_cmap('hsv', n)
	for i in np.arange(n):
		COLORS.append(cm(i))
	return COLORS


path = 'O:\\Олег\\программирование\\python\\blackufa_chat_stat\\data'
f_users = open(path + '\\sorted\\users.txt', 'r', encoding='utf-8')

pbar = ProgressBar(maxval=23460142)
pbar.start()


temp_count = 0
for line in f_users.readlines():
	temp_count += 1
	try:
		pbar.update(temp_count)
	except ValueError:
		pass
	temp_count += 1
	if line in symbols:
		symbols[line] += 1
	else:
		symbols[line] = 1

f_users.close()
pbar.finish()

# df = pd.read_csv('./passwords.csv', low_memory=False)

dict_items = symbols.items()
sorted(dict_items)

symbol_count_keys, symbol_count_values = symbols.keys(), symbols.values()
TOP_SYMBOL = len(symbol_count_keys)
plt.title(' ', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(len(symbols)), symbol_count_values, color=getColors(TOP_SYMBOL))
plt.xticks(np.arange(TOP_SYMBOL), symbol_count_keys, rotation=0, fontsize=12)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество слов', fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()
