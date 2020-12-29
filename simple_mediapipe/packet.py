import time


class Packet:
    def __init__(self, data=None, timestamp=time.time()*1000):
        # timestamp default unit is milli seconds
        self.data = data
        self.timestamp = timestamp

    def __str__(self):
        return 'Timestamp: {}, Data: {}'.format(self.timestamp, self.data)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __le__(self, other):
        return self.timestamp <= other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __ge__(self, other):
        return self.timestamp >= other.timestamp

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def __ne__(self, other):
        return self.timestamp != other.timestamp
