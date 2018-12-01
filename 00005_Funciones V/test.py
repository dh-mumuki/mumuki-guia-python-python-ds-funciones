class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(lista_par_impar(), ([2, 4, 8, 6, 0], [5, 9, 3, 5]))