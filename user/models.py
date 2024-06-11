from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings
from django.forms import model_to_dict
from crum import get_current_request
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='system/images/users/', null=True, blank=True, verbose_name='Imagen')
    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL, self.image)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
                item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item
    
    def get_current_group(self, request):
        group_id = request.session.get('group_id')
        if group_id:
            try:
                return Group.objects.get(pk=group_id)
            except Group.DoesNotExist:
                pass
        return None
    
    # def get_group_session(self):
    #     try:
    #         request = get_current_request()
    #         groups = self.groups.all()
    #         print(f"Groups for user {self.username}: {groups}")
    #         if groups.exists():
    #             if 'group' not in request.session:
    #                 request.session['group'] = groups[0].id
    #     except:
    #         pass
    def get_group_session(self):
        try:
            request = get_current_request()
            if request is None:
                raise Exception("No current request found")

            groups = self.groups.all()
            print(f"Groups for user {self.username}: {groups}")

            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0].id # Guardar el ID del grupo
                    print(f"Group set in session: {request.session['group']}")
                    return groups[0]
                else:
                    print(f"Group already in session: {request.session['group']}")
                    group_id = request.session['group']
                    group = groups.get(id=group_id)
                    return group
            else:
                print(f"No groups found for user {self.username}")
                return None
        except Exception as e:
            print(f"Error in get_group_session: {e}")
            return None
    
    # print(f" Funcion : {get_current_request()}")
    # def get_group_session(self):
    #     try:
    #         request = get_current_request()
    #         if request:
    #             groups = self.groups.all()
    #             if groups.exists():
    #                 if 'group_id' not in request.session:
    #                     group = groups[0]
    #                     request.session['group_id'] = group.pk
    #                     request.session.save()
    #                     return group  # Retornar el objeto Group
    #     except:
    #         pass
    #     return None 
    # def get_group_session(self):
    #     try:
    #         request = get_current_request()
    #         if request:
    #             groups = self.groups.all()
    #             if groups.exists():
    #                 if 'group_id' not in request.session:
    #                     request.session['group_id'] = groups[0].pk
    #                     request.session.save()
    #     except:
    #         pass
    # def get_group_session(self):
    #     try:
    #         request = get_current_request()
    #         group_id = request.session.get('group_id')
    #         if group_id:
    #             group = Group.objects.get(pk=group_id)
    #             return group
    #         else:
    #             groups = self.groups.all()
    #             if groups.exists():
    #                 request.session['group_id'] = groups[0].pk
    #                 return groups[0]
    #     except Group.DoesNotExist:
    #         # Manejar el caso en que el grupo no exista
    #         pass
    #     except Exception as e:
    #         # Manejar otros errores si es necesario
    #         pass
    #     return None
    
    # def get_group_session(self):
    #     try:
    #         request = get_current_request()
    #         groups = self.groups.all()
    #         if groups.exists():
    #             if 'group_id' in request.session:
    #                 group_id = request.session['group_id']
    #                 group = Group.objects.get(id=group_id)
    #                 return group
    #             else:
    #                 request.session['group_id'] = groups[0].id
    #                 return groups[0]
    #     except Exception as e:
    #         print(e)  # Para depuración, quita esto en producción
    #         return None
    
    # def get_group_session(self):
    #     try:
    #         request = get_current_request()
    #         groups = self.groups.all()
    #         print(f"Groups for user {self.username}: {groups}") 
    #         if groups.exists():
    #             if 'group' not in request.session:
    #                 request.session['group'] = groups[0].id
    #     except:
    #         pass
    # def save (self, *args, **kwargs):
    #     if self.pk is None:
    #         self.set_password(self.password)
    #     else:
    #         user = User.objects.get(pk=self.pk)
    #         if user.password != self.password:
    #             self.set_password(self.password)
    #     super().save(*args, **kwargs)