from odoo import models, fields, api

class InternLeaveRequest(models.Model):
    _name = 'intern.leave.request'
    _description = 'Intern Leave Request'

    name = fields.Many2one('intern.employee', string='Nama Karyawan', required=True)
    start_date = fields.Date(string='Tanggal Mulai', required=True)
    end_date = fields.Date(string='Tanggal Selesai', required=True)
    reason = fields.Text(string='Alasan Cuti', required=True)
    