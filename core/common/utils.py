from rest_framework.fields import SerializerMethodField

from django.contrib.humanize.templatetags.humanize import naturaltime


class HumanizedCreatedSinceField(SerializerMethodField):
    def to_representation(self, obj):
        return naturaltime(obj.created)


class HumanizedModifiedSinceField(SerializerMethodField):
    def to_representation(self, obj):
        return naturaltime(obj.modified)
