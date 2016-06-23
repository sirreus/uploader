from django.contrib import admin

# Register your models here.
from .models import Document

class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated_at","name"]
    search_fields = ["title", "name"]
    class Meta:
        model = Document

admin.site.register(Document, DocumentModelAdmin)
