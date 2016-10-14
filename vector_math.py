import math
import data

def scale_vector(vector,scalar): 
    scalar = float(scalar)
    v1 = data.Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar) 
    return v1

def dot_vector(vector1, vector2):
   v1 = data.Vector(vector1.x,vector1.y,vector1.z)
   v2 = data.Vector(vector2.x,vector2.y,vector2.z)
   vf = ((v1.x * v2.x)+ (v1.y * v2.y) + (v1.z * v2.z))
   return vf 

def length_vector(vector):  
   return  (math.sqrt((vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2)))

def normalize_vector(vector):
   return data.Vector (vector.x * (1/length_vector(vector)), vector.y * (1/length_vector(vector)), vector.z * (1/length_vector(vector)))
   
def difference_point(point1, point2):
   v = data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)
   return v

def difference_vector(vector1, vector2):
   v = data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
   return v

def translate_point(point,vector):
   p = data.Point( point.x + vector.x, point.y + vector.y, point.z + vector.z)
   return p

def vector_from_to(from_point,to_point):
   v = data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)
   return v
