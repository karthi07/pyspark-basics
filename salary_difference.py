# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
db_employee = db_employee.join(db_dept, db_employee['department_id'] == db_dept['id'])\
    .filter(db_dept['department'].isin(['engineering','marketing'])) \
    .groupby() \
    .pivot('department') \
    .agg(F.max('salary')) \
    .select(F.abs(F.col('engineering') - F.col('marketing')).alias('salary_difference'))


# To validate your solution, convert your final pySpark df to a pandas df
db_employee.toPandas()