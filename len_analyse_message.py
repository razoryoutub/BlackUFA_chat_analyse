# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
# import csv
from progressbar import ProgressBar

"""
'а' : 0,
'б' : 0,
'в' : 0,
'г' : 0,
'д' : 0,
'е' : 0,
'ё' : 0,
'ж' : 0,
'з' : 0,
'и' : 0,
'й' : 0,
'к' : 0,
'л' : 0,
'м' : 0,
'н' : 0,
'о' : 0,
'п' : 0,
'р' : 0,
'с' : 0,
'т' : 0,
'у' : 0,
'ф' : 0,
'х' : 0,
'ц' : 0,
'ч' : 0,
'ш' : 0,
'щ' : 0,
'ъ' : 0,
'ы' : 0,
'ь' : 0,
'э' : 0,
'ю' : 0,
'я' : 0,
"""

symbols = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0,
	'7': 0,
	'8': 0,
	'9': 0,
	'10': 0,
	'11': 0,
	'12': 0,
	'13': 0,
	'14': 0,
	'15': 0,
	'16': 0,
	'17': 0,
	'18': 0,
	'19': 0,
	'20': 0,
	'21': 0,
	'22': 0,
	'23': 0,
	'24': 0,
	'25': 0,
	'26': 0,
	'27': 0,
	'28': 0,
	'29': 0,
	'30': 0,
	'31': 0,
	'32': 0,
	'33': 0,
	'34': 0,
	'35': 0,
	'36': 0,
	'37': 0,
	'38': 0,
	'39': 0,
	'40': 0,
	'41': 0,
	'42': 0,
	'43': 0,
	'44': 0,
	'45': 0,
	'46': 0,
	'47': 0,
	'48': 0,
	'49': 0,
	'50': 0,
	'51': 0,
	'52': 0,
	'53': 0,
	'54': 0,
	'55': 0,
	'56': 0,
	'57': 0,
	'58': 0,
	'59': 0,
	'60': 0,
	'61': 0,
	'62': 0,
	'63': 0,
	'64': 0,
	'65': 0,
	'66': 0,
	'67': 0,
	'68': 0,
	'69': 0,
	'70': 0,
	'71': 0,
	'72': 0,
	'73': 0,
	'74': 0,
	'75': 0,
	'76': 0,
	'77': 0,
	'78': 0,
	'79': 0,
	'80': 0,
	'81': 0,
	'82': 0,
	'83': 0,
	'84': 0,
	'85': 0,
	'86': 0,
	'87': 0,
	'88': 0,
	'89': 0,
	'90': 0,
	'91': 0,
	'92': 0,
	'93': 0,
	'94': 0,
	'95': 0,
	'96': 0,
	'97': 0,
	'98': 0,
	'99': 0,
	'100': 0,
	'101': 0,
	'102': 0,
	'103': 0,
	'104': 0,
	'105': 0,
	'106': 0,
	'107': 0,
	'108': 0,
	'109': 0,
	'110': 0,
	'111': 0,
	'112': 0,
	'113': 0,
	'114': 0,
	'115': 0,
	'116': 0,
	'117': 0,
	'118': 0,
	'119': 0,
	'120': 0,
	'121': 0,
	'122': 0,
	'123': 0,
	'124': 0,
	'125': 0,
	'126': 0,
	'127': 0,
	'128': 0,
	'129': 0,
	'130': 0,
	'131': 0,
	'132': 0,
	'133': 0,
	'134': 0,
	'135': 0,
	'136': 0,
	'137': 0,
	'138': 0,
	'139': 0,
	'140': 0,
	'141': 0,
	'142': 0,
	'143': 0,
	'144': 0,
	'145': 0,
	'146': 0,
	'147': 0,
	'148': 0,
	'149': 0,
	'150': 0,
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
f_users = open(path + '\\sorted\\msg.txt', 'r', encoding='utf-8')

pbar = ProgressBar(maxval=11730072)
pbar.start()


temp_count = 0
for line in f_users.readlines():
	temp_count += 1
	try:
		pbar.update(temp_count)
	except ValueError:
		pass
	temp_count += 1
	symbol_count = 0
	for symbol in line:
		symbol_count += 1
	try:
		symbols[str(symbol_count)] += 1
	except KeyError:
		pass
f_users.close()
pbar.finish()

# df = pd.read_csv('./passwords.csv', low_memory=False)


symbol_count_keys, symbol_count_values = symbols.keys(), symbols.values()
TOP_SYMBOL = len(symbol_count_keys)
plt.title('средняя длина сообщений чата', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(len(symbols)), symbol_count_values, color=getColors(TOP_SYMBOL))
plt.xticks(np.arange(TOP_SYMBOL), symbol_count_keys, rotation=0, fontsize=12)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество символов', fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()
