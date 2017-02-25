""" Test suite for power_market.py """
import unittest
from power_market import Market
from power_market import Agent

class TestMarket(unittest.TestCase):
    """ Test Market """
    def test_market_members(self):
        """ test joining a market """
        market = Market()
        agent = Agent()
        self.assertEqual(market.join(1), False)
        self.assertEqual(market.members, set())
        self.assertEqual(market.join(agent), True)
        assert agent in market.members

if __name__ == '__main__':
    unittest.main()
