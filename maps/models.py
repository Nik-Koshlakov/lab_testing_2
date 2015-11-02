from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    class Meta:
        verbose_name = _(u'City')
        verbose_name_plural = _(u'Cities')

    name = models.CharField(verbose_name=_(u'Name'), unique=True, max_length=100)
    coord_X = models.IntegerField(verbose_name=_(u'X coordinate'))
    coord_Y = models.IntegerField(verbose_name=_(u'Y coordinate'))
    map = models.ForeignKey('Map', verbose_name=_(u'Map'))

    def __unicode__(self):
        return u'%s' % self.name


class Distance(models.Model):
    class Meta:
        verbose_name = _(u'Distance')
        verbose_name_plural = _(u'Distances')

    city_from = models.ForeignKey('City', related_name='distances_from', verbose_name=_(u'City from'))
    city_to = models.ForeignKey('City', related_name='distances_to', verbose_name=_(u'City to'))
    value = models.PositiveIntegerField(verbose_name=_(u'Value'))


class Map(models.Model):
    name = models.CharField(verbose_name=_(u'Name'), unique=True, max_length=100)

    def __unicode__(self):
        return u'%s' % self.name
