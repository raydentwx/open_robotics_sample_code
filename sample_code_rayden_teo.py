class Intern:
	def __init__(self, name, company, job):
		self.name = name
		self.company = company
		self.job = job
        
	def __str__(self):
		return f'Name: {self.name}\nCompany: {self.company}\nJob: {self.job}'

name = input("Enter your name: ")
company = input("Enter your company: ")
job = input("Enter your job: ")

intern1 = Intern(name, company, job)

print("\n")
print(intern1)
print("\nThis code was compiled by Rayden Teo, Nanyang Technological University Computer Science Undergraduate (2021 - 2025). Do review my CV and LinkedIn, and I hope to hear from you soon. :)") 
