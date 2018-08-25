# Ref: https://github.com/dkarchmer/aws-eb-docker-django/blob/master/authentication/management/commands/initadmin.py
#      https://stackoverflow.com/questions/30027203/create-django-super-user-in-a-docker-container-without-inputting-password

from django.conf import settings
from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        Account = get_user_model()

        if Account.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = 'admin'
                print('Creating account for %s (%s)' % (username, email))
                admin = Account.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
