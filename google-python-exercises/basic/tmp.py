# You are given a list of "employees". Every element of this list is
# a sublist that contains 2 elements. First element is the employee's
# name. Second element is the employee's salary.

def raisesalary(employee):
    return [employee[0], employee[1] * 1.3]

def underpaid(employee):
    return employee[1] < 30.0

def sum(employee1, employee2):
    return (employee1[1] + employee2[1])

employees = [['Alice', 20], ['Bob', 35], ['Carol', 25], ['John', 40]]

# Use the built-in function "filter" to get the list of "underpaid"
# employees that get less than $30 an hour. Also use the
# "underpaid" function defined above.

underpaidEmployees = filter(underpaid, employees) # <- your code

# Next, feed the data from underpaidEmployees to the function
# 'raisesalary' that will add 30% to the salary of every such
# employee. Use the built-in function 'map' for this part.

increasedEmployees =  map(raisesalary, underpaidEmployees)# <- your code

# Next, calculate the hourly total before and after, i.e. for
# the "underpaidEmployees" and for the "increasedEmployees".
# Use the built-in function "reduce" and the "sum" function
# provided for you.

hourlyBefore =  reduce(sum, underpaidEmployees)# <- your code
hourlyAfter =  reduce(sum, increasedEmployees)# <- your code

print 'Underpaid: ', underpaidEmployees
print 'Increased: ', increasedEmployees
print 'Before, per hour: ', hourlyBefore
print 'After, per hour: ', hourlyAfter
