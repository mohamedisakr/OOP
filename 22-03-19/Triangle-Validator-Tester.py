import unittest
import Triangle_Validator

class TestTriangle(unittest.TestCase):

    def test_IsValid_Pass(self):
        actual = Triangle_Validator.IsValid(5, 12, 13)
        expected = True
        self.assertEqual(actual, expected)


    def test_IsValid_NotPass(self):
        actual = Triangle_Validator.IsValid(1, 10, 13)
        expected = False
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

    
#if __name__ == '__main__' :
#    unittest.main(exit=False)
'''  
a = 5#1
b = 12#10
c = 13#12
print('Valid Triangle' if(IsValid(a, b, c)) else 'Not valid triangle')
'''
