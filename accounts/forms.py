from django.contrib.auth import get_user_model
from unfold.forms import UserCreationForm, UserChangeForm  # bcs we use unfold for frontend
from accounts.models import AppUser

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email']


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel