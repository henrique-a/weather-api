from django.db import models

# Create your models here.
class UserRequest(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.user_id

class WeatherData(models.Model):
    city_id = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    user_request = models.ForeignKey(UserRequest, related_name='weather_data', on_delete=models.CASCADE)