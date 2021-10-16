from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Texts
from .forms import TextForm
import uuid
from cryptography.fernet import Fernet

def rewrite(rewrite_encoded_sting): # Rewrite function.
    data = rewrite_encoded_sting.replace("b'", "")
    data2 = data.replace("'", "")
    return data2


# Create your views he re.
def home(request):
    if request.method == 'POST':
        form = TextForm(request.POST or None)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.view_id = uuid.uuid4().hex[:6].upper() # Rewrite VIEW ID.

            # Encrypt the data
            key = Fernet.generate_key()
            f = Fernet(key)
            token = f.encrypt(str.encode(instance.text))
            instance.text = token
            instance.save()
            # END: Encrypt the data

            messages.success(request, ("Text has been encrypted! Your link is ready."))
            link = "http://localhost:8000/view/" + str(instance.view_id)
            return render(request, 'home.html', {'link': link, 'decryptKey': key.decode("utf-8")})
    else:
        return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


def view(request, text_id):
    try:
        item = Texts.objects.get(view_id=text_id)
        if request.method == 'POST':

            try: # Password try
                # Initialize Fernet object
                key = request.POST.get('decryptionKey')
                f = Fernet(str.encode(key))
                # END: Initialize Fernet object

                content = item.text # Raw output before decrypt. :)

                # Rewrite the string & Encode & Decrypt
                rewrite_string = rewrite(content) # First, we need to rewrite the string as it cannot be decoded, it contains b'' but is string not byte type
                clear_data = f.decrypt(str.encode(rewrite_string))
                show_data = clear_data.decode("utf-8")
                # END: Rewrite the string & Encode & Decrypt

                item.delete()
                return render(request, 'view.html', {'item': show_data})
            except Exception as e2:
                item.delete()
                return render(request, 'view.html', {'invalid': 2, 'id': text_id})

        return render(request, 'view.html', {'confirm': 1, 'id': text_id})

    except Exception as e:

        return render(request, 'view.html', {'invalid': 1, 'id': text_id, "error": e})


