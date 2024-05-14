import sys
sys.path.append("src")

from Logica_declaración import Logica
import unittest

from unittest.mock import patch



"""Organizar bien los casos de prueba"""
class Declaracion_test(unittest.TestCase):

    def test_renta_ceroen_ret_seg_apor_hip_don_gas(self):
        ingresos_laborales=50000000
        otros_ingresos=1000000
        retenciones_fuente=0
        seguridad_social=0
        aportes_pension=0
        gastos_creditos_hipotecarios=0
        donaciones=0
        gastos_educacion=0


        result=(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2)) 


    def test_renta_ceroen_otros_ret_hip_don_gas(self):
        ingresos_laborales=60000000
        otros_ingresos=0
        retenciones_fuente=0
        seguridad_social=5000000
        aportes_pension=5000000
        gastos_creditos_hipotecarios=0
        donaciones=0
        gastos_educacion=0

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))
    
    def test_renta_ceroen_otros_ret_seg_apor_hip_gas(self):
        ingresos_laborales=0
        otros_ingresos=0
        retenciones_fuente=0
        seguridad_social=0
        aportes_pension=0
        gastos_creditos_hipotecarios=0
        donaciones=2000000
        gastos_educacion=0

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_ceroen_ingr_otros_seg_apor_hip_don_gas(self):

        ingresos_laborales=0
        otros_ingresos=0
        retenciones_fuente=6000000
        seguridad_social=0
        aportes_pension=0
        gastos_creditos_hipotecarios=0
        donaciones=0
        gastos_educacion=0

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_ceroen_otros_ret(self):
        ingresos_laborales=60000000
        otros_ingresos=0
        retenciones_fuente=0
        seguridad_social=5000000
        aportes_pension=3000000
        gastos_creditos_hipotecarios=2000000
        donaciones=600000
        gastos_educacion=3000000

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=2000000

        self.assertEqual(expected,round(result,2))

    def test_renta_ceroen_seg_ret(self):
        ingresos_laborales=32000000
        otros_ingresos=1200000
        retenciones_fuente=0
        seguridad_social=0
        aportes_pension=3000000
        gastos_creditos_hipotecarios=2000000
        donaciones=500000
        gastos_educacion=26000000

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=1700000

        self.assertEqual(expected,round(result,2))

    def test_renta_ceroen_ingresos(self):
        ingresos_laborales=0
        otros_ingresos=1200000
        retenciones_fuente=1000000
        seguridad_social=5000000
        aportes_pension=3000000
        gastos_creditos_hipotecarios=1100000
        donaciones=500000
        gastos_educacion=1200000

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))
    

    def test_renta_ceroen_gas(self):
        ingresos_laborales=60000000
        otros_ingresos=1300000
        retenciones_fuente=0
        seguridad_social=5000000
        aportes_pension=3000000
        gastos_creditos_hipotecarios=700000
        donaciones=500000    
        gastos_educacion=0

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=52000

        self.assertEqual(expected,round(result,2))

    def test_renta_negativos(self):
        ingresos_laborales=-60000000
        otros_ingresos=-1300000
        retenciones_fuente=-1300000
        seguridad_social=-5000000
        aportes_pension=-3000000
        gastos_creditos_hipotecarios=-700000
        donaciones=-500000    
        gastos_educacion=-2000000

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_decimales(self):
        ingresos_laborales=60000000.25
        otros_ingresos=1300000.3
        retenciones_fuente=1300000.5
        seguridad_social=5000000.0
        aportes_pension=5000000.0
        gastos_creditos_hipotecarios=7000000.8
        donaciones=500000.2    
        gastos_educacion=2000000.0

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_todo_cero(self):
        ingresos_laborales=0
        otros_ingresos=0
        retenciones_fuente=0
        seguridad_social=0
        aportes_pension=0
        gastos_creditos_hipotecarios=0
        donaciones=0    
        gastos_educacion=0

        
        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))
        


    def test_renta_decimales(self):
        ingresos_laborales=60000000.25
        otros_ingresos=1300000.3
        retenciones_fuente=1300000.5
        seguridad_social=5000000.0
        aportes_pension=3000000.0
        gastos_creditos_hipotecarios=700000.8
        donaciones=500000.2    
        gastos_educacion=2000000.0

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_decimal_algunos(self):
        ingresos_laborales=60000000
        otros_ingresos=13000000
        retenciones_fuente=7500000.5
        seguridad_social=5000000
        aportes_pension=5000000
        gastos_creditos_hipotecarios=7000000
        donaciones=500000    
        gastos_educacion=2000000.4

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=23000000

        self.assertEqual(expected,round(result,2))

    def test_renta_decimal_algunos_neg_y_cero(self):
        ingresos_laborales=600000000
        otros_ingresos=1300000
        retenciones_fuente=1300000.5
        seguridad_social=5000000
        aportes_pension=3000000
        gastos_creditos_hipotecarios=700000
        donaciones=500000    
        gastos_educacion=0  

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=23000000

        self.assertEqual(expected,round(result,2))

    def test_renta_cero_en_otros_seg_apor_hip_don_gas(self):
        ingresos_laborales=60000000
        otros_ingresos=0
        retenciones_fuente=1300000
        seguridad_social=0
        aportes_pension=0
        gastos_creditos_hipotecarios=0
        donaciones=0
        gastos_educacion=0  

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_cero_en_ret(self):
        ingresos_laborales=60000000
        otros_ingresos=1300000
        retenciones_fuente=0
        seguridad_social=5000000
        aportes_pension=3000000
        gastos_creditos_hipotecarios=700000
        donaciones=500000    
        gastos_educacion=1300000

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta(self):
        ingresos_laborales=75500000
        otros_ingresos=5300000
        retenciones_fuente=1300000
        seguridad_social=2000000
        aportes_pension=2000000
        gastos_creditos_hipotecarios=3000000
        donaciones=500000    
        gastos_educacion=2500000 

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=2499810

        self.assertEqual(expected,round(result,2))

    def test_renta_ganancias_neg(self):
        ingresos_laborales=-75500000
        otros_ingresos=5300000
        retenciones_fuente=1300000
        seguridad_social=2000000
        aportes_pension=2000000
        gastos_creditos_hipotecarios=3000000
        donaciones=500000    
        gastos_educacion=2500000 

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=0

        self.assertEqual(expected,round(result,2))

    def test_renta_apor_don_neg(self):
        ingresos_laborales=75500000
        otros_ingresos=5300000
        retenciones_fuente=1300000
        seguridad_social=2000000
        aportes_pension=-2000000
        gastos_creditos_hipotecarios=3000000
        donaciones=-500000    
        gastos_educacion=2500000 

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=3259810

        self.assertEqual(expected,round(result,2))

    def test_renta_otros_gas_neg(self):
        ingresos_laborales=75500000
        otros_ingresos=-5300000
        retenciones_fuente=1300000
        seguridad_social=2000000
        aportes_pension=2000000
        gastos_creditos_hipotecarios=3000000
        donaciones=500000    
        gastos_educacion=-2500000 
        
        

        result=Logica.calcular_impuesto_renta(ingresos_laborales,otros_ingresos,retenciones_fuente,seguridad_social,aportes_pension,gastos_creditos_hipotecarios, donaciones,gastos_educacion)

        expected=1435810

        self.assertEqual(expected,round(result,2))
    

    
if __name__=='__main__':
    unittest.main()






