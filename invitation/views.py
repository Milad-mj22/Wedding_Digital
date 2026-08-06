from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Invitation, Rsvp

def invitation_view(request):
    # فقط اولین دعوتنامه رو نشون بده (برای سادگی)
    invitation = Invitation.objects.first()
    if not invitation:
        return render(request, 'invitation/home.html', {'error': 'هنوز دعوتنامه‌ای ساخته نشده!'})
    
    if request.method == 'POST':
        # دریافت اطلاعات از فرم RSVP
        name = request.POST.get('name')
        email = request.POST.get('email')
        attending = request.POST.get('attending') == 'on'
        message = request.POST.get('message', '')
        
        if name and email:
            Rsvp.objects.create(
                invitation=invitation,
                name=name,
                email=email,
                attending=attending,
                message=message
            )
            messages.success(request, 'پاسخ شما با موفقیت ثبت شد. منتظرتون هستیم!')
        else:
            messages.error(request, 'لطفاً نام و ایمیل خود را وارد کنید.')
        return redirect('invitation')
    
    return render(request, 'invitation/home.html', {'invitation': invitation})