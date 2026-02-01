from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Is Teacher')
    is_freelance = fields.Boolean(string='Is freelance')
    is_student = fields.Boolean(string='Is student')
    vat = fields.Char(required=True, copy=False)

    def unlink(self):
        for partner in self:
            if partner.email == 'mainteacher@mail.com':
                courses = self.env['grades.course'].search([('teacher_id', '=', partner.id)])
                secondary_teacher = self.env['res.partner'].search([('email', '=', 'secundario@mail.com')])
                courses.write({'teacher_id': secondary_teacher.id})
        result = super(ResPartner, self).unlink()
        return result

    def copy(self, default=None):
        default = default or {}
        if self.is_teacher:
            default['name'] = 'Teacher'
        if self.is_student:
            default['name'] = 'Student'

        res = super(ResPartner, self).copy(default)
        return res