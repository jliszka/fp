
import math
import random

class Dist(object):
	def __init__(self, mean, std):
		self.mean = mean
		self.std = std

	def get(self):
		return random.gauss(0, 1) * self.std + self.mean

	def get_monthly(self):
		return random.gauss(0, 1) * self.std / math.sqrt(12) + self.mean / 12

class Ledger(object):
	def __init__(self, year, month, note, amt, tax, bal):
		self.year = year
		self.month = month
		self.note = note
		self.amt = amt
		self.tax = tax
		self.bal = bal

	def __str__(self):
		return '{} {:2d} {:<30s} {:>15s} {:>15s} {:>15s}'.format(
			self.year, self.month, self.note, 
			'${:,.2f}'.format(self.amt),
			'-' if abs(self.tax) < 0.001 else '${:,.2f}'.format(self.tax),
			'${:,.2f}'.format(self.bal),
		)
