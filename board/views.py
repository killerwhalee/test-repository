from django.shortcuts import render, redirect

from django.utils import timezone

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Note

from .forms import NoteForm

from django.utils import timezone

def board_index(request):
    if request.method == "POST":
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.user = request.user
            note.date_created = timezone.now()
            note.save()
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'board/board-index.html', context)

@login_required(login_url='common:login')
def board_delete(request, id):
    target_data = get_object_or_404(Note, id=id)
    if target_data.user == request.user or request.user.is_staff:
        target_data.delete()
        return redirect('board:index')
    return HttpResponseForbidden()

