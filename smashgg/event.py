class Event:
	id: int
	slug: str
	name: str
	startAt: int

	def __init__(self, id, slug, name, startAt):
		self.id = id
		self.slug = slug
		self.name = name
		self.startAt = startAt

	def __str__(self):
		return f"{self.id},'{self.slug}','{self.name}',{self.startAt}"