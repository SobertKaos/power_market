

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

    def get_bids(self, time_slot):
        """
        Gets bids from everyone in self.members
        Arguments:
            time_slot (datetime) - time slot for bids to be collected
        Returns:
            bids (dict) - all collected bids

        Example usage:
        Market.get_bids()
        returns bids:
        [{agent_name: '<name>',
          time_slot: datetime,
          amount: <float>,
          bid: <float>
          }
        ]
        """
        bids = list()
        bids.append(member.get_bid(time_slot) for member in self.members)
        return bids

    def settle_bids(self):
        pass

    def report_bids(self, bids):
        for member in self.members:
            member.recieve_bid(bids)


class Agent(object):
    """ docstring for Agent """
    def __init__(self):
        self.demand = dict()

    def get_demand(self):
        pass

    def get_bid(self, index):
        """
        Gets bid for the index time slot
        Arguments:
            index (datetime) - Refers to the timeslot for which the bid is concerned
        Returns:
            bid (dict) - dict containing the keys 'agent_name', 'time_slot', 'amount' and 'bid'
        """
        pass

    def recieve_bid(self, bid):
        pass

if __name__ == '__main__':
    pass
