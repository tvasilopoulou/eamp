from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from  apps.models import *
# from django.contrib.auth.models import User

USER_CHOICES= (
    ('', 'Ιδιότητα'),
    ('student', 'Φοιτητής'),
    ('secretary', 'Γραμματεία'),
    ('publisher', 'Εκδότης'),
    ('eprovider', 'Διαθέτης e-Σημειώσεων'),
    ('delivery', 'Σημείο Διανομής - Βιβλιοθήκη'),
)

class EproviderForm(forms.ModelForm):

    class Meta:
        model = Eprovider
        fields = [ 'identity_number', 'house', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['identity_number'].label = None
        self.fields['identity_number'].widget = forms.TextInput(attrs={'placeholder':'Αριθμός Ταυτότητας'})
        self.fields['house'].label = None
        self.fields['house'].empty_label =  'Εκδοτικός Οίκος'

class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = [ 'trn', 'ssn', 'house', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trn'].label = None
        self.fields['trn'].widget = forms.TextInput(attrs={'placeholder':'ΑΦΜ'})
        self.fields['ssn'].label = None
        self.fields['ssn'].widget = forms.TextInput(attrs={'placeholder':'ΑΜΚΑ'})
        self.fields['house'].label = None
        self.fields['house'].empty_label =  'Εκδοτικός Οίκος'

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = [ 'd_name', 'address', 'postal_code', 'phone_number',  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['d_name'].label = None
        self.fields['d_name'].widget = forms.TextInput(attrs={'placeholder':'Ονομασία Σημείου Διανομής'})
        self.fields['address'].label = None
        self.fields['address'].widget = forms.TextInput(attrs={'placeholder':'Διεύθυνση'})
        self.fields['postal_code'].label = None
        self.fields['postal_code'].widget = forms.TextInput(attrs={'placeholder':'Ταχυδρομικός Κώδικας'})
        self.fields['postal_code'].max_length = 5
        self.fields['phone_number'].label = None
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder':'Τηλέφωνο'})
        self.fields['phone_number'].max_length = 10

class SecretaryForm(forms.ModelForm):

    class Meta:
        model = Secreteriat
        fields = [ 'uni', 'department', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uni'].label = None
        self.fields['uni'].empty_label = 'Εκπαιδευτικό Ίδρυμα'
        self.fields['department'].label = None
        self.fields['department'].empty_label =  'Τμήμα Σπουδών'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'uni', 'department', 'phone_number', 'stud_id', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = None
        self.fields['phone_number'].max_length = 10
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder':'Τηλέφωνο'})
        self.fields['stud_id'].label = None
        self.fields['stud_id'].widget = forms.TextInput(attrs={'placeholder':'Αριθμός Μητρώου'})
        self.fields['uni'].label = None
        self.fields['uni'].empty_label = 'Εκπαιδευτικό Ίδρυμα'
        self.fields['department'].label = None
        self.fields['department'].empty_label =  'Τμήμα Σπουδών'
class SignUpForm(UserCreationForm):

    email = forms.EmailField(label = '', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    user_type = forms.ChoiceField(label = '', choices = USER_CHOICES)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type', ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = None
        self.fields['username'].help_text = None
        self.fields['password1'].label = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password2'].label = None
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Όνομα Χρήστη'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder':'Όνομα'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder':'Επώνυμο'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Κωδικός Πρόσβασης'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Επαλήθευση Κωδικού'})
