from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import transaction

# Register your models here.
# Register your models here.
admin.site.site_header  =  "Treez admin" 
admin.site.site_title  =  "Treez admin site"
admin.site.index_title  =  "Treez Admin"

class transactionAdmin(ImportExportMixin, admin.ModelAdmin):
    """
    This class is used to display the transaction model in the admin page.
    """
    list_display = ('swifter_id', 'external_id', 'customer', 'source', 'gross_amount', 'date', 'status')

admin.site.register(transaction, transactionAdmin)


