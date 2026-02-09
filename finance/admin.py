from django.contrib import admin
from .models import Transaction, Goal
from import_export import resources
from import_export.admin import ExportMixin

# Fix resource class
class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        # Correct field name
        fields = ('date', 'title', 'amount', 'transaction_type', 'category')

class TransactionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TransactionResource  # singular, not list
    list_display = ('date', 'title', 'amount', 'transaction_type', 'category')  # fix typo
    search_fields = ('title',)

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Goal)
