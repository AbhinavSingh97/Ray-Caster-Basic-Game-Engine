from collisions import *
from vector_math import * 
from math import * 
from data import *
import sys

def distance(ep, point):
  return sqrt((ep.x - point.x)**2 + (ep.y - point.y)**2 + (ep.z - point.z)**2 )

def ambience_multipication(color, ambience):
  return (color.r * ambience), (color.g * ambience), (color.b * ambience)

def color_mutliplication(color1, color2):
  return (color1[0] * color2.r), (color1[1] * color2.g), (color1[2] * color2.b)

def tuple_multplication(tup1, tup2):
  return (tup1[0] * tup2[0]), (tup1[1] * tup2[1]), (tup1[2] * tup2[2])

def tuple_addition(tup1, tup2):
  return (tup1[0] + tup2[0]), (tup1[1] + tup2[1]), (tup1[2] + tup2[2])

def cast_ray(ray, sphere_list,eye_point, color, Light):
   if len(find_intersection_points(sphere_list, ray)) > 0:

     sl = find_intersection_points(sphere_list, ray)
     for i in range(len(sl)):
      
       min_dist = distance(eye_point, sl[0][1])
       
       printed_sphere = sl[0][0]
       int_point = sl[0][1]

       dist = distance(eye_point,sl[i][1])
       
       if dist < min_dist:
        min_dist = dist 
        printed_sphere = sl[i][0]
        int_point = sl[i][1]


     psc = printed_sphere.color
     fsc = printed_sphere.finish.ambient
     sphere_ambience = ambience_multipication(psc, fsc)
     ambience_mult = color_mutliplication(sphere_ambience, color)
     
     diffuse = printed_sphere.finish.diffuse
     
     n = sphere_normal_at_point(printed_sphere, int_point)
     mult_vector = scale_vector(n, .01)
     pe = translate_point(int_point, mult_vector)
     
     ldir = normalize_vector(vector_from_to(pe, Light.pt))
     light_ray = Ray(pe, ldir)
     light_n = dot_vector(n,ldir)

     sphere_diffuse = ambience_multipication(psc, diffuse)
     reflection = difference_vector(ldir,scale_vector(n, (2*light_n)))
     vdir = normalize_vector(vector_from_to(eye_point, pe))
     specular_intensity = dot_vector(reflection, vdir)
     
     if len(find_intersection_points(sphere_list, light_ray)) == 0:
          if dot_vector(n, ldir) > 0:
            light_color = Light.color
            if specular_intensity > 0:
              light_col = ambience_multipication(Light.color,(printed_sphere.finish.specular * (specular_intensity ** (1/printed_sphere.finish.roughness))))
            else:
              light_col = (0, 0, 0)
          else:
            light_color = Color(0, 0, 0)
            light_col = (0, 0, 0)
          
          light_N = ambience_multipication(light_color, light_n)
          total_diffuse = tuple_multplication(light_N, sphere_diffuse)

     else: 
        total_diffuse = (0, 0, 0)
        light_col = (0, 0, 0)
  
     total = tuple_addition(ambience_mult, total_diffuse)
     return tuple_addition(total, light_col)

   else:
        return False 

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, Light, filename):
   s_x =  ((max_x - min_x)/ float(width)) 
   s_y =  ((max_y - min_y)/ float(height))
   mx = min_x
   my = max_y
   filename.write('P3\n' )
   filename.write(str(width) + '\n')
   filename.write(str(height) +'\n')
   filename.write(str(255) +'\n')
   while (my > min_y):
      while (mx < max_x):
        v1 = vector_from_to(eye_point, Point(mx + s_x, my - s_y, 0))
        r1 = Ray(eye_point, v1)
                

        if cast_ray(r1, sphere_list, eye_point, color, Light):
           c = cast_ray(r1, sphere_list, eye_point, color, Light)
           write_colors = colors(c[0], c[1], c[2]) 
           filename.write(str(write_colors) + '\n')               
        else:
           filename.write(str(colors(1, 1, 1)) + '\n')
        mx = mx + s_x
                
      mx = min_x
      my-=s_y

def colors(r, g, b):
   
   if int(r * 255) > 255:
     r = 1

   if int(g * 255) > 255:
    g = 1

   if int(b * 255) > 255:
    b = 1

   return (str(int(r * 255)) + " " + str(int(g * 255)) + " " + str(int(b * 255)))

