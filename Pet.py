from Trainer import Trainer

class Pet:
	def __init__(self, energy=130, energyPerGame=12):
		self.energy = energy
		self.energyPerGame = energyPerGame
		self.numPlayableGames = self.energy // self.energyPerGame
		self.trainer = Trainer()

	def train(self):
		for i in range(self.numPlayableGames):
			self.trainer.train()
