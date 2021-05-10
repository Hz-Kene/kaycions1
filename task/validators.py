from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
'''
def fullnameValidator(value):
    qwerty = value.split()
    if len(qwerty) >= 2:
        return value
    else:
        raise ValidationError('Please input at least two names without digits')
'''

full_regex_pattern = RegexValidator(regex=r'^[a-zA-Z]+\s[a-zA-Z]*$', message='Please input only two names without digits or special characters',)



def usernameValidator(value):
    if len(value) < 5:
        raise ValidationError(_('\'%(value)s\' is too short. (Use 5 chars or more)'), params={'value':value},)
    else:
        return value

def fullnameValidator(value):
    if len(value) < 6:
        raise ValidationError(_('\'%(value)s\' is too short. (Use 6 chars or more)'), params={'value':value},)
    else:
        return value

def twitterIdValidator(value):
    if not value.startswith('@'):
        raise ValidationError('Invalid Id. Please start with the \'@\' symbol')

def instagramIdValidator(value):
    if not value.startswith('@'):
        raise ValidationError('Invalid Id. Please start with the \'@\' symbol')

def youtubeIdValidator(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Invalid Id. Please use a valid Gmail address')
