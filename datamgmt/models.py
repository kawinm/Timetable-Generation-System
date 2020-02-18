from django.db import models

class Staff(models.Model):
    staff_name = models.CharField(max_length=200)
    staff_dept = models.CharField(max_length=200)

    def __str__(self):
        return self.staff_name

class Group(models.Model):
    group_dept = models.CharField(max_length=50)
    group_sem = models.IntegerField(default=0)
    group_strength = models.IntegerField(default=0)

    def __str__(self):
        return self.group_dept + "-" + str(self.group_sem)

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=50)
    hours_per_week = models.IntegerField(default=0)
    span = models.IntegerField(default=1)
    staff_handling = models.ForeignKey(Staff, on_delete=models.CASCADE)
    to_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_code + " - " + self.subject_name
