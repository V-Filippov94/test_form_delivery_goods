from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import AddressIssuance, Product


class AddressIssuanceForm(ModelForm):
    class Meta:
        model = AddressIssuance
        exclude = ()


AddressIssuanceFormSet = inlineformset_factory(Product, AddressIssuance, form=AddressIssuanceForm, extra=1,
                                               can_delete=False)
