class TestFixtures(unittest.TestCase):
  def test_sum_q_1(self):
    self.assertEquals(cuadrado_de_suma(1, 2),9)
    
  def test_sum_q_2(self):
    self.assertEquals(cuadrado_de_suma(-10, 3),49)
  