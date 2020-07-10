#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # return a list of destinations in order based on source
    trip = [None] * length
    # cache
    cache = {ticket.source: ticket.destination for ticket in tickets}
    # iterate through destinations and place in trip
    # get first
    destination = cache['NONE']
    for i in range(length):
        trip[i] = destination
        destination = cache[destination]
    return trip

