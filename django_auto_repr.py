from django.db import models


class AutoRepr(object):
    """A model mixin that generates a useful __repr__"""

    def _repr_format_field(self, field):
        """Get a "bar='bar_value'" str.

        field is a Django Field object.
        """
        if isinstance(field, models.ForeignKey):
            field_name = field.name + '_id'
        else:
            field_name = field.name

        field_value = getattr(self, field_name)

        default = field.default
        if field_value == default:
            return ''
        elif default is models.NOT_PROVIDED:
            if isinstance(field, models.CharField) and field_value == '':
                return ''
            if field_value is None:
                return ''
        return "{}={!r}".format(field_name, field_value)

    def __repr__(self):
        cls = type(self)
        fields = cls._meta.fields
        parts = filter(None, map(self._repr_format_field, fields))
        attrs = ', '.join(parts)
        return '{}({})'.format(cls.__name__, attrs)

