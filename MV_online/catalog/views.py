from django.shortcuts import render, get_object_or_404
from .models import User


def index(request):
    users_list = User.objects.all()
    context = {
        'users_list': users_list,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_user(request):
    if request.method == 'POST':
        new_user = User(
            username=request.POST['name'],
            usermail=request.POST['email'],
        )

        new_user.save()

        return render(
            template_name='new_user_added.html',
            request=request,
            context={
                'username': new_user.username,
                'email': new_user.usermail
            }
        )
    return render(
        template_name='new_user_template.html',
        request=request
    )


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return render(
        request,
        'deleted_user.html',
        context={'user': user,
                 'user_id': user_id}
    )


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'GET':
        return render(
            request,
            'edit_user.html',
            context={'user': user}
        )
    else:
        user.username = request.POST['name']
        user.usermail = request.POST['email']
        user.save()
        return render(
            request,
            template_name='user_edited.html',
            context={'user': user}
        )


def get_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    return render(
        request,
        'get_user.html',
        context={'user': user,
                 'user_id': user_id}
    )
