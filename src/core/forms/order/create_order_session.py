from django import forms

from core.models.certificate import Certificate
from core.models.property import Property
from core.services.certificate.group_items import build_child_parent_map


class CreateOrderSessionForm(forms.Form):
    customer_name = forms.CharField(
        max_length=254,
        label="Full Name",
        error_messages={
            "required": "A name is required.",
        },
    )
    customer_company_name = forms.CharField(
        max_length=200,
        label="Business",
        error_messages={
            "required": "A business is required.",
        },
    )

    property_id = forms.IntegerField(
        widget=forms.HiddenInput(),
        error_messages={
            "required": "A property is required.",
        },
    )

    lines = forms.JSONField(
        widget=forms.HiddenInput(),
        error_messages={
            "required": "A certificate is required",
        },
    )

    def clean_customer_name(self):
        data = self.cleaned_data["customer_name"]
        return data

    def clean_customer_company_name(self):
        data = self.cleaned_data["customer_company_name"]
        return data

    def clean_property_id(self):
        property_id = self.cleaned_data["property_id"]
        try:
            Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise forms.ValidationError("Invalid property ID")
        return property_id

    def clean_lines(self):
        lines = self.cleaned_data["lines"]
        if not isinstance(lines, list):
            raise forms.ValidationError("Lines must be a list")
        for line in lines:
            if not isinstance(line, dict):
                raise forms.ValidationError("Order line must be a dict")
            elif "certificate_id" not in line:
                raise forms.ValidationError("Order line have a certificate_id")
            elif not isinstance(line["certificate_id"], int):
                raise forms.ValidationError("Certificate ID must be a number")
            elif "fee_id" in line and not isinstance(line["fee_id"], int):
                raise forms.ValidationError("Fee ID must be a number")
        return lines

    def clean(self):
        cleaned_data = super().clean()
        order_lines = cleaned_data.get("lines", [])

        certificates = Certificate.objects.all()
        certificate_map = {obj.id: obj for obj in certificates}
        child_parent_map = build_child_parent_map(certificates)

        selected_certificates = set()

        # First pass: Add all selected certificates
        for line in order_lines:
            certificate_id = line["certificate_id"]
            if certificate_id not in certificate_map:
                raise forms.ValidationError(
                    f"Certificate with ID {certificate_id} not found."
                )
            selected_certificates.add(certificate_map[certificate_id])

        # Second pass: Check for conflicts
        for certificate in selected_certificates:
            parents = child_parent_map[certificate]
            for parent in parents:
                if parent in selected_certificates:
                    raise forms.ValidationError(
                        f"Select either {parent.name} or {certificate.name}, "
                        "not both."
                    )

        return cleaned_data
