""" Test suite for power_market.py """
import unittest
from power_market import Market
from power_market import Agent

class TestMarket(unittest.TestCase):
    """ Test Market functionality """
    def test_join(self):
        market = Market()
        agent = Agent()
        self.assertEqual(market.join(1), False)
        self.assertEqual(market.members, set())
        self.assertEqual(market.join(agent), True)
        assert agent in market.members

    def test_get_bids(self):
        pass

    def test_settle_bids(self):
        pass

class TestAgent(unittest.TestCase):
    """ Test Agent functionality """

if __name__ == '__main__':
    unittest.main()
