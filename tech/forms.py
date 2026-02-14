from django import forms
from .models import TechServiceRequest, TechCourseEnrollment


class TechServiceRequestForm(forms.ModelForm):
    class Meta:
        model = TechServiceRequest
        fields = ['full_name', 'email', 'phone', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg '
                         'focus:border-blue-500 focus:ring-2 focus:ring-blue-200 '
                         'focus:outline-none transition duration-200 '
                         'placeholder-gray-400 text-gray-900',
                'placeholder': 'Enter your full name',
                'required': 'required',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg '
                         'focus:border-blue-500 focus:ring-2 focus:ring-blue-200 '
                         'focus:outline-none transition duration-200 '
                         'placeholder-gray-400 text-gray-900',
                'placeholder': 'Enter your email address',
                'required': 'required',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg '
                         'focus:border-blue-500 focus:ring-2 focus:ring-blue-200 '
                         'focus:outline-none transition duration-200 '
                         'placeholder-gray-400 text-gray-900',
                'placeholder': 'e.g. +256 700 123 456',
                'required': 'required',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg '
                         'focus:border-blue-500 focus:ring-2 focus:ring-blue-200 '
                         'focus:outline-none transition duration-200 '
                         'placeholder-gray-400 text-gray-900 resize-y min-h-[110px]',
                'rows': 4,
                'placeholder': 'Optional: Briefly describe your project, system needs, or questions',
            }),
        }


from django import forms
from .models import TechCourseEnrollment


class TechCourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = TechCourseEnrollment
        fields = ['full_name', 'email', 'phone', 'address', 'remarks']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black'
            }),
            'remarks': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black'
            }),
        }
