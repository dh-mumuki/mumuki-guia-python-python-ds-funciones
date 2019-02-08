class TestFixtures(unittest.TestCase):
  def test_perimetro(self):
    self.assertAlmostEqual(perimetro_circulo(5), 31.416, places=1, msg='Recorda que el perimetro es  2 * radio * pi')

  