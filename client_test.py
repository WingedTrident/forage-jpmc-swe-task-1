import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0])[3], (120.48+121.2)/2)
    self.assertEqual(getDataPoint(quotes[1])[3], (121.68+117.87)/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertGreater(getDataPoint(quotes[0])[1],getDataPoint(quotes[0])[2])
    self.assertGreater(getDataPoint(quotes[1])[1],getDataPoint(quotes[1])[2])


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_checkOutliers(self):
    prices = [
      {"ABC": 0, "DEF": 121.68},
      {"ABC": 121.68, "DEF": 0}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertIs(getRatio(prices[0]["ABC"], prices[0]["DEF"]), 0.0)
    self.assertIs(getRatio(prices[1]["ABC"], prices[1]["DEF"]), "Error: Dividing Price is Zero")



if __name__ == '__main__':
    unittest.main()
