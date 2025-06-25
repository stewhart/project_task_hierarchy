{
    'name': 'Project Task Hierarchy',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Adds a hierarchical Task → Sub-task tree view under Project and clipboard fallback for error dialogs',
    'description': """Provides a new menu item showing tasks nested by their parent-child relationship,
leveraging the built-in parent_id/children_ids fields, and adds a JS patch
for clipboard fallback in RPC error dialogs.""" ,
    'author': 'Your Name',
    'depends': ['project', 'web'],
    'data': ['views/project_task_hierarchy_views.xml'],
    'assets': {
        'web.assets_backend': [
            'project_task_hierarchy/static/src/js/error_dialog_clipboard.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
