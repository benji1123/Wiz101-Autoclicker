"""
Promised Rhiannon i'd write
a pet training script a month ago.
here it is....
"""

from Pet import Pet

def main():
	energy = 58
	energyPerGame = 10
	pet = Pet(energy, energyPerGame)
	pet.train()

main()
