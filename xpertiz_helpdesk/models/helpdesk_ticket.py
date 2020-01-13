from odoo import api, fields, models, _
from odoo.exceptions import UserError

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
    @api.multi
    def generate_task(self):
        context = { 'default_name':self.name,
                    'default_project_id':self.project_id.id if self.project_id else False,
                    'default_partner_id':self.partner_id.id if self.partner_id else False,
                    'default_user_id':self.user_id.id if self.user_id else False,
                    'default_description':self.description,
                    'default_partner_email':self.partner_email,
                    'default_helpdesk_ticket_id':self.id}
        return {
            'name': _('Generate Task from Ticket'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ticket.task',
            'view_id': False,
            'target': 'new',
            'context':context,
            'type': 'ir.actions.act_window',
        }
        
class TicketTask(models.TransientModel):
    _name = 'ticket.task'
    
    name = fields.Char(string='Name', size=32, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=False, ondelete='restrict')
    partner_email = fields.Char(string='Customer Email', size=32, required=False)
    user_id = fields.Many2one('res.users', string='Assigned to', required=False, ondelete='restrict')
    project_id = fields.Many2one('project.project', string='Project', required=True, ondelete='restrict')
    description = fields.Text(string='Description')
    helpdesk_ticket_id = fields.Many2one('helpdesk.ticket', string='Helpdesk Ticket', required=False, ondelete='restrict')
    
    @api.multi
    def generate_task(self):
        project_id = self.project_id
        if not project_id :
            raise UserError(_('You must choose a project before generating the task.'))
        vals = {'project_id':project_id.id,
                'name':self.name,
                'partner_id':self.partner_id.id if self.partner_id else False,
                'user_id':self.user_id.id if self.user_id else False,
                'description':self.description,
                'partner_email':self.partner_email,
                }
        task_id = self.env['project.task'].create(vals)
        self.helpdesk_ticket_id.task_id=task_id.id
        return self.action_view_task(task_id)
        
        
        
    @api.multi
    def action_view_task(self, task_id):
        action = self.env.ref('project.action_view_task').read()[0]
        form_view = [(self.env.ref('project.view_task_form2').id, 'form')]
        if 'views' in action:
            action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
        else:
            action['views'] = form_view
        action['res_id'] = task_id.id
        return action