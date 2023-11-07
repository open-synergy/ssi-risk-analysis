import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-risk-analysis",
    description="Meta package for open-synergy-ssi-risk-analysis Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_risk_analysis',
        'odoo14-addon-ssi_risk_analysis_project',
        'odoo14-addon-ssi_risk_analysis_reference_document',
        'odoo14-addon-ssi_risk_analysis_related_attachment',
        'odoo14-addon-ssi_risk_analysis_work_log',
        'odoo14-addon-ssi_risk_analysis_worksheet_related_attachment',
        'odoo14-addon-ssi_risk_management',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
