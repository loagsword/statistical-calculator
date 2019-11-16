from src.Calculator.Addition import addition
from src.Calculator.Division import division


n = len(data)
m = mean(data)
std_err = sem(data)
h = std_err * t.ppf((1 + confidence) / 2, n - 1)

start = m - h
print start

end = m + h
print end
