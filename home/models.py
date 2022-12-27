from django.db import models

# Create your models here.
class Data(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100)
    prodi = models.CharField(max_length=40)
    kelas = models.CharField(max_length=40)

    def __str__(self):
        return self.nama