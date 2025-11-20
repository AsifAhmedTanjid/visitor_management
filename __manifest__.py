{
    "name": "Visitor Management",
    "version": "1.0",
    "depends": ["base",'hr'],
    "author": "Asif",
    "category": "Tools",
    "description": "Manage visitor check-in and check-out",
    "data": [
        "security/ir.model.access.csv",
        "views/visitor_views.xml",
        'views/hr_employee_views.xml',
        'views/menu.xml',
        "reports/visitor_card_report.xml",
    ],
    "installable": True,
    "application": True,
}
