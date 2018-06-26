1)
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


2) 
python manage.py makemigrations
python manage.py migrate
3)
python manage.py shell

    1 - User.objects.all()
    2 - User.objects.last()
    3 - User.objects.create(first_name="mary", last_name="geri", email_address="mary@geri.com", age=37)
    User.objects.create(first_name="Eric", last_name="Bob", email_address="eric@bob.com", age=32)
    User.objects.create(first_name="Lola", last_name="London", email_address="lola@london.com", age=1)
    4 - User.objects.first()
    5 - User.objects.order_by("-first_name")
    6 - user = User.objects.get(id=3)
    user.last_name = "Dog"
    user.save()
    7 - User.objects.get(id=4).delete()
