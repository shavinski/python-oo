class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create generator with start value and sequential value"""
        self.start = start
        self.sequential = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        """Add +1 to sequential"""
        self.sequential = self.sequential + 1
        return self.sequential - 1

    def reset(self):
        """Reset sequential value to start value"""
        self.sequential = self.start
