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
        self.assertEqual(res, 5)

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
    
     # ObtieneMasBailable
     
     #Verifica el elemento de mayor valor en la lista
    def test_mas_bailable_correcto(self):
        res = self.analizador_musical.ObtieneMasBailable([0.6, 0.9, 0.2])
        self.assertEqual(res, 0.9)

    #Verifica comportamiento con lista vacia
    def test_mas_bailable_lista_vacia(self):
        res = self.analizador_musical.ObtieneMasBailable([])
        self.assertIsNone(res)

    # VerificaListaCanciones
    
    # Verifica comportamiento con lista correcta
    def test_verifica_lista_correcta(self):
        res = self.analizador_musical.VerificaListaCanciones(["A1", "B2", "C3"])
        self.assertTrue(res)

    #Verifica comportamiento con None en la lista
    def test_verifica_lista_con_none(self):
        res = self.analizador_musical.VerificaListaCanciones(["A", None])
        self.assertFalse(res)

    def test_encuentra_correcto(self):
        res = self.analizador_musical.Encuentra([7,4,6,8,5], 3)
        self.assertFalse(res)

    

if __name__ == "__main__":
    unittest.main()