# select id, first_name, last_name, department_id, MAX(salary)
# from ms_employee_salary 
# GROUP BY id, first_name, last_name, department_id order by id ASC;

from pyspark.sql import functions as F

result = ms_employee_salary.groupby('id', 'first_name', 'last_name', 'department_id') \
    .agg(F.max('salary')) \
    .orderBy('id')

result.toPandas()
