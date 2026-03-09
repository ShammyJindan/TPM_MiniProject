from odoo import models, fields, api

class InternEmployee(models.Model):
    _name = 'intern.employee'
    _description = 'Intern Employee Tracker'

    name = fields.Char(string='Nama Karyawan', required=True)
    position = fields.Char(string='Posisi')
    base_salary = fields.Float(string='Gaji Pokok')
    bonus = fields.Float(string='Bonus (10%)', compute='_compute_bonus')

    @api.depends('base_salary')
    def _compute_bonus(self):
        for rec in self:
            rec.bonus = rec.base_salary * 0.1