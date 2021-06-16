from progressbar import ProgressBar
import os
path = 'O:\\Олег\\программирование\\python\\blackufa_chat_stat\\data'
f_users = open(path + '\\sorted\\just_all_users.txt', 'a', encoding='utf-8')
users = []
pbar = ProgressBar(maxval=len(os.listdir(path)))
pbar.start()


for i in range(1, len(os.listdir(path))):
	pbar.update(i)
	f = open(path + '\\' + os.listdir(path)[i], encoding='utf-8')
	for line in f.readlines():
		if line.find('&}') != -1:
			if line[line.find('&}') + 2:line.find('&}: ') - 11] not in users:
				f_users.write(line[line.find('&}') + 2:line.find('&}: ') - 11] + '\n')
				users.append(line[line.find('&}') + 2:line.find('&}: ') - 11])
	f.close()


pbar.finish()
f_users.close()
