class SuperAle:
    """
    Superclass capturing common state & behavior for any ale.
    """

    def __init__(self, name: str, abv: float) -> None:
        """
        Init function stores the common values shared across all sub functions.
        """

        self.name = name
        self.abv = abv  # Alcohol by volume (float)

    def alcohol_content(self, volume_in_oz: float) -> float:
        """
        Return total alcohol units for the given volume.
        """

        return self.abv * volume_in_oz

    def description(self) -> str:
        """
        Return a string description of this ale.
        """

        return f"{self.name}: {self.abv * 100:.1f}% ABV"


class PaleAle(SuperAle):
    def __init__(self) -> None:
        super().__init__("Pale Ale", 0.055)


class IPA(SuperAle):
    def __init__(self) -> None:
        super().__init__("IPA", 0.065)


class Stout(SuperAle):
    def __init__(self) -> None:
        super().__init__("Stout", 0.070)


class Porter(SuperAle):
    def __init__(self) -> None:
        super().__init__("Porter", 0.060)


# Custom Testing
pale   = PaleAle()
ipa    = IPA()
stout  = Stout()
porter = Porter()

print(pale.alcohol_content(12)) # 0.66
print(ipa.alcohol_content(12)) # 0.78
print(stout.alcohol_content(12)) # 0.84
print(porter.alcohol_content(12)) # 0.72
print(pale.alcohol_content(0)) # 0.0
print(ipa.alcohol_content(-5)) # -0.325
print(pale.description()) # "Pale Ale: 5.5% ABV"
print(ipa.description()) # "IPA: 6.5% ABV"
print(stout.description()) # "Stout: 7.0% ABV"
print(porter.description()) # "Porter: 6.0% ABV"


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 