from django.contrib import admin
from .models import AnimeVariety, AnimeReview , Store , AnimeCertificate, AnimeUA

# Register your models here.
class AnimeReviewInline(admin.TabularInline):
    model = AnimeReview
    extra = 1

class AnimeUAInline(admin.TabularInline):
    model = AnimeUA
    extra = 1

class AnimeVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'date_added')
    inlines = [AnimeReviewInline, AnimeUAInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('anime_varities',)

class AnimeCertificateAdmin(admin.ModelAdmin):
    list_display = ('anime', 'certificate_number', 'issued_date', 'valid_until')




admin.site.register(AnimeVariety, AnimeVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AnimeCertificate, AnimeCertificateAdmin)
