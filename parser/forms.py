from django import forms
from . import models, house_parser, bazar_parser


class ParserForm(forms.Form):
    CHOICES = (
        ('house.kg', 'house.kg'),
        ('bazar.kg', 'bazar.kg'),
    )

    type = forms.ChoiceField(choices=CHOICES)

    class Meta:
        fields = ['type']

    def parser_data(self):
        if self.data['type'] == 'house.kg':
            houses = house_parser.get_houses()
            for house in houses:
                models.HouseParser.objects.create(**house)
        elif self.data['type'] == 'bazar.kg':
            items = bazar_parser.get_items()
            for item in items:
                models.BazarParser.objects.create(**item)
