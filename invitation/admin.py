from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count, Q

from .models import Invitation, InvitationEvent, GalleryPhoto, Rsvp


# ============================================================
# INLINES
# ============================================================
class InvitationEventInline(admin.TabularInline):
    model = InvitationEvent
    extra = 1
    fields = ('order', 'title', 'date_time', 'venue')
    ordering = ('order', 'date_time')


class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 1
    fields = ('order', 'image', 'thumbnail', 'caption')
    readonly_fields = ('thumbnail',)
    ordering = ('order', 'id')

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:8px;object-fit:cover;" />',
                obj.image.url,
            )
        return "—"
    thumbnail.short_description = "پیش‌نمایش"


class RsvpInline(admin.TabularInline):
    model = Rsvp
    extra = 0
    fields = ('name', 'phone', 'attending', 'guests_count', 'created_at')
    readonly_fields = ('name', 'phone', 'attending', 'guests_count', 'created_at')
    can_delete = False
    show_change_link = True
    ordering = ('-created_at',)

    def has_add_permission(self, request, obj=None):
        return False


# ============================================================
# INVITATION ADMIN
# ============================================================
@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        'couple_display', 
        'main_photo_thumb', 
        'wedding_date',
        'venue_name', 
        'events_count', 
        'gallery_count', 
        'rsvp_summary',
        'has_rsvp_url',  # اضافه شد
    )
    list_display_links = ('couple_display',)
    search_fields = ('bride_name', 'groom_name', 'venue_name', 'venue_address', 'rsvp_url')
    list_filter = ('wedding_date',)
    date_hierarchy = 'wedding_date'
    readonly_fields = ('created_at', 'main_photo_preview', 'bride_photo_preview', 'groom_photo_preview')
    save_on_top = True
    inlines = [InvitationEventInline, GalleryPhotoInline, RsvpInline]

    fieldsets = (
        ("عروس و داماد", {
            'fields': (
                ('bride_name', 'groom_name'),
                ('bride_photo', 'bride_photo_preview'),
                ('groom_photo', 'groom_photo_preview'),
                ('bride_parents', 'groom_parents'),
            )
        }),
        ("زمان و مکان مراسم", {
            'fields': ('wedding_date', 'venue_name', 'venue_address', 'venue_map_embed')
        }),
        ("محتوای دعوتنامه", {
            'fields': ('story_text', 'gift_message', 'photo_main', 'main_photo_preview')
        }),
        ("رسانه", {
            'fields': ('intro_video', 'background_music'),
            'classes': ('collapse',),
        }),
        # بخش جدید برای تنظیمات RSVP
        ("تنظیمات RSVP", {
            'fields': ('rsvp_url',),
            'classes': ('collapse',),
            'description': 'آدرسی که فرم اعلام حضور به آن ارسال می‌شود. اگر خالی باشد، فرم به همان صفحه فعلی ارسال می‌شود.',
        }),
        ("اطلاعات سیستمی", {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    # ---------- ستون‌های نمایشی سفارشی ----------
    @admin.display(description="زوج")
    def couple_display(self, obj):
        return f"{obj.groom_name} 💍 {obj.bride_name}"

    @admin.display(description="عکس اصلی")
    def main_photo_thumb(self, obj):
        if obj.photo_main:
            return format_html(
                '<img src="{}" style="height:44px;width:44px;border-radius:50%;object-fit:cover;" />',
                obj.photo_main.url,
            )
        return "—"

    @admin.display(description="پیش‌نمایش عکس اصلی")
    def main_photo_preview(self, obj):
        if obj.photo_main:
            return format_html(
                '<img src="{}" style="max-height:220px;border-radius:12px;" />', obj.photo_main.url
            )
        return "عکسی انتخاب نشده"

    @admin.display(description="پیش‌نمایش عکس عروس")
    def bride_photo_preview(self, obj):
        if obj.bride_photo:
            return format_html(
                '<img src="{}" style="height:120px;border-radius:12px;" />', obj.bride_photo.url
            )
        return "—"

    @admin.display(description="پیش‌نمایش عکس داماد")
    def groom_photo_preview(self, obj):
        if obj.groom_photo:
            return format_html(
                '<img src="{}" style="height:120px;border-radius:12px;" />', obj.groom_photo.url
            )
        return "—"

    @admin.display(description="تعداد مراسم")
    def events_count(self, obj):
        return obj.events.count()

    @admin.display(description="تعداد عکس گالری")
    def gallery_count(self, obj):
        return obj.gallery.count()

    @admin.display(description="حضور / عدم حضور")
    def rsvp_summary(self, obj):
        yes = obj.rsvps.filter(attending=True).count()
        no = obj.rsvps.filter(attending=False).count()
        return format_html(
            '<span style="color:#1a7f37;font-weight:600;">✔ {}</span>'
            '&nbsp;&nbsp;'
            '<span style="color:#c0392b;font-weight:600;">✘ {}</span>',
            yes, no,
        )

    @admin.display(description="لینک RSVP", boolean=True)
    def has_rsvp_url(self, obj):
        return bool(obj.rsvp_url)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            _events_count=Count('events', distinct=True),
            _gallery_count=Count('gallery', distinct=True),
        )


# ============================================================
# RSVP ADMIN
# ============================================================
@admin.register(Rsvp)
class RsvpAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'invitation', 'attending', 'guests_count',
        'phone', 'email', 'created_at',
    )
    list_filter = ('attending', 'invitation', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_select_related = ('invitation',)
    actions = ['mark_as_attending', 'mark_as_not_attending']

    @admin.display(description="حضور", ordering='attending')

    @admin.action(description="علامت‌گذاری به‌عنوان «حاضر می‌شوند»")
    def mark_as_attending(self, request, queryset):
        updated = queryset.update(attending=True)
        self.message_user(request, f"{updated} پاسخ به‌روزرسانی شد.")

    @admin.action(description="علامت‌گذاری به‌عنوان «حاضر نمی‌شوند»")
    def mark_as_not_attending(self, request, queryset):
        updated = queryset.update(attending=False)
        self.message_user(request, f"{updated} پاسخ به‌روزرسانی شد.")


# ============================================================
# مدیریت مستقل
# ============================================================
@admin.register(InvitationEvent)
class InvitationEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'invitation', 'date_time', 'venue', 'order')
    list_filter = ('invitation',)
    search_fields = ('title', 'venue')
    ordering = ('invitation', 'order', 'date_time')


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('invitation', 'thumbnail', 'caption', 'order')
    list_filter = ('invitation',)
    ordering = ('invitation', 'order', 'id')

    @admin.display(description="پیش‌نمایش")
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;border-radius:8px;object-fit:cover;" />',
                obj.image.url,
            )
        return "—"


# ============================================================
# سربرگ پنل ادمین
# ============================================================
admin.site.site_header = "مدیریت دعوتنامه‌های عروسی"
admin.site.site_title = "پنل دعوتنامه"
admin.site.index_title = "خوش آمدید"