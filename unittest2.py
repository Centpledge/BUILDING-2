def cube(n):
    return n**3
def triarea(base,height):
    return base * height /2
import unittest

class myTest(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(5),125)
        self.assertEqual(cube(10),1000)
        self.assertEqual(cube(0),0)
    def test_triarea(self):
        self.assertEqual(triarea(10,10),50)
        self.assertEqual(triarea(0,0),0)
        self.assertEqual(triarea(5,10),25)

unittest.main()
        
