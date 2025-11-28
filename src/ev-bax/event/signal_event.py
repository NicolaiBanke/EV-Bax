from event import Event


class SignalEvent(Event):
    """
    The event of sending a Signal from a Strategy object.
    Such an event will be received by the Portfolio object
    which will then handles the appropriate action.
    """

    def __init__(self, symbol, datetime, signal_type):
        """
        SignalEvent initializer. The event type is set here as "SIGNAL".

        Parameters:
        symbol - the ticker symbol, e.g., 'MSFT'
        datetime - the point in time when the signal was generated
        signal_type - positioning, i.e. 'LONG' or 'SHORT'
        """
        self.type = "SIGNAL"
        self.symbol = symbol
        self.datetime = datetime
        self.signa_type = signal_type
