from django.contrib import admin

from .models import BlueCard, State, Strand, Subject, TeacherRegistration, Tutor


__author__ = "Rohan"

admin.site.register(BlueCard)
admin.site.register(State)
admin.site.register(Strand)
admin.site.register(Subject)
admin.site.register(TeacherRegistration)
admin.site.register(Tutor)

if __name__ == "__main__":
    pass
