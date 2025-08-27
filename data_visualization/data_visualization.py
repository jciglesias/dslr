class DataVisualization:
    """
    - List of subject columns
    - Hogwarts house colors
    """

    # Whitelist of subject columns
    whitelist = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]

    # Hogwarts house colors
    HOUSE_COLORS = {
        "Gryffindor": "#740001",  # Red
        "Hufflepuff": "#FFDB00",  # Yellow
        "Ravenclaw": "#222F5B",   # Dark Blue
        "Slytherin": "#1A472A"    # Dark Green
    }

    @classmethod
    def get_subjects(cls):
        """Return the list of subjects"""
        return cls.whitelist

    @classmethod
    def get_house_colors(cls):
        """Return the house colors dictionary"""
        return cls.HOUSE_COLORS
