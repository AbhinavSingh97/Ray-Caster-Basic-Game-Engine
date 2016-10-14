#This is the ray caster
from casts import *
from vector_math import *
from data import * 
from commandline import * 
from sys import *
def ray_caster():
	try:
		f = open(argv[1], "r")
	except:
		print "usage: python ray_caster <filename>[-eye x y z] [-view min_x max_x min_y max_y width height][-light x y z r g b][-ambient r g b]"

	try:
		final_list = []
		index = 0
		for line in f:
			new_list = []
			l = line.split()
			index += 1
		
			if len(l) == 11:
			
				try:
					for i in range(0, len(l)):
						try:
							new_list.append(float(l[i]))
						except:
							del new_list[:]
							l.next()
					
				except:
					print "malformed sphere on line" + " " + str(index) + " ... skipping"
			
			else:
				print "malformed sphere on line" + " " + str(index) + " ... skipping"
			
			if len(new_list) != 0:
				final_list.append(new_list)

		command_line(final_list)
		f.close()
	except:
		pass
	
	
	
	
if __name__ == "__main__":
	ray_caster()             