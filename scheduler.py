import re
import os

is_24_hour_format = False
start_time = '7:00 AM'
end_time = '9:00 PM'
activity_length = 180
block_length = 5
num_choices = 5

def to_num_12(tme):
	hh, mm, mer = re.split('\W', tme)
	hh, mm = int(hh), int(mm)
	hh %= 12
	if mer == 'PM':
		hh += 12
	return 60*hh + mm

def to_num_24(tme):
	hh, mm = map(int, re.split('\W', tme))
	return 60*hh + mm

def time_to_num(tme):
	if is_24_hour_format:
		return to_num_24(tme)
	else:
		return to_num_12(tme)

def num_to_24(num):
	hh, mm = num//60, num % 60
	return '{}:{:02}'.format(hh, mm)

def num_to_12(num):
	hh, mm = num//60, num % 60
	mer = ''
	if hh >= 12:
		mer = 'PM'
		hh -= 12
	else:
		mer = 'AM'
	if hh == 0:
		hh = 12
	return '{}:{:02} {}'.format(hh, mm, mer)

def num_to_time(num):
	if is_24_hour_format:
		return num_to_24(num)
	else:
		return num_to_12(num)

def find_available():
	f = open('schedules.txt', 'r')
	days = f.readline().split()
	num_days = len(days)

	start = time_to_num(start_time)
	end   = time_to_num(end_time)
	num_blocks = (end - start) // block_length
	check_blocks = activity_length // block_length

	members = []	# names
	scheds = []		# 3D arr, 2D arr = day of week
					# 1D_arr[block_idx] = [members unavailable]
	for i in range(num_days):
		scheds.append([[] for i in range(num_blocks)])
	while member := f.readline():
		member_idx = len(members)
		members.append(member.strip())
		sched = []
		for day in range(num_days):
			day_sched = f.readline().split(sep = ',')
			for interval in day_sched:
				L, R = map(str.strip, interval.split(sep = '-'))
				L, R = map(time_to_num, (L, R))
				L = (L-start)//block_length
				R = (R-start)//block_length
				for block in range(L, R):
					scheds[day][block].append(member_idx)
	f.close()

	num_members = len(members)
	choices = [] # num people unavailable, day of week
				 # start time, [people unavailable]

	for day in range(num_days):
		for start_block in range(num_blocks-check_blocks+1):
			unavails = set()
			for block in range(start_block, start_block+check_blocks):
				unavails.update(scheds[day][block])
			num_unavail = len(unavails)
			cand_start = start_block * block_length + start
			choices.append((num_unavail, day, cand_start, list(unavails)))

	choices.sort()

	f = open('choices.txt', 'w')

	for choice_num in range(num_choices):
		num_unavail, day, choice_start, unavails = choices[choice_num]
		choice_end = choice_start + activity_length
		f.write(f'Choice #{choice_num+1}: {days[day]}, '
				f'{num_to_time(choice_start)} - {num_to_time(choice_end)}\n')
		f.write(f'Members available: {num_members-num_unavail}/{num_members}\n')
		f.write(f'Members unavailable:\n')
		for i in range(len(unavails)):
			if i % 10 == 0:
				f.write('\n')
			f.write('{:<25}'.format(members[unavails[i]]))
		f.write('\n\n')

	f.close()

if __name__ == '__main__':
	find_available()

