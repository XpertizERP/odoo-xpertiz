from odoo import api, models, fields, _

class ProjectTask(models.Model):
    _inherit='project.task'
    
    @api.multi
    def action_open_helpdesk_ticket(self):
        action = self.env.ref('helpdesk.helpdesk_ticket_action_main_tree').read()[0]
        action['context'] = {}
        action['domain'] = [('task_id', 'child_of', self.ids)]
        return action
    
    ticket_count = fields.Integer("Tickets", compute='_compute_ticket_count')

    def _compute_ticket_count(self):
        # retrieve all children tasks and prefetch 'parent_id' on them
        all_tasks = self.search([('id', 'child_of', self.ids)])
        all_tasks.read(['parent_id'])

        # group tickets by task, and account for each task in self
        groups = self.env['helpdesk.ticket'].read_group(
            [('task_id', 'in', all_tasks.ids)],
            fields=['task_id'], groupby=['task_id'],
        )
        for group in groups:
            task = self.browse(group['task_id'][0])
            while task:
                if task in self:
                    task.ticket_count += group['task_id_count']
                task = task.parent_id
                
        