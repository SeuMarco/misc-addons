{
    'name': 'Odoo Web Sessions Management Rules',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Manage Users Login Rules in Odoo.',
    'description': """
# Manage Users Login Rules in Odoo\n
===========================\n
\n
This modules allows the management of logins, by groups or users.\n\n
One can do following:\n
# Group/User Login Configuration:\n
1. Allow multiple sign in of same user;\n
2. Define session timeouts;\n
3. Define a time/week day where users can login;\n
4. You can have user exceptions, overwriting group settings in user settings. The most restrict rule will be applied.\n\n
# Administrator Session Management:\n
1. Sessions log;\n
2. Group by session state, login date time, logout date time, user, group;\n
3. Close any active session.\n\n
# User Session Management:\n
1. Users can see their own log of sessions;\n
2. Users can close related active session;\n
3. Users can choose to close all sessions except current one.\n
NOTE: Admin has no restrictions""",
    'author': 'ThinkOpen Solutions Brasil, IT-Projects LLC, Ivan Yelizariev',
    'website': 'http://www.tkobr.com',
    'depends': [
                'share',
                'base',
                'resource',
                'web',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/scheduler.xml',
        'views/res_users_view.xml',
        'views/res_groups_view.xml',
        'views/ir_sessions_view.xml',
        'views/webclient_templates.xml',
    ],
    'init': [],
    'demo': [],
    'update': [],
    'test': [],  # YAML files with tests
    'installable': False,
    'application': False,
    'auto_install': False,  # If it's True, the modules will be auto-installed when all dependencies are installed
    'certificate': '',
    "post_load": 'post_load',
}
