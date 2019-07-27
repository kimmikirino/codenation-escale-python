import unittest

from main import *


class CloudCostTests(unittest.TestCase):
    def test_lambda_execution(self):
        cc = CloudCost()
        self.assertGreater(cc.lambda_execution(), 0)

    def test_app_execution(self):
        cc = CloudCost()
        self.assertGreater(cc.app_execution(1), 0)
        self.assertGreater(cc.app_execution(50), 0)
        self.assertGreater(cc.app_execution(100), 0)
        self.assertGreater(cc.app_execution(1000), 0)
        self.assertGreater(cc.app_execution(5000), 0)
    
    def test_month(self):
        cc = CloudCost()
        self.assertEqual(cc.month(1, 1), 0.0387128)
        self.assertEqual(cc.month(1, 2), 0.0349664)
        self.assertEqual(cc.month(1, 4), 0.037464)
        self.assertEqual(cc.month(50, 4), 1.8732)
        self.assertEqual(cc.month(100, 4), 3.7464)
        self.assertEqual(cc.month(1000, 4), 37.464)
        self.assertEqual(cc.month(50000, 4), 1873.1999999999998)
    
    def test_year(self):
        cc = CloudCost()
        self.assertEqual(12, len(cc.year(1)))
        self.assertEqual(12, len(cc.year(50)))
        self.assertEqual(12, len(cc.year(100)))
        self.assertEqual(12, len(cc.year(1000)))
        self.assertEqual(12, len(cc.year(5000)))

if __name__ == '__main__':
    unittest.main()
