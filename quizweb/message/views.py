from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import SendMessageForm
from team.models import Team

@login_required
def send_message(request):
    if not request.user.is_staff:
        return redirect('messages')  # csak tanároknak elérhető

    if request.method == 'POST':
        form = SendMessageForm(request.POST, teacher=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('messages')
    else:
        form = SendMessageForm(teacher=request.user)

    # Lekérdezzük az eddigi küldött üzeneteket
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    if not sent_messages.exists():
        sent_messages = None  # Felhasználható az oldal "nem küldött üzenetet" üzenethez

    return render(request, 'sendmessage.html', {'form': form, 'sent_messages': sent_messages})


@login_required
def messages_list(request):
    if request.user.is_staff:
        # Tanárnak a küldött üzenetei
        messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
        empty_message = "Nem küldött még üzenetet."
    else:
        # Diáknak a kapott üzenetei
        messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
        empty_message = "Még nem kapott üzenetet."

    if not messages.exists():
        messages = None

    return render(request, 'messages.html', {'messages': messages, 'empty_message': empty_message})
