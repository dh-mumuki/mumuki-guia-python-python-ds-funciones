class TestFixtures(unittest.TestCase):
  def test_listas_len(self):
    self.assertEquals(contador([2, 5, 4, 8, 9, 3, 5 , 6]),  8)
    
  def test_listas_media(self):
    self.assertEquals(media([2, 5, 4, 8, 9, 3, 5 , 6]),  5.25)    