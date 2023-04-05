# Calculating the salary of employees
class Employee:
    def _init_(self, name, basic_salary, qualification):
        self.name = name
        self.basic_salary = basic_salary
        self.qualification = qualification
    
    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False
    
    def validate_qualification(self):
        if self.qualification == "Bachelors" or self.qualification == "Masters":
            return True
        else:
            return False

class Graduate(Employee):
    def _init_(self, name, basic_salary, qualification, job, cgpa):
        super()._init_(name, basic_salary, qualification)
        self.job = job
        self.cgpa = cgpa
    
    def validate_job_band(self):
        valid_jobs = ["A", "B", "C"]
        if self.job in valid_jobs:
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job():
            pf = 0.12 * self.basic_salary
            if self.cgpa >= 4 and self.cgpa <= 4.25:
                tpi = 1000
            elif self.cgpa > 4.25 and self.cgpa <= 4.5:
                tpi = 1700
            elif self.cgpa > 4.5 and self.cgpa <= 4.75:
                tpi = 3200
            else:
                tpi = 5000
            
            if self.job == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job == "B":
                incentive = 0.06 * self.basic_salary
            else:
                incentive = 0.1 * self.basic_salary
            
            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1

class Lateral(Employee):
    def _init_(self, name, basic_salary, qualification, job, skill_set):
        super()._init_(name, basic_salary, qualification)
        self.job = job
        self.skill_set = skill_set
    
    def validate_job_band(self):
        valid_jobs = ["D", "E", "F"]
        if self.job in valid_jobs:
            return True
        else:
            return False
    
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job():
            pf = 0.12 * self.basic_salary
            if self.skill_set == "AGP":
                bonus = 6500
            elif self.skill_set == "AGPT":
                bonus = 8200
            elif self.skill_set == "AGDEV":
                bonus = 11500
            else:
                bonus = 0
            
            if self.job == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job == "E":
                incentive = 0.16 * self.basic_salary
            else:
                incentive = 0.2 * self.basic_salary
            
            gross_salary = self.basic_salary + pf + bonus + incentive
            return gross_salary
        else:
            return -1

# Testing
g = Graduate("John", 5000, "Bachelors", "B", 4.5)
print("Graduate details:")
print("Name:", g.name)
print("Basic Salary:", g.basic_salary)
