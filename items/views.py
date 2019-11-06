from django.shortcuts import render
from items.models import Item

# Create your views here.
def main(request):
    queryset = Item.objects.all()
    query_list = []
    for i in queryset:
        if i.quantity != 0:
            query_list.append(i)
    types = []
    t_count = 0
    for i in query_list:
        if i.i_type not in types:
            t_count+=1
            types.append(i.i_type)
    temp = types.pop()
    context={
        "object_list"   : query_list,
        "types"         : types,
        "t_count"       : t_count,
        "temp"          : temp,
    }

    return render(request,'index.html',context)