from django.contrib import admin
from .models import Card, Tag, Deck

class CardAdmin(admin.ModelAdmin):
    verbose_name = "Carte"
    verbose_name_plural = "Cartes"
    def display_tags(self, obj):
        # Get the tags for the object
        tags = obj.tags.all()
        # Return a string with the tag names separated by commas
        return ', '.join([tag.tag for tag in tags])
    
    display_tags.short_description = 'Tags'

    readonly_fields = ('modified_date', 'created_date')

    list_display = ('__str__', 'text', 'display_tags', 'type', 'public', 'user', 'modified_date', 'created_date',
    )
    list_filter = ['modified_date', 'created_date']

    search_fields = ['text']
admin.site.register(Card, CardAdmin)

admin.site.register(Tag)

class DeckAdmin(admin.ModelAdmin):
    verbose_name = "Paquet de cartes"
    verbose_name_plural = "Paquets de cartes"

    def cards_count(self, obj):
        return obj.cards.count()
    cards_count.short_description = 'Nombre de cartes'

    readonly_fields = ['created_date']

    list_display = ['name', 'cards_count', 'public', 'user']
    list_filter = ['created_date']

    search_fields = ['name']
admin.site.register(Deck, DeckAdmin)