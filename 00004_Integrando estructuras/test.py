class TestFixtures(unittest.TestCase):
  def test_listas_cantidad_elementos(self):
    self.assertEquals(contador([2, 5, 4, 8, 9, 3, 5 , 6]),  8, 'La funcion no devuelve la cantidad de elementos requerida')
    
  def test_listas_media(self):
    self.assertEquals(media([2, 5, 4, 8, 9, 3, 5, 6, 10, 15]),  6, 'La funcion no computa adecuadamente la media.')

  def test_listas_sumatoria(self):
    self.assertEquals(sumatoria([2, 5, 4, 8, 9, 3, 5, 6, 10, 15]),  74, 'La funcion no devuelve la suma de elementos requerida'