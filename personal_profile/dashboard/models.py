from django.db import models


class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

class RareMetalPrice(models.Model):
	PALLADIUM = 'PA'
	RUTHENIUM = 'RU'
	PLATINUM = 'PL'
	IRIDIUM = 'IR'
	RHODIUM = 'RO'

	HONG_KONG = 'HK'
	LONDON = 'LO'
	NEW_YORK = 'NY'

	metals = [
		(PALLADIUM, 'PALLADIUM'),
		(RUTHENIUM, 'RUTHENIUM'),
		(PLATINUM, 'PLATINUM'),
		(IRIDIUM, 'IRIDIUM'),
		(RHODIUM, 'RHODIUM')
	]

	cities = [
		(HONG_KONG, 'HONG_KONG'),
		(LONDON, 'LONDON'),
		(NEW_YORK, 'NEW_YORK')
	]

	metal_type = models.CharField(
		max_length=2,
		choices=metals)

	date = models.DateField()

	location = models.CharField(
		max_length=2,
		choices=cities
		)

	price = models.DecimalField(max_digits=7, decimal_places=2)

class RareMetalSupplyAndDemand(models.Model):
	Year = models.DateField()
	South_Africa = 'SA'
	Russia = 'RU'
	Russia_Primary = 'RP'
	Russia_Stock_Sales	= 'RS'	
	North_America = 'NA'
	Zimbabwe = 'ZI'
	Others = 'OT'

	places = [
		(South_Africa, 'South Africa'),
		(Russia, 'Russia'),
		(Russia_Primary, 'Russia Primary'),
		(Russia_Stock_Sales, 'Russia Stock Sales'),
		(North_America, 'North_America'),
		(Zimbabwe, 'Zimbabwe'),
		(Others, 'Others')
	]

	Total_Supply = models.DecimalField(max_digits=7, decimal_places=2)
	Total_Demand = models.DecimalField(max_digits=7, decimal_places=2)
	Recycling = models.DecimalField(max_digits=7, decimal_places=2)
	Net_Demand = models.DecimalField(max_digits=7, decimal_places=2)
	Movements = models.DecimalField(max_digits=7, decimal_places=2)

	location = models.CharField(
		max_length=2,
		choices=places
		)	
	
