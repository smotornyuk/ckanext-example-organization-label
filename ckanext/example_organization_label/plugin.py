import ckan.plugins as plugins

from ckan.lib.plugins import DefaultTranslation

class ExampleOrganizationLabelPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
