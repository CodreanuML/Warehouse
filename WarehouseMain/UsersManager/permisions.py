from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import TemplateView






"""
group access mixing -> cand vrei sa eviti  adaugarea de mai multe mixuri in view , 
pasezi acest GroupAccessMixin si setez allowed_groups ca lista de utilizatori care pot 
accesa viewul

""" 
class GroupAccessMixin(UserPassesTestMixin):
    allowed_groups = None  # listă sau string
    redirect_url = "UsersManager:login"

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False

        if self.allowed_groups is None:
            return False

        # dacă e string, îl transformăm în listă
        if isinstance(self.allowed_groups, str):
            groups = [self.allowed_groups]
        else:
            groups = self.allowed_groups

        return self.request.user.groups.filter(name__in=groups).exists()

    def handle_no_permission(self):
        return redirect(self.redirect_url)




#individual mixing logistics
class Logistic_lvl1_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "logistic_user_lvl1"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login")  


class Logistic_lvl2_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "logistic_user_lvl2"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login")  


class Logistic_manager_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "logistic_manager"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login") 

class Logistic_all_AllowedGroupMixin(UserPassesTestMixin):        
    allowed_groups = ["logistic_user_lvl1","logistic_user_lvl2","logistic_manager"]  

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.allowed_groups).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login")




#individual mixing warehouse
class Warehouse_lvl1_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "warehouse_user_lvl1"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login")  


class Warehouse_lvl2_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "warehouse_user_lvl2"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login")  


class Warehouse_manager_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "warehouse_manager"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login") 


class Warehouse_all_AllowedGroupMixin(UserPassesTestMixin):        
    allowed_groups = ["warehouse_user_lvl1","warehouse_user_lvl2","warehouse_manager"]  

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.allowed_groups).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login")



#general manager mixing 
class General_manager_AllowedGroupMixin(UserPassesTestMixin):
    restricted_group = "general_manager"

    def test_func(self):
        return self.request.user.groups.filter(name=self.restricted_group).exists()

    def handle_no_permission(self):
        return redirect("UsersManager:login") 


 
