import unittest
from data import *
import vector_math
import math
import utility 
import collisions

class TestSpheresColors(unittest.Testcase):
  def test_sphere_with_color(self):
    s = Sphere(Point(0 , 0, 0), 2, 196)
    self.assertEqual(s.center.x, 0)
    self.assertEqual(s.cetner.y, 0)
    self.assertEqual(s.center.z,0)
    self.assertEqual(s.radius, 2 )
    self.assertEqual(s.color, 196)

    
class TestCollisions(unittest.TestCase):
   #Testing the case where both t values are positive, so the sphere should be hit
   
   def test_sphere_intersection(self):
      s = data.Sphere(data.Point(0, 4, 0), 2)
      r = data.Ray(data.Point(0, 1, 0), data.Vector(0, 1, 0))
      # Ray r will intersect with sphere s
      col = collisions.sphere_intersection_point(r, s) #Assigning our values for ray and sphere into our function
      self.assertEqual(col,data.Point(0, 2, 0))

   #Testing the case where both t values are negative, therefore None should be returned
  
   def test_sphere_intersection_2(self):
      s = data.Sphere(data.Point(0, 0, 0), 1)
      r = data.Ray(data.Point(0, 2, 0), data.Vector(0, 1, 0))
      # There should be no intersection leading to None 
      col = collisions.sphere_intersection_point(r, s) #Inputting arguments for the function
      self.assertEqual(col,None)

    #Testing the case where one t value is negative where as the other is positive
    #The non-negative t will be giving us our point of intersection
   
   def test_sphere_intersection_3(self):
      s = data.Sphere(data.Point(0, 0, 0), math.sqrt(19))
      r = data.Ray(data.Point(0, 3, 0), data.Vector(0, 1, 0))
      #This should result in one t be set to a negative number.
      #The point should result from the non-negative t value 
      col = collisions.sphere_intersection_point(r, s) # Inputting arguments for the function
      self.assertEqual(col, data.Point(0, math.sqrt(19), 0)) #The point at which the ray intersects the sphere
      # This is achieved by plugging in the positive t value into the point equation given to us
   

   #Testing the case where the functions square root returns a compiles number
   #This should result in us getting None back because we can't deal with complex numbers
   
   def test_sphere_intersection_4(self):
     s = data.Sphere(data.Point(0, 6, 0), 1)
     r = data.Ray(data.Point(3, 0, 0), data.Vector(0, 1, 0))

     col = collisions.sphere_intersection_point(r, s)
     self.assertEqual(col, None)


   #The ray will be starting from within the sphere and be shot outwards
   #It will have one intersection point when it exits the sphere 
   
   def test_sphere_intersection_5(self):
    s = data.Sphere(data.Point(0, 0 ,0), 3)
    r = data.Ray(data.Point(0, 1, 0), data.Vector(0, 1, 0))

    col = collisions.sphere_intersection_point(r, s)
    self.assertEqual(col, data.Point(0, 3, 0))


  #The ray will glance the sphere, essentially making both t values equal
  #This means that the square root part of the quadratic will return zero 
  #Either t value can be used to return the point of intersection 
  
   def test_sphere_intersection_6(self):
    s = data.Sphere(data.Point(0, 1, 0), 1)
    r = data.Ray(data.Point(1, 0, 0), data.Vector(0, 1, 0))
    #The collision point is at (1, 1, 0) which is expected as the ray shoots up
    #Essentially tangent with the sphere
    col = collisions.sphere_intersection_point(r, s)
    self.assertEqual(col, data.Point(1, 1, 0))
 

  # Testing a case where the list of spheres contains two spheres
  # The first sphere will be hit at (0 , 2, 0) and sphere two will be hit (0, 9, 0)
   
   def test_find_intersection_points(self):
    # The list of spheres
    spheres = [data.Sphere(data.Point(0, 4, 0), 2),
               data.Sphere(data.Point(0, 9, 0), 1)]
    # The ray
    r = data.Ray(data.Point(0, 1, 0), data.Vector(0, 1, 0))
    
    expected = [(spheres[0],data.Point(0, 2, 0,)) ,
                (spheres[1], data.Point(0, 8, 0))]
    col = collisions.find_intersection_points(spheres, r)
    self.assertEqual(col, expected)
   
   #Testing a case where one sphere is hit and the other one is not hit
   #Sphere 1 will not be hit resulting in None, whereas sphere two will be hit at (0, 2, 0)
   
   def test_find_intersection_points_2(self):

    # The list of spheres
    spheres = [data.Sphere(data.Point(0, 0, 0), 1), 
               data.Sphere(data.Point(0, 3, 0), 1)]
    r = data.Ray(data.Point(0, 3, 0), data.Vector(0, 1, 0))
    expected = [(spheres[1], data.Point(0, 4, 0))]
    col = collisions.find_intersection_points(spheres, r)
    self.assertEqual(col, expected)

   
    #Testing a case where none of the spheres will be hit therefore returning None
    #However, we do not want None in our list and this means the list will be empty
    #This is similar to the example given to us in the assignment 
   
    def test_find_intersection_points_3(self):
      spheres = [data.Sphere(data.Point(0, 5, 0), 2.2), 
                  data.Sphere(data.Point(0, 12, 0), 1), 
                  data.Sphere(data.Point(0, 0, 0), 5)]
      r = data.Ray(data.Point(0, 14, 1), data.Vector(0, 1, 0))
      expected = []
      col = collisions.find_intersection_points(spheres, r)
      self.assertEqual(col, expected)

  
   #This test will be testing the normalize vector function, in which we will get a vector
   #from the origin of the sphere to the intersection point, this will make our vector
   #We will take that vector and normalize it 
  
   def test_sphere_normal_at_point(self):
    s = data.Sphere(data.Point(0, 0, 0), 3)
    r = data.Ray(data.Point(0, 1, 0), data.Vector(0, 1, 0))
    col = collisions.sphere_intersection_point(r, s)
    #Since the collision point is (0, 3, 0) and the sphere center is (0, 0, 0)
    # we expect your normalized vector to be (0, 1, 0)
    nv = collisions.sphere_normal_at_point(s, col)
    self.assertEqual(nv, data.Vector(0, 1, 0))
    
   def test_sphere_normal_at_point_2(self):
    s = data.Sphere(data.Point(0, 2, 0), 1)
    r = data.Ray(data.Point(0, 0, 0), data.Vector(0, 1, 0))
    col = collisions.sphere_intersection_point(r, s)
    nv = collisions.sphere_normal_at_point(s, col)
    self.assertEqual(nv, data.Vector(0, -1, 0))


if __name__ == "__main__":
     unittest.main()
