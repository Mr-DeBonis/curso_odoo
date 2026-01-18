from odoo import models
from odoo import fields


class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Grades Course'


    name = fields.Char(string='Name')
    student_qty = fields.Integer(String='Student quantity')
    grades_average = fields.Float(String='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is active')
    course_start = fields.Date(string='Course start')
    course_end = fields.Date(string='Course end')
    last_evaluation_date = fields.Datetime(string='Last evaluation date')
    course_image = fields.Binary(string='Course image')
    course_shift = fields.Selection([('day', 'Day'), ('night', 'Night')], string='Course shift')
