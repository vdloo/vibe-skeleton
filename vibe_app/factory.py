import factory

from vibe_app.models import SomeModel


class SomeModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SomeModel

    some_field = 'default'
