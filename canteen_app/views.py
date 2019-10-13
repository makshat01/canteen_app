from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from canteen.settings import MEDIA_URL

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'canteen_app/signup.html', {'form': form})


def category(request):
    food_types = FoodType.objects.all()
    return render(request, 'canteen_app/menumain.html', {'food_types':food_types, 'media_url':MEDIA_URL})


def menu_list(request, food_type_id):
    menu_food = Menu.objects.filter(food_type_id=food_type_id)
    return render(request, 'canteen_app/menu_list.html', {'menu_food':menu_food})


def cart(request, menu_id):
    orders = Order.objects.filter(user=request.user, is_fulfilled=False)
    menu = Menu.objects.filter(id=menu_id)
    if len(orders)==0:
        order = Order(user=request.user, is_fulfilled=False, total_price=menu[0].price)
        order.save()
        order_item = OrderItem(order=order, food_item=menu[0], quantity=1)
        order_item.save()
    else:
        orders[0].total_price += menu[0].price
        orders[0].save()
        order_item = OrderItem(order=orders[0], food_item=menu[0], quantity=1)
        order_item.save()
    menu_food = Menu.objects.filter(food_type_id=menu[0].food_type_id)
    return render(request, 'canteen_app/menu_list.html', {'menu_food':menu_food})


def bill(request):
    orders = Order.objects.filter(user=request.user, is_fulfilled=False)
    bill_items = OrderItem.objects.filter(order=orders[0])
    return render(request, 'canteen_app/bill.html', {'bill_items':bill_items, 'order':orders[0]})


def orders_list(request):
    orders = Order.objects.filter(is_fulfilled=False)
    li = []
    for order in orders:
        dire = {}
        li2 = []
        order_items = OrderItem.objects.filter(order=order)
        for order_item in order_items:
            li2.append(order_item.food_item.food_name)
        food_types = li2
        dire['id'] = order.id
        dire['user'] = order.user.username
        dire['food_items'] = food_types
        dire['total_price'] = order.total_price
        li.append(dire)
    return render(request, 'canteen_app/orders_list.html', {'orders': li})

def full_fill(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_fulfilled = True
    order.save()
    #return redirect(to=orders_list)
    orders = Order.objects.filter(is_fulfilled=False)
    li = []
    for order in orders:
        dire = {}
        li2 = []
        order_items = OrderItem.objects.filter(order=order)
        for order_item in order_items:
            li2.append(order_item.food_item.food_name)
        food_types = li2
        dire['id'] = order.id
        dire['user'] = order.user.username
        dire['food_items'] = food_types
        dire['total_price'] = order.total_price
        li.append(dire)
    return render(request, 'canteen_app/orders_list.html', {'orders': li})



def home(request):
    return render(request, 'canteen_app/home.html')


def about(request):
    return render(request, 'canteen_app/about.html')


def gallery(request):
    return render(request, 'canteen_app/gallery.html')


def form(request):
    return render(request, 'canteen_app/forms.html')


def food(request):
    name = request.POST['foodname']
    file = request.FILES['file']
    foodname = FoodType(food_type=name, image=file)
    foodname.save()

    return render(request, 'canteen_app/forms.html')
    # return redirect(to, form) 