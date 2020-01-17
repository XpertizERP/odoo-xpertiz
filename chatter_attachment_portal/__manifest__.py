{
    'name' : 'Chatter Portal Attachment',
    'version' : '12.0',
    'author' : 'Mohamed Mejdi, Xpertiz SA',
    'category' : 'Website',
    'description' : """ Allow users to attach multiple attachments with chatter comments/messages. """,
    'website': 'https://xpertiz.lu',
    'images' : [],
    'depends' : [
             'portal','website'
                ],
                
    'data': [
             'views/templates.xml',
             ],
             
    'qweb' : ['static/src/xml/*.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}