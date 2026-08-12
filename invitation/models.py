from django.db import models


class Invitation(models.Model):
    # ---------- عروس و داماد ----------
    bride_name = models.CharField(max_length=100, verbose_name="اسم عروس")
    groom_name = models.CharField(max_length=100, verbose_name="اسم داماد")

    bride_photo = models.ImageField(
        upload_to='invitation/couple/', verbose_name="عکس عروس", blank=True
    )
    groom_photo = models.ImageField(
        upload_to='invitation/couple/', verbose_name="عکس داماد", blank=True
    )

    bride_parents = models.CharField(
        max_length=150, verbose_name="نام پدر و مادر عروس", blank=True,
        help_text="مثلاً: آقای احمدی و خانم محمدی"
    )
    groom_parents = models.CharField(
        max_length=150, verbose_name="نام پدر و مادر داماد", blank=True
    )

    # ---------- زمان و مکان ----------
    wedding_date = models.DateTimeField(verbose_name="تاریخ و ساعت عروسی")
    venue_name = models.CharField(max_length=255, verbose_name="محل برگزاری")
    venue_address = models.TextField(verbose_name="آدرس")
    venue_map_embed = models.TextField(
        verbose_name="کد نقشه گوگل (iframe)", blank=True,
        help_text="لینک iframe گوگل مپ را اینجا بچسبانید"
    )

    # ---------- محتوای متنی و رسانه ----------
    story_text = models.TextField(verbose_name="داستان عشق", blank=True)
    gift_message = models.TextField(
        verbose_name="پیام هدیه / کارت خراش‌دار", blank=True,
        help_text="پیامی که زیر کارت خراش‌دار نمایش داده می‌شود"
    )
    photo_main = models.ImageField(
        upload_to='invitation/', verbose_name="عکس اصلی (هدر)", blank=True
    )

    intro_video = models.FileField(
        upload_to='invitation/videos/', verbose_name="ویدئوی اینترو", blank=True, null=True,
        help_text="فرمت mp4 پیشنهاد می‌شود"
    )
    background_music = models.FileField(
        upload_to='invitation/music/', verbose_name="موزیک پس‌زمینه", blank=True, null=True,
        help_text="فرمت mp3 پیشنهاد می‌شود"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    rsvp_url = models.TextField(max_length=500, blank=True, null=True, verbose_name="آدرس RSVP")


    def __str__(self):
        return f"{self.bride_name} & {self.groom_name}"

    class Meta:
        verbose_name = "دعوتنامه"
        verbose_name_plural = "دعوتنامه‌ها"


class InvitationEvent(models.Model):
    """
    برنامه‌ی مراسم (عقد، حنابندان، عروسی و ...) — در تمپلیت با
    invitation.events.all رندر می‌شود.
    """
    invitation = models.ForeignKey(
        Invitation, on_delete=models.CASCADE, related_name='events',
        verbose_name="دعوتنامه"
    )
    title = models.CharField(max_length=100, verbose_name="عنوان مراسم", help_text="مثلاً: مراسم عقد")
    date_time = models.DateTimeField(verbose_name="تاریخ و ساعت")
    venue = models.CharField(max_length=255, verbose_name="محل برگزاری", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        verbose_name = "برنامه مراسم"
        verbose_name_plural = "برنامه‌های مراسم"
        ordering = ['order', 'date_time']

    def __str__(self):
        return f"{self.title} - {self.invitation}"

    @property
    def date(self):
        """سازگاری با تمپلیت: event.date|to_shamsi"""
        return self.date_time

    @property
    def time(self):
        """سازگاری با تمپلیت: نمایش ساعت مراسم"""
        return self.date_time.strftime('%H:%M')


class GalleryPhoto(models.Model):
    """
    عکس‌های گالری خاطرات — در تمپلیت با invitation.gallery.all رندر می‌شود.
    """
    invitation = models.ForeignKey(
        Invitation, on_delete=models.CASCADE, related_name='gallery',
        verbose_name="دعوتنامه"
    )
    image = models.ImageField(upload_to='invitation/gallery/', verbose_name="عکس")
    caption = models.CharField(max_length=150, verbose_name="توضیح کوتاه", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")

    class Meta:
        verbose_name = "عکس گالری"
        verbose_name_plural = "گالری تصاویر"
        ordering = ['order', 'id']

    def __str__(self):
        return f"عکس گالری - {self.invitation}"


class Rsvp(models.Model):
    invitation = models.ForeignKey(
        Invitation, on_delete=models.CASCADE, related_name='rsvps',
        verbose_name="دعوتنامه"
    )
    name = models.CharField(max_length=100, verbose_name="نام شما")
    email = models.EmailField(verbose_name="ایمیل", blank=True)
    phone = models.CharField(max_length=20, verbose_name="شماره تماس", blank=True)
    attending = models.BooleanField(verbose_name="شرکت می‌کنم", default=True)
    guests_count = models.PositiveIntegerField(
        verbose_name="تعداد همراهان", default=0
    )
    message = models.TextField(verbose_name="پیام تبریک", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پاسخ حضور"
        verbose_name_plural = "پاسخ‌های حضور"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {'می‌آید' if self.attending else 'نمی‌آید'}"