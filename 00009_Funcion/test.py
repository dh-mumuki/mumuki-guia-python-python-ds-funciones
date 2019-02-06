class TestFixtures(unittest.TestCase):
  def Test_2(self):
    self.assertEquals(cuadrado_de_suma(1, 2), 9)
    
  def Test_1(self):
    self.assertEquals(cuadrado_de_suma(-10, 3), 49)
  