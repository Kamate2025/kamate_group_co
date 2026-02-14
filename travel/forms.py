from django import forms
from .models import ContactInquiry, TravelRequest


class ContactInquiryForm(forms.ModelForm):

    class Meta:
        model = ContactInquiry
        fields = ["name", "email", "phone", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Your full name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "input-field",
                "placeholder": "Your email address"
            }),
            "phone": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "WhatsApp or phone number"
            }),
            "message": forms.Textarea(attrs={
                "class": "input-field",
                "rows": 4,
                "placeholder": "Type your inquiry here..."
            }),
        }
        

class TravelRequestForm(forms.ModelForm):

    class Meta:
        model = TravelRequest
        fields = "__all__"

        widgets = {
            "service": forms.Select(attrs={
                "class": "input-field"
            }),
            "name": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Full Name"
            }),
            "phone": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "WhatsApp Number"
            }),
            "email": forms.EmailInput(attrs={
                "class": "input-field",
                "placeholder": "Email (Optional)"
            }),
            "departure_airport": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Departing Airport"
            }),
            "destination": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Destination"
            }),
            "travel_date": forms.DateInput(attrs={
                "type": "date",
                "class": "input-field"
            }),
            "message": forms.Textarea(attrs={
                "class": "input-field",
                "rows": 4,
                "placeholder": "Provide additional details (Optional)"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        service = cleaned_data.get("service")

        if service and service.name == "Flight Booking":
            if not cleaned_data.get("departure_airport"):
                self.add_error("departure_airport", "Required for flight booking.")
            if not cleaned_data.get("destination"):
                self.add_error("destination", "Required for flight booking.")
            if not cleaned_data.get("travel_date"):
                self.add_error("travel_date", "Required for flight booking.")

        return cleaned_data
