import graphene

from graphene_django.types import DjangoObjectType

from .models import BlueCard, State, Strand, Student, Subject, TeacherRegistration, Tutor

__author__ = "Rohan"


class BlueCardType(DjangoObjectType):
    class Meta(object):
        model = BlueCard
        interfaces = (graphene.Node,)


class StateType(DjangoObjectType):
    class Meta(object):
        model = State
        interfaces = (graphene.Node,)


class StrandType(DjangoObjectType):
    class Meta(object):
        model = Strand
        interfaces = (graphene.Node,)


class StudentType(DjangoObjectType):
    class Meta(object):
        model = Student
        interfaces = (graphene.Node,)


class SubjectType(DjangoObjectType):
    class Meta(object):
        model = Subject
        interfaces = (graphene.Node,)


class TeacherRegistrationType(DjangoObjectType):
    class Meta(object):
        model = TeacherRegistration
        interfaces = (graphene.Node,)


class TutorType(DjangoObjectType):
    class Meta(object):
        model = Tutor
        interfaces = (graphene.Node,)


class Query(object):
    all_tutors = graphene.List(TutorType)
    all_subjects = graphene.List(SubjectType)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def resolve_all_tutors(self, info, **kwargs):
        return Tutor.objects.all()


if __name__ == "__main__":
    pass
