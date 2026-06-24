from pyspark import SparkContext

sc = SparkContext("local[*]", "EmployeeRDDApp")

# Read CSV
data = sc.textFile("/app/employee.csv")

# Remove header
header = data.first()
rdd = data.filter(lambda x: x != header)

# Convert into structured tuples
employees = rdd.map(lambda x: x.split(",")) \
               .map(lambda x: (
                   int(x[0]),      # id
                   x[1],           # name
                   x[2],           # department
                   int(x[3])       # salary
               ))

# -----------------------------------------
# 1. Sort employees by salary descending
# -----------------------------------------
print("\n===== Employees Sorted By Salary =====")

sorted_emp = employees.sortBy(lambda x: x[3], ascending=False)

for emp in sorted_emp.collect():
    print(emp)

# -----------------------------------------
# 2. Total salary by department
# -----------------------------------------
print("\n===== Department Salary Totals =====")

dept_salary = employees.map(
    lambda x: (x[2], x[3])
).reduceByKey(
    lambda a, b: a + b
)

for dept in dept_salary.collect():
    print(dept)

# -----------------------------------------
# 3. Top 3 highest paid employees
# -----------------------------------------
top3 = sorted_emp.take(3)

with open("top3_employees.txt", "w") as f:
    f.write("Top 3 Highest Paid Employees\n\n")

    for emp in top3:
        f.write(
            f"ID:{emp[0]}, Name:{emp[1]}, "
            f"Department:{emp[2]}, Salary:{emp[3]}\n"
        )

print("\nTop 3 employees saved to top3_employees.txt")

sc.stop()