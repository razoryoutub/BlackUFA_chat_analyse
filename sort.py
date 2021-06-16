from progressbar import ProgressBar
import os
from time import perf_counter
path = 'O:\\Олег\\программирование\\python\\blackufa_chat_stat\\data'
f_users = open(path + '\\sorted\\users.txt', 'a', encoding='utf-8')
f_msg = open(path + '\\sorted\\msg.txt', 'a', encoding='utf-8')
pbar = ProgressBar(maxval=len(os.listdir(path)))
pbar.start()
start_time = perf_counter()


def find_xxx(line):
	end = True
	for i in range(1, 100):
		if (' x⁣' + str(i) + ' ' in line) or (' x⁣' + str(i) in line):
			end = False
	return end


for i in range(1, len(os.listdir(path))):
	pbar.update(i)
	f = open(path + '\\' + os.listdir(path)[i], encoding='utf-8')
	for line in f.readlines():
		if line.find('&}') != -1:
			f_users.write(line[line.find('&}') + 2:line.find('&}: ') - 11] + '\n')

			if find_xxx((line[line.find('&}: ') + 4:]).replace(r'\N', '')):
				f_msg.write((line[line.find('&}: ') + 4:]).replace(r'\N', ''))
			else:
				f_msg_xxx = open(path + '\\sorted\\msg_xxx.txt', 'a', encoding='utf-8')
				f_msg_xxx.write((line[line.find('&}: ') + 4:]).replace(r'\N', ''))
				f_msg_xxx.close()
	f.close()


pbar.finish()
f_users.close()
f_msg.close()
end_time = perf_counter()
f_record_time = open(path + '\\time_to_convert_separation.txt', 'a', encoding='utf-8')
f_record_time.write(str(end_time - start_time))
f_record_time.close()
