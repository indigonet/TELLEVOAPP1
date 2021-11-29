from json.decoder import JSONDecodeError
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

# Create your views here.


class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if (id>0):
            users=list(Usuario.objects.filter(id=id).values())
            if len(users)>0:
                user=users[0]
                datos={'message':"Encontrado",'user':user}
            else:
                datos={'message':"No encontradoo..."}     
            return JsonResponse(datos)    
            
        else:
            users= list(Usuario.objects.values())
            if len(users)>0:
                datos={'message':"Completado",'users':users}
            else:
                datos={'message':"No encontradoo..."}
            return JsonResponse(datos)    

    def post(self, request):
        jd = json.loads(request.body)
        Usuario.objects.create(Nombre=jd['Nombre'], Correo=jd['Correo'], contraseña=jd['contraseña'])
        datos = {'message': "Success"}
        return JsonResponse(datos)


    def put(self, request,id):
        jd = json.loads(request.body)
        users = list(Usuario.objects.filter(id=id).values())
        if len(users) > 0:
            users = Usuario.objects.get(id=id)
            users.Nombre = jd['Nombre']
            users.Correo = jd['Correo']
            users.contraseña = jd['contraseña']
            users.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def delete(self, request,id):
        users = list(Usuario.objects.filter(id=id).values())
        if len(users) > 0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)
        
    

    
    
        