from odoo import models, fields , api
from odoo.exceptions import ValidationError
class Food(models.Model):
	_name = "food.food"
	_description = "Model For Food"


	# fields
	name = fields.Char(string="Name")
	partner_id = fields.Many2one('res.partner',string="Name")
	price = fields.Float(string="Standard Price")
	quantity = fields.Integer(string="Amount")
	review = fields.Text(string="Review Of The Food")
	is_satisfied = fields.Boolean(string="Satisfied/Not")
	check_in = fields.Date(string="Check In")
	served_time = fields.Datetime(string="Served Time")
	types = fields.Selection([('dine_in','Dine In'),('delivery','Delivery')])
	images = fields.Binary(string="Images")
	blog = fields.Html(string="Blog")
	sale_order_id = fields.Many2one('sale.order',string="Sale Order")
	invoice_id = fields.Many2one('account.move',string="Related Invoice")

	def test_function(self):
		# Conditional Statement
		if self.name:
			print("Name Field is not empty",self.name) # ExceptionHandling
		else:
			print("The Name field is empty")

	# ORM Methods
	# Create
	# Extend     = Extending base logic + Custom logic (base+custom)
	# Override   = Is Removing all the base Function and Setting Your logic

	@api.model
	def create(self,vals):
		"""
		Before creationg
		"""
		res = super(Food,self).create(vals)
		"""
		After creation
		"""
		# res contain the created record
		if res.is_satisfied == False: # checking the is_satisfield is true or not
			res.is_satisfied = True   # assingning it true

		return res
	
	def write(self,vals):
		flag = 1
		if flag ==1:
			raise ValidationError("You are not permitted to edit the record")
		
		"""
		Before writing
		"""

		res = super(Food,self).write(vals)
		"""
		After edit
		"""

		return res