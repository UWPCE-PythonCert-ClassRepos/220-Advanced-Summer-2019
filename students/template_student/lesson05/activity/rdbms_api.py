class BaseModel(Model):
   class Meta:
       database = database

class Person(BaseModel):
   """
     This class defines Person, which maintains details of someone
     for whom we want to research career to date.
   """

   person_name = CharField(primary_key = True, max_length = 30)
   lives_in_town = CharField(max_length = 40)
   nickname = CharField(max_length = 20, null = True)

class Job(BaseModel):
   """
     This class defines Job, which maintains details of past Jobs
     held by a Person.
   """
   job_name = CharField(primary_key = True, max_length = 30)
   start_date = DateField(formats = 'YYYY-MM-DD')
   end_date = DateField(formats = 'YYYY-MM-DD')
   salary = DecimalField(max_digits = 7, decimal_places = 2)
   person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)
new_person = Person.create(
  person_name = 'Fred',
  lives_in_town = 'Seattle',
  nickname = 'Fearless')
   new_person.save()

aperson = Person.get(Person.person_name == 'Fred')
