from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GradesGrade(models.Model):
    _name = "grades.grade"
    _description = "Grades grade"

    student_id = fields.Many2one('res.partner', String='Student')
    value = fields.Integer(String='Value')
    date = fields.Date(String='Date', default=fields.Date.today())
    evaluation_id = fields.Many2one('grades.evaluation', String='Evaluation', readonly=True)

    @api.constrains('value')
    def _check_value(self):
        for grade in self:
            if grade.value < 0 or grade.value > 10:
                raise ValidationError("The grade has to be from 0 to 10")
