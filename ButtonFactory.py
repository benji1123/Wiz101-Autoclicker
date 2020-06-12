from Button import Button

SKIP_X = 1703
SKIP_Y = 1204
PICKSNACK_X = 1293
PICKSNACK_Y = 971
FEED_X = 2130
FEED_Y = 1197
RESET_X = 1685
RESET_Y = 1189

class ButtonFactory:
	def __init__(self):
		print('factory')

	def newSkipButton(self):
		return Button(SKIP_X, SKIP_Y)

	def newPickSnackButton(self):
		return Button(PICKSNACK_X, PICKSNACK_Y)

	def newFeedButton(self):
		return Button(FEED_X, FEED_Y)

	def newResetButton(self):
		return Button(RESET_X, RESET_Y)
