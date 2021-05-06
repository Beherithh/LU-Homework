from django.shortcuts import render
from .models import Deposit


def index(request):
    deps_list = Deposit.objects.all()
    context = {
        'deps_list': deps_list,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_dep(request):
    if request.method == 'POST':
        new_dep = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
        )
        new_dep.save()

        deps_list = Deposit.objects.all()
        context = {
            'deps_list': deps_list,
        }

        return render(
            template_name='index.html',
            request=request,
            context=context,
        )

    return render(
        template_name='new_dep_template.html',
        request=request
    )


def get_dep(request, dep_id):
    dep = get_object_or_404(Deposit, pk=dep_id)

    return render(
        request,
        'get_dep.html',
        context={'dep': dep,
                 'dep_id': dep_id}
    )
