import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xl = pd.read_csv("Stats.csv",encoding='utf-8')
df = pd.DataFrame(xl)
print df
salarySD=df['Salary in Rs.'].std()
variancesalary=df['Salary in Rs.'].var()


print "Standard deviation of salary"
print salarySD
print "variance of salary"
print variancesalary
