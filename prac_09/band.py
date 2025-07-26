class Band:
    """Band class to represent a band made up of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return string representation of the Band, including member details."""
        members_str = ", ".join(str(musician) for musician in self.members)
        return f"{self.name} ({members_str})"

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Simulate all musicians in the band playing their instruments."""
        return "\n".join(musician.play() for musician in self.members)