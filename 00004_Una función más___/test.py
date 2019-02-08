class TestFixtures(unittest.TestCase):
  def test_listas_cantidad_elementos(self):
    self.assertEqual(contador([2, 5, 4, 8, 9, 3, 5 , 6]),  8, 'La funcion no devuelve la cantidad de elementos requerida')
    
  def test_listas_media(self):
    self.assertEqual(media([2, 5, 4, 8, 9, 3, 5 , 6]),  5.25, 'La funcion no computa adecuadamente la media.')    