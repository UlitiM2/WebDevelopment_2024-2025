from django.shortcuts import render, redirect

from site_web.models import MenuItem
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from site_web.forms import ContactForm


def index(request):
    menu_osn = MenuItem.objects.filter(type__exact='Main')
    menu_dop = MenuItem.objects.filter(type__exact='Dop')
    context = {'menu_osn': menu_osn, 'menu_dop': menu_dop}
    return render(
        request,
        'index.html',
        context=context
    )


def about(request):
    return render(
        request,
        'about.html'
    )


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contacts.html',
        context=context
    )


def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
