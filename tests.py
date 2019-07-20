import unittest

def divide(a, b):
    return a / b

# assert divide(10, 2) == 12

class DivideTestCase(unittest.TestCase):
    def test_should_divide(self):
        a, b = 10, 2
        expected = 5

        response = divide(a, b)
        assert response == expected
    

if __name__ == '__main__':
    unittest.main()

# model mommy
# factory boy
# py test

python -m venv myenv
source myenv/bin/activate