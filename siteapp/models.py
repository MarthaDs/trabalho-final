from django.db import models
from django.utils import timezone
from django.db.models.fields import CharField


class PhysicalCharacteristic(models.Model):
	"""
		Class of physical attribute of candidate
	"""

	BEAUTY_CHOICES = [
		('pretty', 'Bela'),
		('ugly', 'Feia'),
	]

	SKIN_CHOICES = [
		('white', 'Branca'),
		('brown', 'Marrom'),
		('black', 'Preta'),
	]

	HAIR_CHOICES = [
		('straight', 'Liso'),
		('curly', 'Cacheado'),
		('coily', 'Crespo'),
	]

	FACIAL_TRACE = [
		('large', 'Traço Largo'),
		('thin', 'Traço Fino')
	]

	beauty = models.CharField(max_length=10,blank=True,
		unique=False, choices=BEAUTY_CHOICES)
	skin_color = models.CharField(max_length=10,blank=True,
		unique=False, choices=SKIN_CHOICES)
	hair_type = models.CharField(max_length=15,blank=True,
		unique=False, choices=HAIR_CHOICES)
	facial_trace = models.CharField(max_length=15,blank=True,
		unique=False, choices=FACIAL_TRACE)

	def __str__(self):
	  return '%s %s %s %s' % (self.beauty, self.skin_color, 
      self.hair_type, self.facial_trace)


class Intelect(models.Model):
	"""
		Class of intelect attribute of candidate
	"""
	
	INCLINATION_CHOICES = [
		('committed','Empenhada'),
		('lazy', 'Preguiçosa')
	]

	RELIABILITY_CHOICES = [
		('honest', 'Honesta'),
		('dishonest', 'Desonesta'),
	]

	NATURE_CHOICES = [
		('good_nature', 'Boa Indole'),
		('bad_nature', 'Má Indole'),
	]

	INTELLIGENCE_CHOICES = [
		('ingenious', 'Engenhosa'),
		('fool', 'Tola'),
	]

	inclination = models.CharField(max_length=15, blank=True,
		unique=False, choices=INCLINATION_CHOICES)
	reliability = models.CharField(max_length=15,blank=True,
		unique=False, choices=RELIABILITY_CHOICES)
	nature = models.CharField(max_length=15,blank=True,
		unique=False, choices=NATURE_CHOICES)
	intelligence = models.CharField(max_length=15,blank=True,
		unique=False, choices=INTELLIGENCE_CHOICES)

	def __str__(self):
	  return '%s %s %s %s' % (self.inclination, self.reliability, 
      self.nature, self.intelligence)

class SocialRace(models.Model):
	"""
		Class of candidate races
	"""

	RACE_CHOICES = [
		('white', 'Branca'),
		('black', 'Preta'),
	]

	race = models.CharField(max_length=10,blank=True,
		unique=False, choices=RACE_CHOICES)

	def __str__(self):
	  return self.race


class Stereotype(models.Model):
	"""
		Class creates stereotype
	"""

	STEREOTYPE_CHOICES = [
		('superior_race', 'Raça Superior'),
		('inferior_race', 'Raça Inferior'),
	]

	stereotype = CharField(max_length=15, blank=True,
		unique=False, choices=STEREOTYPE_CHOICES)

	def __str__(self):
	  return self.stereotype


class Candidate(models.Model):
	"""
		Class creates Candidate
	"""

	candidate_id = models.AutoField(primary_key=True)
	physical_characteristic = models.ForeignKey(PhysicalCharacteristic, null=True, blank=True, on_delete=models.CASCADE)
	intelect = models.ForeignKey(Intelect, null=True, blank=True, on_delete=models.CASCADE)
	race = models.ForeignKey(SocialRace, null=True, blank=True, on_delete=models.CASCADE)
	stereotype = models.ForeignKey(Stereotype, null=True, blank=True, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	job = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return '%s %s %s %s %s %s %s' % (self.candidate_id, self.physical_characteristic, 
      self.intelect, self.race, self.stereotype, self.created_date, self.job)