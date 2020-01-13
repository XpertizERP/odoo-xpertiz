# -*- coding: utf-8 -*-
{
    'name' : 'Helpdesk Customization',
    'version' : '12.0.1',
    'author' : 'XPERTIZ SA',
    'category' : 'HELPDESK',
    'description' : """ HELPDESK """,
    'website': 'https://xpertiz.lu',
    'images' : [],
    'depends' : [
             'helpdesk_timesheet',
             'project'
                ],
                
    'data': [
             'views/helpdesk_ticket_views.xml',
             'views/project_task_views.xml'
             ],
             
    'qweb' : [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}