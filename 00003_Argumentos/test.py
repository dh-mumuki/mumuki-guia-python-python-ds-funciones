class TestFixtures(unittest.TestCase):
  def test_entero(self):
    self.assertEquals(tipo_de_dato(5), False, 'Para un entero positivo la funcion debe devolver False')
    
  def test_float(self):
    self.assertEquals(tipo_de_dato(5.0), True, 'Para un float la funcion debe devolver True')
    
  def test_string(self):
    self.assertEquals(tipo_de_dato("cinco"), True, 'Para un string la funcion debe devolver True')
    
  def test_bool(self):
    self.assertEquals(tipo_de_dato(True), False, 'Para un booleano la funcion debe devolver False')