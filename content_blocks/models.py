from django.db import models
from django.conf import settings

class Block(models.Model):
    """A block is a piece of content that can be assigned to
    a template position as defined in settings.py, the content
    is then insterted into the template via a special template
    tag."""
    
    NO_POSITION = 'None'
    
    POSITION_CHOICES = getattr(settings, 'CONTENTBLOCKS_POSITION_CHOICES', [(NO_POSITION, u'None')])
    
    #This check ensures that NO_POSITION is not listed twice if no extra options are given in settings.
    if POSITION_CHOICES[0][0] != NO_POSITION:
        POSITION_CHOICES.insert(0, (NO_POSITION, 'None'))
    
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    template_position = models.CharField(max_length=50, choices=POSITION_CHOICES, default=NO_POSITION)
    content = models.TextField()

    def __unicode__(self):
        return u'%s' % self.title