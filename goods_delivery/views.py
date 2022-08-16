from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *


class ShowFormDelivery(CreateView):
    model = Product
    fields = ['name', 'type', 'date_delivery', 'file']
    success_url = reverse_lazy('form_delivery')
    template_name = 'goods_delivery/form.html'

    def get_context_data(self, **kwargs):
        data = super(ShowFormDelivery, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address_issuance'] = AddressIssuanceFormSet(self.request.POST)
        else:
            data['address_issuance'] = AddressIssuanceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address_issuance = context['address_issuance']
        with transaction.atomic():
            self.object = form.save()
            if address_issuance.is_valid():
                address_issuance.instance = self.object
                address_issuance.save()
        return super(ShowFormDelivery, self).form_valid(form)



