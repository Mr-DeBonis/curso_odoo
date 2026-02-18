from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Grades Course'

    def _default_teacher_id(self):
        teacher = (self.env['res.partner']
                   .search([('is_teacher', '=', True), ('email', '=', 'mainteacher@mail.com')], limit=1))
        return teacher.id

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student quantity', compute='_computed_student_qty', store=True)
    grades_average = fields.Float(string='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is active')
    course_start = fields.Date(string='Course start', default=fields.Date.today())
    course_end = fields.Date(string='Course end')
    last_evaluation_date = fields.Date(string='Last evaluation date', compute='_computed_last_evaluation_date',
                                           store=True)
    course_image = fields.Binary(string='Course image')
    course_shift = fields.Selection([('day', 'Day'), ('night', 'Night')], string='Course shift')
    teacher_id = fields.Many2one('res.partner', string='Teacher', default=_default_teacher_id)
    teacher_email = fields.Char(related='teacher_id.email', store=True)
    evaluation_ids = fields.One2many('grades.evaluation', 'course_id', string='Evaluations')
    student_ids = fields.Many2many('res.partner', 'grades_course_students_rel', string='Students')
    state = fields.Selection([('register', 'Register'), ('in_progress', 'In progress'), ('finished', 'Finished')],
                             string='State', default='register')
    invalid_dates = fields.Boolean(string='Invalid dates')
    type = fields.Selection([('basic', 'Basic'), ('advanced', 'Advanced')], string='Type', default='basic')

    def write(self, vals):
        if vals and 'evaluation_ids' in vals and not self.student_ids:
            raise ValidationError('There are no students for this course')
        result = super(GradesCourse, self).write(vals)
        return result
        
    @api.onchange('course_start', 'course_end')
    def onchange_dates(self):
        if (self.course_start and self.course_end) and (self.course_start >= self.course_end):
            self.invalid_dates = True
        else:
            self.invalid_dates = False

    @api.depends('evaluation_ids.date')
    def _computed_last_evaluation_date(self):
        for course in self:
            if course.evaluation_ids:
                evaluation = course.evaluation_ids[-1]
                course.last_evaluation_date = evaluation.date

    @api.depends('student_ids')
    def _computed_student_qty(self):
        for course in self:
            course.student_qty = len(course.student_ids)