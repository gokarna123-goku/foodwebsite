from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# from django.contrib.auth.usermanager import UserManager
from django.conf import settings
# from nepali_datetime_field.models import NepaliDateField
# import nepali_datetime
# from evaluate.models import GRADE_CHOICES, SECTION_CHOICES
GRADE_CHOICES = (
    ("NUR", "NURSERY"),
    ("LKG", "Lower Kinder Garden"),
    ("UKG", "Lower Kinder Garden"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("BBS", "Bachelor's of Business Studies"),
)

SECTION_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
)


COURSES_CHOICES = (
    ("ENG", "ENGLISH"),
    ("NEP", "NEPALI"),
    ("SOC", "Social Studies"),
    ("MAT", "MATHS"),
    ("SCI", "SCIENCE"),
)



ADDRESS_CHOICES = [
    ('Mechi', (
            ('bhojpur', 'Bhojpur'),
            ('dhankuta', 'Dhankuta'),
            ('ilam', 'Ilam'),
            ('jhapa', 'Jhapa'),
            ('khotang', 'Khotang'),
            ('morang', 'Morang'),
            ('okhaldhunga', 'Okhaldhunga'),
            ('panchthar', 'Panchthar'),
            ('sankhuwasabha', 'Sankhuwasabha'),
            ('solukhumbu', 'Solukhumbu'),
            ('sunsari', 'Sunsari'),
            ('taplejung', 'Taplejung'),
            ('terhathum', 'Terhathum'),
            ('udayapur', 'Udayapur'),
        )
    ),
    ('Pardesh 2', (
            ('bara', 'Bara'),
            ('dhanusa', 'Dhanusa'),
            ('mahottari', 'Mahottari'),
            ('parsa', 'Parsa'),
            ('rautahat', 'Rautahat'),
            ('saptari', 'Saptari'),
            ('sarlahi', 'Sarlahi'),
            ('siraha', 'Siraha'),
        )
    ),
    ('Bagmati', (
            ('bhaktapur ', 'Bhaktapur '),
            ('chitwan', 'Chitwan'),
            ('dhading', 'Dhading'),
            ('dolakha', 'Dolakha'),
            ('kathmandu', 'Kathmandu'),
            ('nuwakot', 'Nuwakot'),
            ('kavrepalanchok', 'Kavrepalanchok'),
            ('lalitpur', 'Lalitpur'),
            ('makawanpur', 'Makawanpur'),
            ('ramechhap', 'Ramechhap'),
            ('rasuwa', 'Rasuwa'),
            ('saindhuli', 'Sindhuli'),
            ('sindhupalchok', 'Sindhupalchok'),
        )
    ),
    ('Gandaki', (
            ('baglung ', 'Baglung '),
            ('gorkha', 'Gorkha'),
            ('kaski', 'Kaski'),
            ('lamjung', 'Lamjung'),
            ('manang', 'Manang'),
            ('mustang', 'Mustang'),
            ('myagdi', 'Myagdi'),
            ('nawalpur', 'Nawalpur'),
            ('parbat', 'Parbat'),
            ('syangja', 'Syangja'),
        )
    ),
    ('Lumbini', (
            ('arghakhanchi ', 'Arghakhanchi '),
            ('banke', 'Banke'),
            ('bardiya', 'Bardiya'),
            ('dang', 'Dang'),
            ('gulmi', 'Gulmi'),
            ('kapilvastu', 'Kapilvastu'),
            ('parasi', 'Parasi'),
            ('palpa', 'Palpa'),
            ('pyuthan', 'Pyuthan'),
            ('rolpa', 'Rolpa'),
            ('rukum', 'Rukum'),
            ('rupandehi', 'Rupandehi'),
        )
    ),
    ('Pradesh 6', (
            ('dailekh  ', 'Dailekh'),
            ('dolpa ', 'Dolpa'),
            ('humla', 'Humla'),
            ('jajarkot ', 'Jajarkot'),
            ('jumla ', 'Jumla'),
            ('kalikot ', 'Kalikot'),
            ('mugu', 'Mugu'),
            ('rukum', 'Rukum Paschim'),
            ('salyan ', 'Salyan '),
            ('surkhet ', 'Surkhet '),
        )
    ),
    ('Pradesh 7', (
            ('achham ', 'Achham '),
            ('baitadi', 'Baitadi'),
            ('bajhang', 'Bajhang'),
            ('bajura', 'Bajura'),
            ('dadeldhura', 'Dadeldhura'),
            ('kapilvastu', 'Kapilvastu'),
            ('darchula', 'Darchula'),
            ('doti', 'Doti'),
            ('kailali', 'Kailali'),
            ('kanchanpur', 'Kanchanpur'),
        )
    ),
]
# STUDENT = 1
# TEACHER = 2
# SUPERVISOR = 3
# ROLE_CHOICES = (
#     (STUDENT, 'Student'),
#     (TEACHER, 'Teacher'),
#     (SUPERVISOR, 'Supervisor'),
# )

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True,)
    email = models.EmailField(verbose_name='email address', max_length=255,)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    email_confirmed = models.BooleanField(default=False) #initially this field is false but will se chan
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #emaila nd password are required fields and first name and last name is inherited from the user creation model

    #instanciate the usermanager object
    object = UserManager()

    # def get_username(self):
    #     username = self.first_name+"."+self.last_name
    #     return username

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name


#Teachers
class Teacher(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    teacher_name = models.CharField(max_length=255)
    # manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    DOB = models.CharField(max_length=255)
    permanent_Address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    temporary_address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    teacher_class_level = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    # bio = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.teacher_name

class Gradecourse(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    course_grade_level = models.CharField(max_length=20, null=True, blank=True)
    # student_section = models.CharField(max_length=20, choices=SECTION_CHOICES) #models.CharField(max_length=255)
    student_courses_1 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_2 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_3 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_4 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_5 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_6 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_7 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_8 = models.CharField(max_length=20, null=True, blank=True)
    student_courses_9 = models.CharField(max_length=20, null=True, blank=True)
    # teachers_remarks = models.CharField(max_length=255)
    # teachers_comments = models.CharField(max_length=255)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.course_grade_level
# Students
class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=255)
    DOB = models.CharField(max_length=255)
    permanent_Address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    temporary_address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    father_academic_background = models.CharField(max_length=255)
    behavior_impression = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    mother_academic_background = models.CharField(max_length=255)
    family_income_source = models.CharField(max_length=255)
    student_class_level = models.ForeignKey(Gradecourse, on_delete=models.CASCADE, null=True, blank=True, related_name="student_courses")
    student_section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    teachers_comments = models.CharField(max_length=255,  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # admission_year = NepaliDateField()
    # avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    # bio = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.student_name


class Teacher_Course_Assignment(models.Model):
    # teacher = models.ForeignKey(Student_Admissons, on_delete=models.CASCADE,)
    # teacher_section = models.CharField(max_length=20, choices=SECTION_CHOICES) #models.CharField(max_length=255)
    teacher_courses_1 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_2 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_3 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_4 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_5 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_6 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_7 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_8 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teacher_courses_9 = models.CharField(max_length=20, choices=COURSES_CHOICES)
    teachers_remarks = models.CharField(max_length=255)
    teachers_comments = models.CharField(max_length=255)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE,)

    def __str__(self):              # __unicode__ on Python 2
        return self.student.student_name

#Principal and Admin permissions
class Principal_Admin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    admin_name = models.CharField(max_length=255)
    DOB = models.CharField(max_length=255)
    permanent_Address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    temporary_address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    teacher_class_level = models.CharField(max_length=255)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):              # __unicode__ on Python 2
        return self.admin_name

#Managers permissions
class Director(models.Model):
    management = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mgmt_name = models.CharField(max_length=255)
    DOB = models.CharField(max_length=255)
    permanent_Address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    temporary_address = models.CharField(max_length=20, choices=ADDRESS_CHOICES) #models.CharField(max_length=255)
    ward_tole = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    teacher_class_level = models.CharField(max_length=255)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):              # __unicode__ on Python 2
        return self.mgmt_name

# Extending User Model Using a One-To-One Link
# class Profile(models.Model):
#     STUDENT = 1
#     TEACHER = 2
#     SUPERVISOR = 3
#     ROLE_CHOICES = (
#         (STUDENT, 'Student'),
#         (TEACHER, 'Teacher'),
#         (SUPERVISOR, 'Supervisor'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     location = models.CharField(max_length=30, blank=True)
#     birthdate = models.DateField(null=True, blank=True)
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#     def save(self, *args, **kwargs):
#         super(Profile, self).save(*args, **kwargs)
#         img = Image.open(self.avatar.path)
#         if img.height > 150 or img.width > 150:
#             output_size = (150, 150)
#             img.thumbnail(output_size)
#             img.save(self.avatar.path)
