class TestFixtures(unittest.TestCase):
  def test_listas(self):
    self.assertEquals(lista_par_impar([2, 5, 4, 8, 9, 3, 5 , 6, 0]), ([2, 4, 8, 6, 0], [5, 9, 3, 5]), 'La funcion clasifica de forma incorrecta, la primera lista debe contener los pares y la segunda los impares.')