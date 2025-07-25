from django.shortcuts import render, get_object_or_404, redirect
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_staff_user(user):
    return user.is_staff or user.is_superuser

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': announcements})

@login_required
@user_passes_test(is_staff_user)
def announcement_create(request):
    form = AnnouncementForm(request.POST or None)
    if form.is_valid():
        ann = form.save(commit=False)
        ann.created_by = request.user
        ann.save()
        return redirect('announcement_list')
    return render(request, 'announcements/form.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def announcement_edit(request, pk):
    ann = get_object_or_404(Announcement, pk=pk)
    form = AnnouncementForm(request.POST or None, instance=ann)
    if form.is_valid():
        form.save()
        return redirect('announcement_list')
    return render(request, 'announcements/form.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def announcement_delete(request, pk):
    ann = get_object_or_404(Announcement, pk=pk)
    ann.delete()
    return redirect('announcement_list')