from django.core.exceptions import ValidationError

def validate_email(value):
		email=value
		if ".edu" in email:
			raise ValidationError("we don't accept edu emails")
		
CATEGORIES =['Mexican', 'Asian', 'American', 'Whatever']

def validate_category(value):
	cat=value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError("this is not in categories")