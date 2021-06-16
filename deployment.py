from progressbar import ProgressBar
from playsound import playsound
from time import perf_counter
path = 'O:\\Олег\\программирование\\python\\blackufa_chat_stat\\data\\sorted'
f_with_msg = open(path + '\\msg_xxx.txt', 'r', encoding='utf-8')
f_msg_deployed = open(path + '\\msg_xxx_deployed.txt', 'a', encoding='utf-8')
start_time = perf_counter()
pbar = ProgressBar(maxval=2021249)
pbar.start()


def find_xxx(line):
	end = False
	for i in range(1, 100):
		if (' x⁣' + str(i) + ' ' in line) or (' x⁣' + str(i) in line) or ('x⁣' + str(i) in line):
			end = True
	return end


def find_count(word):
	for i in range(1, 100):
		if (' x⁣' + str(i) + ' ' in word):
			end = int(i)
		elif (' x⁣' + str(i) in word):
			end = int(i)
		elif ('x⁣' + str(i) in word):
			end = int(i)
	return end


def deploy_line(line):
	end = ''
	last_word = ''
	for word in line.split():
		if not find_xxx(word):
			end += word + ' '
		else:
			end += (last_word + ' ') * (find_count(word) - 1)
		last_word = word
	return end


def deploy(line):
	while find_xxx(line):
		line = deploy_line(line)
	f_msg_deployed.write(line + '\n')


count = 0
for line in f_with_msg.readlines():
	count += 1
	pbar.update(count)
	deploy(line)


f_with_msg.close()
f_msg_deployed.close()
end_time = perf_counter()
f_time_for_deploy = open(path + '\\time_for_deploy.txt', 'a', encoding='utf-8')
pbar.finish()
f_time_for_deploy.write(str(end_time - start_time))
print(str(end_time - start_time))
playsound('ding.mp3')
f_time_for_deploy.close()
