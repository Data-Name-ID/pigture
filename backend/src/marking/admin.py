import django.contrib

import marking.models


@django.contrib.admin.register(marking.models.Category)
class CategoriesAdmin(django.contrib.admin.ModelAdmin):
    list_display = (marking.models.Category.name.field.name,)


@django.contrib.admin.register(marking.models.Tag)
class TagsAdmin(django.contrib.admin.ModelAdmin):
    list_display = (marking.models.Tag.name.field.name,)
