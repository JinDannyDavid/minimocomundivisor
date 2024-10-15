import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
from src.logica.OperacionesEnteros import FaltanParametros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 18
        numero2 = 24
        numero3 = 30
        numero4 = 4
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numero1 = 18
        operacion = OperacionesEnteros([numero1])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()

    def test_MCD_unaCadena_lanzaExcepcion(self):
        # Arrange
        numero1 = "18a"
        numero2 = 13
        operacion = OperacionesEnteros([numero1, numero2])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            operacion.calcularMCD()

    def test_mcm_dosNumerosPositivos_retornamcm(self):
        # Arrange
        numero1 = 7
        numero2 = 14
        resultadoEsperado = 14
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = operacion.calcularmcm()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_tresNumerosPositivos_retornamcm(self):
        # Arrange
        numero1 = 7
        numero2 = 14
        numero3 = 35
        resultadoEsperado = 70
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularmcm()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_cuatroNumerosPositivos_retornamcm(self):
        # Arrange
        numero1 = 7
        numero2 = 14
        numero3 = 35
        numero4 = 42
        resultadoEsperado = 210
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularmcm()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_unNumeroPositivo_lanzaExcepcion(self):
        # Arrange
        numero1 = 7
        operacion = OperacionesEnteros([numero1])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(FaltanParametros):
            operacion.calcularmcm()

    def test_mcm_unaCadena_lanzaExcepcion(self):
        # Arrange
        numero1 = "7b"
        numero2 = 14
        operacion = OperacionesEnteros([numero1, numero2])

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            operacion.calcularmcm()