from event import Event


class FillEvent(Event):
    """
    Models the event of receiving a filled order notice
    from a brokerage. In it are the quantity of the instrument
    that was actually filled along with the price. It also
    contains the comission of the trade from the brokerage.
    """

    def __init__(self, timeindex, symbol, exchange, quantity, direction, fill_cost, comission=None):
        """
        FillEvent initializer. Here is set the symbol, exchange, quantity, 
        direction and fill cost. Setting commission is optional.

        If no commission is selected, a commission will be calculated.

        Parameters:
        timeindex - Bar-resolution at the time the order was filled, 
        i.e., whether a bar represents 1 min, 1 hour, 1 day, etc.
        symbol - The instrument which was filled.
        exchange - The exchange on which the fill occurred.
        quantity - The number of shares filled in the order.
        direction - 'BUY' or 'SELL'
        fill_cost - The cost to fill the order.
        commission - The commission paid to the broker.
        """

        self.type = "FILL"
        self.timeindex = timeindex
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.direction = direction
        self.fill_cost = fill_cost

        # Calculate the commission
        if comission is None:
            self.commission = self.calculate_commission()
        else:
            self.commission = comission

    def calculate_commission():
        """
        Calculates the commission fee from Saxo Bank.
        """
        raise NotImplementedError
