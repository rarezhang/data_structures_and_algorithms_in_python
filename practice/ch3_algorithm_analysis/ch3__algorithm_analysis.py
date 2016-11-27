# p 133
## measure elapsed time
from time import time
start_time = time()
for i in range(10):
    i
end_time = time()
elapse = end_time - start_time
print(elapse)