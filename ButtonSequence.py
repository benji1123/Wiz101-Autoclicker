from ButtonFactory import ButtonFactory
from Button import Button

class ButtonSequence:
	def __init__(self):
		bf = ButtonFactory()
		skip = bf.newSkipButton()
		snack = bf.newPickSnackButton()
		feed = bf.newFeedButton()
		reset = bf.newResetButton()
		self.buttons = [skip, snack, feed, reset]

	def execute(self):
		for button in self.buttons:
			button.click()
