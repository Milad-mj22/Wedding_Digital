from django.http import JsonResponse
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



def rsvp_submit(request, invitation_id):
    """
    ویوی دریافت و ذخیره فرم اعلام حضور (Ajax)
    """
    invitation = get_object_or_404(Invitation, id=invitation_id)
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        attending = request.POST.get('attending') == 'yes'
        note = request.POST.get('note', '').strip()
        
        # اعتبارسنجی
        if not full_name:
            return JsonResponse({
                'success': False,
                'message': 'لطفاً نام خود را وارد کنید.'
            }, status=400)
        
        # ذخیره در دیتابیس
        rsvp = Rsvp.objects.create(
            invitation=invitation,
            name=full_name,
            attending=attending,
            message=note,
        )

        if attending:
            msg = 'با تشکر، منتظر دیدار شما هستیم.'
        else:
            msg = 'با تشکر، عدم حضور شما ثبت شد'

        
        # پاسخ موفقیت
        return JsonResponse({
            'success': True,
            'message': msg,
            'data': {
                'name': rsvp.name,
                'attending': rsvp.attending,
            }
        })
    
    return JsonResponse({
        'success': False,
        'message': 'روش غیرمجاز'
    }, status=405)