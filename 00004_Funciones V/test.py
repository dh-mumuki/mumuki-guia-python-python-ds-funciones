class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(contaor([2, 5, 4, 8, 9, 3, 5 , 6]),  8.0)
    
  def test_listas(self):
    self.assertEquals(media([2, 5, 4, 8, 9, 3, 5 , 6]),  5.25)    