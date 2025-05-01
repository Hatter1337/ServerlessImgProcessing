class MessageGroupIdDistributor:
    """
    A round-robin distributor for SQS FIFO MessageGroupId values.
    """

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

        self._verify_range()
        self.current = start

    def _verify_range(self):
        """
        Verifies that the start and end values are valid.
        """
        if self.start > self.end:
            raise ValueError("Start must be less than or equal to end")

    def next(self) -> str:
        """
        Returns the next MessageGroupId in the round-robin sequence.

        Returns:
            str: The next group ID as a string.
        """
        group_id = str(self.current)
        self.current += 1

        if self.current > self.end:
            self.current = self.start

        return group_id
