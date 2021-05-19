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
		unique=True, choices=BEAUTY_CHOICES)
	skin_color = models.CharField(max_length=10,blank=True,
		unique=True, choices=SKIN_CHOICES)
	hair_type = models.CharField(max_length=15,blank=True,
		unique=True, choices=HAIR_CHOICES)
	facial_trace = models.CharField(max_length=15,blank=True,
		unique=True, choices=FACIAL_TRACE)


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
		unique=True, choices=INCLINATION_CHOICES)
	reliability = models.CharField(max_length=15,blank=True,
		unique=True, choices=RELIABILITY_CHOICES)
	nature = models.CharField(max_length=15,blank=True,
		unique=True, choices=NATURE_CHOICES)
	intelligence = models.CharField(max_length=15,blank=True,
		unique=True, choices=INTELLIGENCE_CHOICES)


class SocialRace(models.Model):
	"""
		Class of candidate races
	"""

	RACE_CHOICES = [
		('white', 'Branca'),
		('black', 'Preta'),
	]

	race = models.CharField(max_length=10,blank=True,
		unique=True, choices=RACE_CHOICES)


class Stereotype(models.Model):
	"""
		Class creates stereotype
	"""

	STEREOTYPE_CHOICES = [
		('superior_race', 'Raça Superior'),
		('inferior_race', 'Raça Inferior'),
	]

	stereotype = CharField(max_length=15, blank=True,
		unique=True, choices=STEREOTYPE_CHOICES)


class Candidate(models.Model):
	"""
		Class creates Candidate
	"""

	candidate_id = models.AutoField(primary_key=True)
	physical_characteristic = models.ForeignKey(PhysicalCharacteristic, blank=True, on_delete=models.CASCADE)
	intelect = models.ForeignKey(Intelect, blank=True, on_delete=models.CASCADE)
	race = models.ForeignKey(SocialRace, blank=True, on_delete=models.CASCADE)
	stereotype = models.ForeignKey(Stereotype, blank=True, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.candidate_id