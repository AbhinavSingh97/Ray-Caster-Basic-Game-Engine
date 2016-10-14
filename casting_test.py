import unittest
from casts import *
from data import *

def test_cast_all_rays():
	width = 512
	height = 384 

	print 'P3'
	print width, height
	print 255 

	eye_pt = Point(0, 0, -14)
	sphere_list = [Sphere(Point(1, 1, 0), 2, Color(0,0,1), Finish(0.2, 0.4, 0.5, 0.05)) , 
	               Sphere(Point(.5, 1.5, -3), .5, Color(1,0,0), Finish(0.4, 0.4, 0.5, 0.05))]
	img = open('image.ppm', "w")
	cast_all_rays(-10, 10, -7.5, 7.5, width, height, eye_pt, sphere_list, Color(1, 1, 1), Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5)), img)
	img.close()
   
test_cast_all_rays()


