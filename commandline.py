#This is the command line
from sys import *
from data import *
from casts import *
def command_line(sphere_in):

	sphere_list = []

	for l in sphere_in:

		x = l[0]
		y = l[1]
		z = l[2]

		radius = l[3]
		red = l[4]
		g = l[5]
		b = l[6]

		ambient = l[7]
		diffuse = l[8]
		specular = l[9]
		roughness = l[10]
		pt = Point(x, y, z)
		r = radius
		color = Color(red, g, b)
		finish = Finish(ambient, diffuse, specular, roughness)
		sphere_list.append(Sphere(pt,r, color, finish))

	#try:
	eye_point = Point(0, 0, -14)
	min_x = -10
	max_x = 10
	min_y = -7.5
	max_y = 7.5

	width = 512
	height = 384

	light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
	ambient = Color(1, 1, 1)

	for i in range(len(argv)):
		if argv[i] == "-eye": 
			try:
				argv[i+1]
				argv[i+2]
				argv[i+3]
				try:
					eye_point.x = float(argv[i+1])
				except:
					print "Bad argument for x, reassigning to default value" 
				try:
					eye_point.y = float(argv[i+2])
				except:
					print "Bad argument for y, reassigning to default value"
				try:
					eye_point.z = float(argv[i+3])
				except:
					print "Bad argument for z, reassigning to default value"
			except:
				print "Missing arguments, default eye point will be used"
		if argv[i] == "-view":
			try:
				argv[i+1]
				argv[i+2]
				argv[i+3]
				argv[i+4]
				argv[i+5]
				argv[i+6]
				try:
					min_x = float(argv[i+1])
				except:
					print "Bad argument for min_x, using default value"

				try:
					max_x = float(argv[i+2])
				except:
					print"Bad argument for max_x, using default value"

				try:
					min_y = float(argv[i+3])
				except:
					print "Bad argument for min_y, using default value"

				try:
					max_y = float(argv[i+4])
				except:
					print "Bad argument for max_y, using default value"

				try:
					width = float(argv[i+5])
				except:
					print "Bad argument for width, using default value"

				try:
					height = float(argv[i+6])
				except:
					print "Bad argument for height, using default value"
			except:
				print "Missing arguements for the view, default view will be used"
			
		if argv[i] == "-light":
			try:
				argv[i+1]
				argv[i+2]
				argv[i+3]
				argv[i+4]
				argv[i+5]
				argv[i+6]
				try:
					light.pt.x = float(argv[i+1])
				except:
					print "Bad argument for x attribute of light's point, using default value"

				try:
					light.pt.y = float(argv[i+2])
				except:
					print"Bad argument for y attribute of light's point, using default value"

				try:
					light.pt.z= float(argv[i+3])
				except:
					print "Bad argument for z attribute of light's point, using default value"

				try:
					light.color.r = float(argv[i+4])
				except:
					print "Bad argument for red color aspect of light, using default value"

				try:
					light.color.g = float(argv[i+5])
				except:
					print "Bad argument for green color aspect of light, using default value"

				try:
					light.color.b = float(argv[i+6])
				except:
					print "Bad argument for blue color aspect of light, using default value"
			except:
				print "Missing arguements for the light, default values will be used"
		if argv[i] == "-ambient":
				try:
					ambient.r = float(argv[i+1])
				except:
					print "Bad argument for red, reassigning to default value" 
				try:
					ambient.g = float(argv[i + 2])
				except:
					print "Bad argument for green, reassigning to default value"
				try:
					ambient.b = float(argv[i + 3])
				except:
					print "Bad argument for blue, reassigning to default value"
	if len(argv) == 2:
		print "No arguments were found in the commandline, all defaults will be used."

					
			
			
	img = open('image.ppm', 'w')
	cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light, img)
	img.close()




	#except:

					


	



	
