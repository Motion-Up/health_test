from django import forms


CHOICE_FOR_TEST = [
    (1, '1'),
    (2, '2'),
    (3, '3')
]


class TestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, parameter in self.initial.items():
            if parameter.field_type == 'int':
                self.fields[name] = forms.FloatField(
                    label=name,
                    widget=forms.NumberInput(
                        attrs={
                            'class': "form-control w-25 p-1",
                            'id': name,
                        }
                    )
                )
            elif parameter.field_type == 'bool':
                self.fields[name] = forms.BooleanField(
                    label=name,
                    required=False,
                    widget=forms.CheckboxInput(attrs={
                        'class': "form-check-input p-2",
                        'id': name,
                    })
                )
            elif parameter.field_type == 'choice':
                self.fields[name] = forms.ChoiceField(
                    choices=CHOICE_FOR_TEST,
                    label=name,
                    widget=forms.Select(attrs={
                        'class': "form-select w-25",
                        'id': name,
                    })
                )
