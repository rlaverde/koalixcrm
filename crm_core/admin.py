# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from reversion.admin import VersionAdmin
from cartridge.shop import models as cartridge_models
from cartridge.shop.admin import admin as cartridge_admin

from .models import UserExtension, Customer, Invoice, PurchaseOrder, Quote, Supplier, HTMLFile, TemplateSet, \
    CustomerBillingCycle, CustomerGroup, Contract, Unit, TaxRate, \
    UnitTransform, CompanyContactData


# Define an inline admin descriptor
# which acts a bit like a singleton
class CRMUserProfileInline(admin.TabularInline):
    model = UserExtension
    can_delete = False
    extra = 1
    max_num = 1
    verbose_name_plural = _('User Profile Extensions')


# Define a new User admin
class NewUserAdmin(UserAdmin):
    inlines = (CRMUserProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)


class CustomerBillingCycleAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (u'id', 'name', 'days_to_payment')
    search_fields = ('name',)


admin.site.register(CustomerBillingCycle, CustomerBillingCycleAdmin)


class CustomerGroupAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (u'id', 'name')
    search_fields = ('name',)


admin.site.register(CustomerGroup, CustomerGroupAdmin)


class CustomerAdmin(VersionAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'prefix',
        'name',
        'firstname',
        'default_currency',
        'billingcycle',
        'dateofcreation',
        'lastmodification',
        'lastmodifiedby',
    )
    list_filter = (
        'billingcycle',
        'dateofcreation',
        'lastmodification',
        'lastmodifiedby',
    )
    raw_id_fields = ('ismemberof',)
    search_fields = ('name',)
    exclude = ('lastmodifiedby',)


admin.site.register(Customer, CustomerAdmin)


class SupplierAdmin(VersionAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'prefix',
        'name',
        'default_currency',
        'direct_shipment_to_customers',
        'dateofcreation',
        'lastmodification',
        'lastmodifiedby',
    )
    list_filter = (
        'direct_shipment_to_customers',
        'dateofcreation',
        'lastmodification',
        'lastmodifiedby',
    )
    search_fields = ('name',)


admin.site.register(Supplier, SupplierAdmin)


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'state',
        'default_customer',
        'default_supplier',
        'description',
        'default_currency',
        'staff',
        'dateofcreation',
        'lastmodification',
        'lastmodifiedby',
    )
    list_filter = (
        'default_customer',
        'default_supplier',
        'staff',
        'dateofcreation',
        'lastmodification',
        'lastmodifiedby',
    )


admin.site.register(Contract, ContractAdmin)


class PurchaseOrderAdmin(VersionAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'contract',
        'customer',
        'validuntil',
        'discount',
        'staff',
        'lastmodifiedby',
    )
    list_filter = (
        'validuntil',
        'contract',
        'customer',
        'staff',
        'lastmodifiedby',
    )


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


class QuoteAdmin(VersionAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'contract',
        'customer',
        'validuntil',
        'discount',
        'staff',
        'lastmodifiedby',
    )
    list_filter = (
        'validuntil',
        'contract',
        'customer',
        'staff',
        'lastmodifiedby',
    )


admin.site.register(Quote, QuoteAdmin)


class InvoiceAdmin(VersionAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'contract',
        'customer',
        'payableuntil',
        'discount',
        'staff',
        'lastmodifiedby',
    )
    list_filter = (
        'payableuntil',
        'contract',
        'customer',
        'staff',
        'lastmodifiedby',
    )


admin.site.register(Invoice, InvoiceAdmin)


class UnitAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'shortname',
        'description',
        'fractionof',
        'factor',
    )
    list_filter = ('fractionof',)


admin.site.register(Unit, UnitAdmin)


class TaxRateAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'name',
        'taxrate_in_percent',
    )
    search_fields = ('name',)


admin.site.register(TaxRate, TaxRateAdmin)


class UnitTransformAdmin(admin.ModelAdmin):
    list_display = (u'id', 'from_unit', 'to_unit', 'product', 'factor')
    list_filter = ('from_unit', 'to_unit', 'product')


admin.site.register(UnitTransform, UnitTransformAdmin)


class HTMLFileAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (u'id', 'title', 'file')


admin.site.register(HTMLFile, HTMLFileAdmin)


class TemplateSetAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        u'id',
        'invoice_html_file',
        'quote_html_file',
        'purchaseorder_html_file',
    )
    list_filter = (
        'invoice_html_file',
        'quote_html_file',
        'purchaseorder_html_file',
    )

admin.site.register(TemplateSet, TemplateSetAdmin)


class CompanyContactDataAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    list_display = (
        'name',
    )

admin.site.register(CompanyContactData, CompanyContactDataAdmin)
