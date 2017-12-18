from django.db import models


class Tutor(models.Model):

    NOT_VERIFIED = "N"
    PENDING = "P"
    VERIFIED = "V"

    FEMALE = "F"
    MALE = "M"
    NON_BINARY = "N"
    PREFER_NOT_TO_SAY = "X"

    GENDER_CHOICES = (
        (FEMALE, "Female"),
        (MALE, "Male"),
        (NON_BINARY, "Gender Non-Binary"),
        (PREFER_NOT_TO_SAY, "Prefer Not To Say"),
    )

    VERIFIED_CHOICES = (
        (NOT_VERIFIED, "Not Verified"),
        (PENDING, "Pending"),
        (VERIFIED, "Verified"),
    )

    first_name = models.CharField(max_length=100,
                                  null=False,
                                  )
    middle_name = models.CharField(max_length=100,
                                   null=True,
                                   blank=True,
                                   default=None,
                                   )
    family_name = models.CharField(max_length=100,
                                   null=False,
                                   )
    nick_name = models.CharField(max_length=50,
                                 null=True,
                                 blank=True,
                                 default=None,)
    date_of_birth = models.DateField(null=False,)
    gender = models.CharField(choices=GENDER_CHOICES,
                              null=False,
                              max_length=1,
                              )
    about = models.TextField()
    abn = models.IntegerField(null=True,
                              blank=True,
                              default=None,
                              )
    email = models.EmailField(null=False,
                              unique=True,
                              )
    # TODO: Proper validation for numbers, and formats.
    mobile = models.CharField(null=False,
                              max_length=15,
                              unique=True,
                              )
    verified = models.CharField(choices=VERIFIED_CHOICES,
                                null=False,
                                default=NOT_VERIFIED,
                                max_length=1,
                                )

    class Meta(object):
        ordering = ("first_name", "family_name")

    def __str__(self):
        return f"{self.first_name} {self.family_name}"


class State(models.Model):

    ACT = "ACT"
    NSW = "NSW"
    NT = "NT"
    QLD = "QLD"
    SA = "SA"
    TAS = "TAS"
    VIC = "VIC"
    WA = "WA"

    STATE_OPTIONS = (
        (ACT, "A.C.T."),
        (NSW, "New South Wales"),
        (NT, "Northern Territory"),
        (QLD, "Queensland"),
        (SA, "South Australia"),
        (TAS, "Tasmania"),
        (VIC, "Victoria"),
        (WA, "Western Australia"),
    )

    name = models.CharField(choices=STATE_OPTIONS,
                            null=False,
                            max_length=3,
                            unique=True)

    class Meta(object):
        ordering = ("name",)

    def __str__(self):
        return self.name


class BlueCard(models.Model):

    tutor = models.ForeignKey(Tutor)
    state = models.ForeignKey(State)
    identifier = models.CharField(max_length=50,
                                  null=False,
                                  )
    expiry = models.DateField(null=False)
    # TODO: Keep encrypted scans of blue cards.
    # TODO: Make superclass to combine with TeacherRegistration
    # TODO: Add validation for identifiers, and dates.

    def __str__(self):
        return f"BlueCard({self.tutor}, {self.expiry})"


class TeacherRegistration(models.Model):

    tutor = models.ForeignKey(Tutor)
    state = models.ForeignKey(State)
    identifier = models.CharField(max_length=50,
                                  null=False,
                                  )
    expiry = models.DateField(null=False)

    def __str__(self):
        return f"TeacherRegistration({self.tutor}, {self.expiry})"


class Student(models.Model):

    KINDERGARTEN = "K"
    Y1 = "1"
    Y2 = "2"
    Y3 = "3"
    Y4 = "4"
    Y5 = "5"
    Y6 = "6"
    Y7 = "7"
    Y8 = "8"
    Y9 = "9"
    Y10 = "10"
    Y11 = "11"
    Y12 = "12"

    YEAR_CHOICES = (
        (KINDERGARTEN, "Kindergarten"),
        (Y1, "Year 1"),
        (Y2, "Year 2"),
        (Y3, "Year 3"),
        (Y4, "Year 4"),
        (Y5, "Year 5"),
        (Y6, "Year 6"),
        (Y7, "Year 7"),
        (Y8, "Year 8"),
        (Y9, "Year 9"),
        (Y10, "Year 10"),
        (Y11, "Year 11"),
        (Y12, "Year 12"),
    )

    first_name = models.CharField(max_length=100,
                                  null=False,
                                  )
    middle_name = models.CharField(max_length=100,
                                   null=True,
                                   blank=True,
                                   default=None,
                                   )
    family_name = models.CharField(max_length=100,
                                   null=False,
                                   )
    year = models.CharField(choices=YEAR_CHOICES,
                            null=False,
                            max_length=2,
                            )
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(null=False,
                              unique=True,)

    class Meta(object):
        ordering = ("first_name", "family_name")

    def __str__(self):
        return f"{self.first_name} {self.family_name}"


class Subject(models.Model):

    name = models.CharField(max_length=50,
                            null=False,
                            unique=True
                            )
    primary_subject = models.BooleanField(default=False,
                                          null=False,
                                          )
    secondary_subject = models.BooleanField(default=True,
                                            null=False,
                                            )

    class Meta(object):
        ordering = ("name",)

    def __str__(self):
        return self.name


class Strand(models.Model):

    name = models.CharField(max_length=100,
                            null=False,
                            unique=True,
                            )
    subject = models.ForeignKey(Subject)
    primary_subject = models.BooleanField(default=False,
                                          null=False,
                                          )
    secondary_subject = models.BooleanField(default=True,
                                            null=False)

    class Meta(object):
        ordering = ("subject", "name",)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    pass
