import unittest

from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      self.assertEqual((stock, bid_price, ask_price, price),
                       (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], expected_price))
    """ ------------ Add the assertion below ------------ """


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      self.assertEqual((stock, bid_price, ask_price, price),
                       (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], expected_price))
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
    self.assertEqual(getRatio(120.0, 60.0), 2.0)
    self.assertEqual(getRatio(0, 60.0), 0.0)
    self.assertIsNone(getRatio(120.0, 0))


if __name__ == '__main__':
    unittest.main()
