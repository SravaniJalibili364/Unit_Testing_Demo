import unittest

import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.add(10.5,23.34),33.84)
        self.assertEqual(calculator.add(-23,20),-3)
        self.assertEqual(calculator.add(30,-40),-10)
        self.assertEqual(calculator.add(-30,-23),-53)


    def test_subtraction(self):
        self.assertEqual(calculator.sub(-34,-32),-2)
        self.assertEqual(calculator.sub(-34,12),-46)
        self.assertEqual(calculator.sub(34.5,-12),46.5)
        self.assertEqual(calculator.sub(34,12),22)




    def test_multiplication(self):
        self.assertEqual(calculator.mul(-2.3,2.6),-5.9799999999999995)
        self.assertEqual(calculator.mul(2.3,-2.6),-5.9799999999999995)
        self.assertEqual(calculator.mul(-2.3,-2.6),5.9799999999999995)
        self.assertEqual(calculator.mul(2.3,2.6),5.9799999999999995)



    
    def test_division(self):
        self.assertEqual(calculator.div(22,-11),-2)
        self.assertEqual(calculator.div(-22,11),-2)
        self.assertEqual(calculator.div(-22,-11),2)
        self.assertEqual(calculator.div(22,11),2)


        #self.assertRaises(ValueError,calculator.div(21,0))
        #self.assertRaises(ValueError,calculator.div(0,0))


        with self.assertRaises(ValueError):
           calculator.div(0,0)
        with self.assertRaises(ValueError):
           calculator.div(76,0)





if __name__ == "__main__" :
    unittest.main()
