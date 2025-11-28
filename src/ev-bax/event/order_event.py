from event import Event


class OrderEvent(Event):
    """
    Handles the event of sending an Order to the execution system.
    An order object contains a ticker symbol, type (market or limit),
    quantity and direction (whether to buy or sell).
    """

    def __init__(self, symbol, order_type, quantity, direction):
        """
        When the order type is initialized, the type or order,
        market ('MKT') or limit ('LMT') is set, its direction,
        'BUY' or 'SELL' and the quantity of shares in the order.
        The event type is set here as 'ORDER'.

        Parameters:
        symbol - ticker symbol to be traded
        order_type - type of order, 'MKT' for market and 'LMT' for limit order
        quantity - int describing the amount of shares to trade. Is non-negative
        direction - 'BUY' or 'SELL'
        """

        self.type = 'ORDER'
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction

    def print_order(self):
        """
        Prints the values within the order
        """

        print(
            f"Order: Symbol={self.symbol}, Type={self.order_type}, Quantity={self.quantity}, Direction={self.direction}")
