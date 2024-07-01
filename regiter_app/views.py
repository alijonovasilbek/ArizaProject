from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import requests
from .forms import UserInformationForm
from django.conf import settings

def user_information_view(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            user_info = form.save()

            # Send data to Telegram bot
            telegram_token = '7371539456:AAGPSXxlO1WPrGsEgRpLPNn1GAy0HAH82Zo'
            telegram_chat_id = '5737465114'
            telegram_message = f'''
        A new user information entry has been submitted.

        Your Details:
        Name: {user_info.first_name} 
        Last_name: {user_info.last_name} 
        Class: {user_info.class_user}   
        Region: {user_info.region}
        Phone: {user_info.phone_your}
        '''
            requests.get(f'https://api.telegram.org/bot{telegram_token}/sendMessage', params={
                'chat_id': telegram_chat_id,
                'text': telegram_message
            })

            # Send data via email
            send_mail(
                'New User Information',
                telegram_message,
                settings.DEFAULT_FROM_EMAIL,
                ['alijonovasilbek058@gmail.com'],
                fail_silently=False,
            )

            return redirect('success')  # Redirect to a success page
    else:
        form = UserInformationForm()
    return render(request, 'user_information_form.html', {'form': form})
