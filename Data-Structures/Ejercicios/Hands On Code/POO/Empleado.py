import os

class Empleado:

    def __init__(this,name : str,position : str,salary : int,years : int):
        this.name = name
        this.position = position
        this.salary = salary
        this.years = years

    def over_salary(this):
        if this.salary > 20000:
            return 'Your salary is over 20.000 euros'

    def promoted (this, promotion : str):
        if promotion[0].capitalize() == 'P': return True
        else: return False

    def file_write(employers : list):
        file = str('Data-Structures\Ejercicios\Hands On Code\POO\List of employers.txt')
        filepath = os.path.join(file)
        with open(filepath,'w+',encoding="utf-8") as file:
            for element in employers:
                if element.salary < 20000:
                    file.write('Name: '+str(element.name)+' Position: '+str(element.position)+' Salary: '+str(element.salary)+' Years: '+str(element.years))
                    file.write('\n')

    def create_employers():
        employers = []
        e1 = Empleado('Lucia','Writer',18000,1)
        e2 = Empleado('Pedro','Software Analyst',36000,4)
        e3 = Empleado('Natalia','Web Design',22000,2)
        e4 = Empleado('Jorge','Security',19000,2)
        e5 = Empleado('Oscar','Editor',28000,5)
        e6 = Empleado('Allie','Human Resources',18000,1)
        e7 = Empleado('Sod','Software Engineer',45000,8)
        e8 = Empleado('Sergio','Backend Developer',18000,1)
        e9 = Empleado('Nerea','Full-Stack Developer',19600,1)
        e10 = Empleado('Rodrigo','Receptionist',18000,2)
        employers.append(e1)
        employers.append(e2)
        employers.append(e3)
        employers.append(e4)
        employers.append(e5)
        employers.append(e6)
        employers.append(e7)
        employers.append(e8)
        employers.append(e9)
        employers.append(e10)
        return employers