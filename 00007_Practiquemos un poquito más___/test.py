class TestFixtures(unittest.TestCase):
  def test_dos(self):
    self.assertEquals(producto(2),4)
  
  def test_negativo(self):
    self.assertEquals(producto(-4),16)