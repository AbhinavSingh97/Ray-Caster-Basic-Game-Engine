from data import *  
import math
from vector_math import *

def sphere_intersection_point(ray, sphere):

  A = dot_vector(ray.dir,ray.dir)
  B = (2*dot_vector(difference_point(ray.pt, sphere.center), ray.dir))
  C = (dot_vector(difference_point(ray.pt, sphere.center),difference_point(ray.pt, sphere.center)) - sphere.radius ** 2)
  
  if (B ** 2) - 4*A*C >= 0:
   
    t1 = (-B + math.sqrt((B ** 2) - 4*A*C))/(2*A)
  
    t2 = (-B - math.sqrt((B ** 2) - 4*A*C))/(2*A)
    
    if t1 >= 0 and t2 >= 0:
      return translate_point(ray.pt, scale_vector(ray.dir, t2))
   
    if t1 < 0 and t2 < 0:
        return None 
      
    if t1 >= 0 and t2 < 0:
      return translate_point(ray.pt, scale_vector(ray.dir, t1))
   
    if t1 <0 and t2 >= 0:
      return translate_point(ray.pt, scale_vector(ray.dir, t2))
  
  else: 
      return None

      
def find_intersection_points(sphere_list, ray):
   expected = []
   for i in range(len(sphere_list)): 
      if sphere_intersection_point(ray,sphere_list[i]) != None:
        expected.append((sphere_list[i], sphere_intersection_point(ray,sphere_list[i])))

   return expected

def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))
          
