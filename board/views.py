from django.shortcuts import render, redirect

from django.utils import timezone

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Note

from .forms import NoteForm

def board_index(request):
    if request.method == "POST":
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.user = request.user
            note.save()
    notes = Note.objects.all()
    return render(request, 'board/board-index.html', {'notes': notes})

from django.http import HttpResponseForbidden

@login_required(login_url='common:login')
def board_delete(request, id):
    target_data = Note.objects.get(id=id)
    if target_data.user == request.user or request.user.is_staff:
        target_data.delete()
        return redirect('board:index')
    return HttpResponseForbidden()

