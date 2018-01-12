
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xl = pd.read_csv("Stats.csv",encoding='utf-8')
df = pd.DataFrame(xl)
print df
salarymean=df['Salary in Rs.'].mean()
modesalary=df['Salary in Rs.'].mode()
mediansalary=df['Salary in Rs.'].median()

print "mean of salary"
print salarymean
print "mode of salary"
print modesalary
print "median of salary"
print mediansalary

#print df
#print df.iloc[0]
