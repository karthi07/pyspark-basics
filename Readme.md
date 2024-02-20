## Week 1 
1. Salaries Differences
 - Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.
    - salary difference -> - join tables -> filter dept -> groupby -> agg salary
2. Finding Updated Records
 - We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.
    - employee_salary.groupby('all fields,').agg(F.max(salary)).sort

