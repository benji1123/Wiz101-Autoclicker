"""
Promised Rhiannon i'd write
a pet training script a month ago.
here it is....
"""

import pyautogui

# CONSTANTS
PLAY_X = 671
PLAY_Y = 823

SKIP_X = 0
SKIP_Y = 0

PICKSNACK_X = 0
PICKSNACK_Y = 0

FEED_X = 0
FEED_Y = 0


def main():
	Button play = new Button(PLAY_X, PLAY_Y)
	Button skip = new Button(SKIPGAME_X, SKIPGAME_Y)
	Button snack = new Button(PICKSNACK_X, PICKSNACK_Y)
	Button feed = new Button(FEED_X, FEED_Y)

	actionSequence = [play, skip, snack, feed]
	Trainer trainer = new Trainer(actionSequence)
	trainer.train()


class Button:
	# a coordinate on the screen
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def click(self):
		# click the button
		print('click')


class Trainer:
	def __init__(self, clickSequence):
		self.clickSequence = clickSequence

	def train(self):
		for button in clickSequence:
			button.click()



