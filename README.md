# django-auto-repr

This is a tiny project to quickly give Django models a usable `repr()`.  To use
it, have your models inherit from `django_auto_repr.AutoRepr`, e.g.:

    from django.db import models
    from django_auto_repr import AutoRepr


    class Product(AutoRepr, models.Model):
        name = models.CharField(max_length=255)
        qty = models.IntegerField()

With this definition, your REPL sesssions will look like this:

    >>> Product.objects.first()
    Product(id=1, name='My Product', qty=3)

In addition to being more readable, this representation has the additional
benefit, shared by Python standard library classes like Decimal and OrderedDict,
that it can be copied and pasted back into the REPL to construct an equivalent
object.
