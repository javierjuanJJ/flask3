class Job:
    def __init__(self, id, title, location, salary, currency, responsibilities, requirements, created_at, updated_at):
        self.id = id
        self.title = title
        self.location = location
        self.salary = salary
        self.currency = currency
        self.responsibities = responsibilities
        self.requirements = requirements
        self.created_at = created_at
        self.updated_at = updated_at