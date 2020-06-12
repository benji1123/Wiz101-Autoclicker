import pyautogui as pag
pag.PAUSE = 4

class Button:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def click(self):
		pag.moveTo(self.x, self.y)
		pag.click()
