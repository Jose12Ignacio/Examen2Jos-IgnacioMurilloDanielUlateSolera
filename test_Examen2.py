import unittest
from Examen2 import MiClase

class TestExamen2(unittest.TestCase):
    
    def setUp(self):
        self.analizador_musical = MiClase(5, 90, 8, ["Around The World", "Killer Queen", "Even Flow"], [0.5, 0.4, 0.8])

    #Tests metodo ObtenerValencia
    def test_obtener_valencia_correcta_string(self):
        res = self.analizador_musical.ObtieneValencia("56478432")
        self.assertIsInstance(res, int)
        self.assertEqual(res, 3)

    def test_obtener_valencia_correcta_int(self):
        res = self.analizador_musical.ObtieneValencia(43262)
        self.assertIsInstance(res, int)
        self.assertEqual(res, 1)

    #Test metodo DivisibleTempo
    def test_divisible_tempo_cantidad_correcta(self):
        res = self.analizador_musical.DivisibleTempo(13)
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), 2)

    def test_divisible_tempo_divisores_correctos(self):
        res = self.analizador_musical.DivisibleTempo(6)
        self.assertIn(1, res)
        self.assertIn(2, res)
        self.assertIn(3, res)
        self.assertIn(6, res)


    
    

if __name__ == "__main__":
    unittest.main()