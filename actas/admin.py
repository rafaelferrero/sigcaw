from django.contrib import admin
from actas.models import (
    Acta,
)


'''
El acta es abstracto, se debe poner solo las actas especificas

@admin.register(Acta)
class ActaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'numero_acta',
                'fecha_acta',
                'numero_folio',
                'numero_libro',
                'descripcion_acta',
                )
        }),
    )
    list_display = (

            'numero_acta',
            'fecha_acta',
            'numero_folio',
            'numero_libro',
            'descripcion_acta',
            )
    search_fields = (
            'numero_acta',
            'fecha_acta',
            'numero_folio',
            'numero_libro',
            'descripcion_acta',
            )
#agregar el campo descripcion_acta.
'''