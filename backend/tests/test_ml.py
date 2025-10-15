import unittest
import numpy as np
from backend.models.commodity_model import Commodity, commodity_dict

class TestCommodityModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load one commodity for testing"""
        cls.commodity = Commodity(commodity_dict["arhar"])

    def test_predict_current_year(self):
        """Test prediction for current year"""
        month = 9  # September
        year = 2025
        rainfall = 50
        prediction = self.commodity.getPredictedValue([float(month), year, rainfall])
        self.assertIsInstance(prediction, float)
        print("Prediction for current year:", prediction)

    def test_predict_past_year(self):
        """Test prediction for past year (should fetch from CSV)"""
        month = 3
        year = 2015
        rainfall = 40
        prediction = self.commodity.getPredictedValue([float(month), year, rainfall])
        self.assertIsInstance(prediction, float)
        print("Prediction for past year:", prediction)

    def test_crop_name(self):
        """Test if crop name is correctly parsed"""
        name = self.commodity.getCropName()
        self.assertEqual(name.lower(), "arhar")
        print("Crop name:", name)

if __name__ == "__main__":
    unittest.main()
