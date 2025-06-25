{
    'name': 'Project Task Hierarchy',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Adds a hierarchical Task → Sub-task tree view under Project',
    'description': """Provides a new menu item showing tasks nested by their parent-child relationship, leveraging the built-in parent_id/children_ids fields.""" ,
    'author': 'Your Name',
    'depends': ['project'],
    'data': ['views/project_task_hierarchy_views.xml'],
    'installable': True,
    'application': False,
    'auto_install': False
}
