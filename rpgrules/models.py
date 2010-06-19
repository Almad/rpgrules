from django.db import models
#from django.utils.translation import ugettext_lazy as _

class Rule(models.Model):
    """
    Rule is "rpg rule". As we're not so intrested into details as rpgdb, definition
    of rule is 'something we want to create extensions for and take track for it'

    Exact difference between where custom edition should be added and new rule
    is left to admins.
    Parent rule is used for hiearchy (as in 'DrD', 'DrD 1.6')
    """

    parent = models.ForeignKey('self', default=None, null=True, blank=True)
    name = models.CharField(max_length=150)
    