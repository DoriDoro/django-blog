# from django.contrib import admin
#
# from contact.models import ContactRequest
#
# no saving of the model yet
#
# @admin.register(ContactRequest)
# class ContactRequestAdmin(admin.ModelAdmin):
#     list_display = ["first_name", "email", "subject", "customer_feedback"]
#     list_filter = ["first_name", "email", "subject", "customer_feedback"]
#     search_fields = ["first_name", "email", "subject", "customer_feedback"]
#     date_hierarchy = "submitted_at"
#     ordering = ["submitted_at"]
#     show_facets = admin.ShowFacets.ALWAYS
