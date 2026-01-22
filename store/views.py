from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict

from json import loads

from store.models import Product

@method_decorator(csrf_exempt,name="dispatch")
class ProductCreateListView(View):

    def post(self,request,*args,**kwargs):

        data = loads(request.body)

        qs=Product.objects.create(**data)

        data["id"]=qs.id


        return JsonResponse({"data":data,"status":"201 created"})
    
    def get(self,request,*args,**kwargs):

        qs = Product.objects.all()
        #url=http://127.0.0.1:8000/product?category=kids
        print(request.GET)#{'category': ['kids']}

        if "category" in request.GET:

            serach_value = request.GET.get("category")

            qs = qs.filter(category=serach_value)

        if "price_lt" in request.GET:

            search_amount = int(request.GET.get("price_lt")) 

            qs = qs.filter(price__lt=search_amount)       

        result = list(qs.values())
       
   
        return JsonResponse({"data":result,"message":"200 ok"})
    
@method_decorator(csrf_exempt,name="dispatch")
class ProductRetrieveUpdateDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        product_object = Product.objects.get(id=id)

        result=model_to_dict(product_object)

        return JsonResponse({"data":result,"status":"200ok"})
    
    def put(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        data = loads(request.body)

        Product.objects.filter(id=id).update(**data) 

        qs=Product.objects.filter(id=id)

        result = list(qs.values())
        

        return JsonResponse({"data":result})