from django.db import models

# Create your models here.
from django.db import models

class Invitation(models.Model):
    bride_name = models.CharField(max_length=100, verbose_name="اسم عروس")
    groom_name = models.CharField(max_length=100, verbose_name="اسم داماد")
    wedding_date = models.DateTimeField(verbose_name="تاریخ و ساعت عروسی")
    venue = models.CharField(max_length=255, verbose_name="محل برگزاری")
    address = models.TextField(verbose_name="آدرس")
    love_story = models.TextField(verbose_name="داستان عشق", blank=True)
    photo_main = models.ImageField(upload_to='invitation/', verbose_name="عکس اصلی", blank=True)
    map_embed = models.TextField(verbose_name="کد نقشه گوگل (iframe)", blank=True,
                                 help_text="لینک iframe گوگل مپ را اینجا بچسبانید")

    video_url = models.FileField(upload_to='videos/', verbose_name="ویدئوی اینترو", blank=True, null=True,
                              help_text="فرمت mp4 پیشنهاد می‌شود")

    def __str__(self):
        return f"{self.bride_name} & {self.groom_name}"

    class Meta:
        verbose_name = "دعوتنامه"
        verbose_name_plural = "دعوتنامه‌ها"


class Rsvp(models.Model):
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, related_name='rsvps')
    name = models.CharField(max_length=100, verbose_name="نام شما")
    email = models.EmailField(verbose_name="ایمیل")
    attending = models.BooleanField(verbose_name="شرکت می‌کنم", default=True)
    message = models.TextField(verbose_name="پیام تبریک", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {'می‌آید' if self.attending else 'نمی‌آید'}"