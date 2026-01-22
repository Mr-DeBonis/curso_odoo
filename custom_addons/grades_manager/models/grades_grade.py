from odoo import models, fields


class GradesGrade(models.Model):
    _name = "grades.grade"
    _description = "Grades grade"

    student_id = fields.Many2one('res.partner', String='Student')
    value = fields.Integer(String='Value')
    date = fields.Date(String='Date', default=fields.Date.today())
    evaluation_id = fields.Many2one('grades.evaluation', String='Evaluation', readonly=True)
