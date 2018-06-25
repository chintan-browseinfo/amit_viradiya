from odoo import api, fields, models, _

class Insurance(models.Model):

    _name = "insurance.info"
    _description = "insurance info"

    name = fields.Char(string='Insurance Info', required=True, copy=False)
    insurance_Type = fields.Selection([('a', 'Auto_Insurance'), ('h', 'Health_Insurance'),
                                    ('l', 'Lifetime_insurance')],string='Insurance_Type')
    insuracne_amt = fields.Integer(string='Insurance_amt',required=True,copy=False)
    account_id = fields.Many2one('res.partner', String="Agent")
    insurance_line = fields.One2many('customer.info','customer_id', string="insurance_line")
    insurance_ids = fields.Many2many('customer.info','insurance_rel','customer_id','insurance_ids',string='insurance_ids')
  

class Customer(models.Models):

    _name = "customer.info"
    _description = "customer info"

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Age')
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
        ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],string='Blood Group')
    city =fields.Selection([('j', 'Junagadh'), ('r', 'Rajkot'), ('a', 'Ahmedabad')], string='City')    
    nationality = fields.Char(string='Nationality')
    customer_id = fields.Many2one('insurance.info', string="customer")
    customer_ids = fields.Many2many('insurance.info','insurance_rel','customer_id','insurance_ids',string="customer")
  