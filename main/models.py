from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)  # Tiêu đề của dự án
    description = models.TextField()  # Mô tả dự án
    technology = models.CharField(max_length=200)  # Các công nghệ sử dụng trong dự án
    image = models.ImageField(upload_to='')  # Ảnh của dự án
    link = models.URLField(blank=True, null=True)  # Liên kết đến dự án (nếu có)
    date = models.DateField()  # Ngày tạo dự án
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)  # Tên của người liên hệ
    email = models.EmailField()  # Email của người liên hệ
    message = models.TextField()  # Tin nhắn của người liên hệ
    date = models.DateTimeField(auto_now_add=True)  # Ngày gửi liên lạc
    
    def __str__(self):
        return self.name
        
