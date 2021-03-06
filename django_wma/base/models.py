from django.db import models
from django.utils.translation import ugettext_lazy as _

import swapper

class AbstractContainer(models.Model):
    name = models.CharField(help_text=_('Container name'), max_length=30)
    volume = models.BigIntegerField(help_text=_('Volume of the container in cubic metres.'))
    base_area = models.BigIntegerField(help_text=_('Base area of the container in square metres.'))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = _('Container')
        verbose_name_plural = _('Containers')


class AbstractWaterQuantity(models.Model):
    container = models.ForeignKey(to=swapper.get_model_name('django_wma', 'Container'),
                                  on_delete=models.CASCADE)
    volume = models.BigIntegerField(help_text=_('Volume of django_wma available in cubic metres'))
    height = models.BigIntegerField(help_text=_('Height of django_wma level in metres'))

    def __str__(self):
        return "{}'s quantity".format(str(self.container.name))

    class Meta:
        abstract = True
        verbose_name = _('Water Quantity')
        verbose_name_plural = _('Water Quantity')


class AbstractWaterQuality(models.Model):
    container = models.ForeignKey(to=swapper.get_model_name('django_wma', 'Container'),
                                  on_delete=models.CASCADE)
    ph = models.DecimalField(help_text=_('pH'),
                             max_digits=10,
                             decimal_places=8)
    do = models.DecimalField(help_text=_('Dissolved oxygen in mg/l'),
                             max_digits=10,
                             decimal_places=3)
    orp = models.DecimalField(help_text=_('Oxidation reduction potential in mV'),
                              max_digits=10,
                              decimal_places=6)
    conductivity = models.DecimalField(help_text=_('Conductivity in uS/cm'),
                                       max_digits=10,
                                       decimal_places=3)
    turbidity = models.DecimalField(help_text=_('Turbidity in NTU'),
                                    max_digits=10,
                                    decimal_places=3)
    temperature = models.DecimalField(help_text=_('Temperature in kelvin'),
                                      max_digits=10,
                                      decimal_places=5)
    """
    Dissolved ion concentrations in mg/l
    """
    fluoride = models.DecimalField(help_text=_('Fluoride ion concentration in mg/l'),
                                   max_digits=20,
                                   decimal_places=10)
    calcium = models.DecimalField(help_text=_('Calcium ion concentration in mg/l'),
                                  max_digits=20,
                                  decimal_places=10)
    nitrate = models.DecimalField(help_text=_('Nitrate ion concentration in mg/l'),
                                  max_digits=20,
                                  decimal_places=10)
    chloride = models.DecimalField(help_text=_('Chloride ion concentration in mg/l'),
                                   max_digits=20,
                                   decimal_places=10)
    iodide = models.DecimalField(help_text=_('Iodide ion concentration in mg/l'),
                                 max_digits=20,
                                 decimal_places=10)
    cupric = models.DecimalField(help_text=_('Cupric ion concentration in mg/l'),
                                 max_digits=20,
                                 decimal_places=10)
    bromide = models.DecimalField(help_text=_('Bromide ion concentration in mg/l'),
                                  max_digits=20,
                                  decimal_places=10)
    silver = models.DecimalField(help_text=_('Silver ion concentration in mg/l'),
                                 max_digits=20,
                                 decimal_places=10)
    fluoroborate = models.DecimalField(help_text=_('Fluoroborate ion concentration in mg/l'),
                                       max_digits=20,
                                       decimal_places=10)
    ammonium = models.DecimalField(help_text=_('Ammonium ion concentration in mg/l'),
                                   max_digits=20,
                                   decimal_places=10)
    lithium = models.DecimalField(help_text=_('Lithium ion concentration in mg/l'),
                                  max_digits=20,
                                  decimal_places=10)
    magnesium = models.DecimalField(help_text=_('Magnesium ion concentration in mg/l'),
                                    max_digits=20,
                                    decimal_places=10)
    nitrite = models.DecimalField(help_text=_('Nitrite ion concentration in mg/l'),
                                  max_digits=20,
                                  decimal_places=10)
    perchlorate = models.DecimalField(help_text=_('Perchlorate ion concentration in mg/l'),
                                      max_digits=20,
                                      decimal_places=10)
    potassium = models.DecimalField(help_text=_('Potassium ion concentration in mg/l'),
                                    max_digits=20,
                                    decimal_places=10)
    sodium = models.DecimalField(help_text=_('Sodium ion concentration in mg/l'),
                                 max_digits=20,
                                 decimal_places=10)

    def __str__(self):
        return "{}'s quality".format(str(self.container))

    class Meta:
        abstract = True
        verbose_name = _('Water Quality')
        verbose_name_plural = _('Water Quality')
