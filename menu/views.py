from django.shortcuts import render, redirect
from .models import MenuOrder, MenuSection
from django.shortcuts import get_object_or_404

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    orders = MenuOrder.objects.order_by("-id")
    return render(
        request,
        "home.html",
        {
            "orders": orders
        }
    )



@login_required
def new_order(request):
    if request.method == "POST":
        order = MenuOrder.objects.create(
            event_name=request.POST["event_name"],
            event_date=request.POST["event_date"],
            rate=request.POST["rate"]
        )
        categories = request.POST.getlist("category[]")
        items = request.POST.getlist("items[]")
        for category, item in zip(categories, items):
            if category.strip():
                MenuSection.objects.create(
                    menu_order=order,
                    category=category,
                    items=item
                )
        return redirect("home")
    return render(request, "new_order.html")



@login_required
def edit_order(request, order_id):
    order = get_object_or_404(MenuOrder, id=order_id)
    if request.method == "POST":
        order.event_name = request.POST["event_name"]
        order.event_date = request.POST["event_date"]
        order.rate = request.POST["rate"]
        order.save()
        MenuSection.objects.filter(menu_order=order).delete()
        categories = request.POST.getlist("category[]")
        items = request.POST.getlist("items[]")
        for category, item in zip(categories, items):
            if category.strip():
                MenuSection.objects.create(
                    menu_order=order,
                    category=category,
                    items=item
                )
        return redirect("home")
    sections = MenuSection.objects.filter(menu_order=order)
    return render(
        request,
        "edit_order.html",
        {
            "order": order,
            "sections": sections,
        }
    )


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(MenuOrder, id=order_id)
    order.delete()
    return redirect("home")


@login_required
def print_order(request, order_id):
    order = get_object_or_404(MenuOrder, id=order_id)
    return render(request, "print_order.html", {
        "order": order
    })