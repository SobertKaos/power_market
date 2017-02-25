

class Market(object):
    """ docstring for Market """
    def __init__(self):
        self.members = set()

    def join(self, applicant):
        """
        Method for joining a Market
        Arguments:
            applicant (Agent) - The Agent instance joining the market
        Returns:
            joined_market (Bool) - Result of applicantion, 'True' if joined, else 'False'
        """
        joined_market = False
        if isinstance(applicant, Agent):
            self.members.add(applicant)
            joined_market = True
        else:
            pass
        return joined_market

    def get_bids(self):
        pass

    def settle_bids(self):
        pass


class Agent(object):
    """ docstring for Agent """
    def __init__(self):
        pass

    def get_demand(self):
        pass

    def post_bid(self):
        pass

if __name__ == '__main__':
    pass
