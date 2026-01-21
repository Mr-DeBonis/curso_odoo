from odoo import models
from odoo import fields


class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Grades Course'

    def _default_teacher_id(self):
        teacher = (self.env['res.partner']
                   .search([('is_teacher', '=', True), ('email', '=', 'mainteacher@mail.com')], limit=1))
        return teacher.id

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student quantity', readonly=True)
    grades_average = fields.Float(string='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is active')
    course_start = fields.Date(string='Course start', default=fields.Date.today())
    course_end = fields.Date(string='Course end')
    last_evaluation_date = fields.Datetime(string='Last evaluation date')
    course_image = fields.Binary(string='Course image')
    course_shift = fields.Selection([('day', 'Day'), ('night', 'Night')], string='Course shift')
    teacher_id = fields.Many2one('res.partner', string='Teacher', default=_default_teacher_id)
    evaluation_ids = fields.One2many('grades.evaluation', 'course_id', string='Evaluations')
    student_ids = fields.Many2many('res.partner', 'grades_course_students_rel', string='Students')
    state = fields.Selection([('register', 'Register'), ('in_progress', 'In progress'), ('finished', 'Finished')],
                             string='State', default='register')
