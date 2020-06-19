from flask.views import MethodView

from apispec import BasePlugin, yaml_utils


class FlaskPlugin(BasePlugin):
    """APISpec plugin for Flask"""

    ...

    def path_helper(self, operations, *, view, app=None, **kwargs):
        """Path helper that allows passing a Flask view function."""

        import pdb; pdb.set_trace()

        rule = self._rule_for_view(view, app=app)
        operations.update(yaml_utils.load_operations_from_docstring(view.__doc__))
        if hasattr(view, "view_class") and issubclass(view.view_class, MethodView):
            for method in view.methods:
                if method in rule.methods:
                    method_name = method.lower()
                    method = getattr(view.view_class, method_name)
                    operations[method_name] = yaml_utils.load_yaml_from_docstring(
                        method.__doc__
                    )
        return self.flaskpath2openapi(rule.rule)
