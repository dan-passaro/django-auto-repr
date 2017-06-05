from django.db import models


class AutoRepr(models.Model):
    """A model mixin that generates a useful __repr__"""

    def _repr_format_field(self, field):
        """Get a "bar='bar_value' str.

        field is a Django Field
        """
        if isinstance(field, models.ForeignKey):
            field_name = field.name + '_id'
        else:
            field_name = field.name
        return f'{field_name}={getattr(self, field_name)!r}'

    def __repr__(self):
        cls = type(self)
        fields = cls._meta.fields
        parts = map(self._repr_format_field, fields)
        attrs = ', '.join(parts)
        return f'{cls.__name__}({attrs})'

    class Meta:
        abstract = True
