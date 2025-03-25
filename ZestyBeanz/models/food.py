from odoo import models, fields

class Food(models.Model):
	_name = "food.food"
	_description = "Model For Food"

	name = fields.Char(string="Name")