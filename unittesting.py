import Hailstone_sequence_calculator
import unittest

class testHailstone(unittest.TestCase):
    
    def test_even_x(self):
        "This test checks to see if the 'even_x()' function divides the given variable in half."
        self.assertEqual(Hailstone_sequence_calculator.even_x(8, 0), (1, 3))
        
    def test_odd_x(self):
        "This test checks to see if the 'odd_x()' function multiples the given variable by 3, then adds 1."
        self.assertEqual(Hailstone_sequence_calculator.odd_x(5, 0), (1, 5))

    def test_fullprogram(self):
        "This tests checks to see if the 'run_program()' function runs properly."
        self.assertEqual(Hailstone_sequence_calculator.run_program(3), (1, 7))
        #try:
        #    hailstone_sequence_calculator.run_program()


if __name__ == '__main__':
    unittest.main()