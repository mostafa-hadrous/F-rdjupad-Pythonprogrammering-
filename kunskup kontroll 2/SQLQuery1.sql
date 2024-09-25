use DS 
go

select * from [Employee Sample Data]

select Full_Name,
	   Job_Title,
	   Country,
	   Annual_Salary * Bonus as 'Bonus'
 from [Employee Sample Data]
 order by (Bonus)

select Department, 
		count(Department) as 'Number of Employees'
		from [Employee Sample Data]
		where Exit_Date is null
		group by(Department)
		order by ([Number of Employees])

select Department, 
		count(Department) as 'Number of Employees'
		from [Employee Sample Data]
		where Exit_Date is not null
		group by(Department)
		order by ([Number of Employees])


select Department, 
		count(Department) as 'Number of Employees'
		from [Employee Sample Data]
		where Exit_Date is null 
		or Country like '%Brazil%'
		group by(Department)
		order by ([Number of Employees])



select count(Department) 'Total number of Employees' from [Employee Sample Data]
	where Country like '%Brazil%' or
	Country like '%China%'

select Country,
	   COUNT(country) as'Number of Employee',
		sum(Annual_Salary) as 'Total Annual Salaries',
		sum(Annual_Salary * Bonus)as 'Bonus'
	   from [Employee Sample Data]
	   where Exit_Date is null
	   group by (Country)

select Country,
	   COUNT(country) as'Number of Employee',
		sum(Annual_Salary) as 'Total Annual Salaries'
	   from [Employee Sample Data]
	   where Exit_Date is not null
	   group by (Country)

select sum(Annual_Salary) ' Total Salaries' from [Employee Sample Data]
where Exit_Date is null

select sum(Annual_Salary) ' Total Salaries' from [Employee Sample Data]
where Exit_Date is not null

select Gender,
	   COUNT(Gender) as 'Number of Gender'
	   from [Employee Sample Data]
	   where Exit_Date is null
	   group by (Gender)
	   

select year (Hire_Date) as 'Start year',
       count (Hire_Date) 'Number of Employee' 
	   from [Employee Sample Data]
	   group by year (Hire_Date)
	   order by year (Hire_Date)

select AVG(Age) 'Avg age in the company' from [Employee Sample Data]
where Exit_Date is null

select Annual_Salary*Bonus
from [Employee Sample Data]


