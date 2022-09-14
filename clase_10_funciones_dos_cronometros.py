import time

start = 10
end = -1

for x in range(start, end, -1):
    time.sleep(1)
    print(f'{x:02d}', end="\r")

     
for x in range(start, end, -1):
    time.sleep(1)
    print(f'{x:02d}', end="\t")


for x in range(start, end, -1):
    time.sleep(1)
    print(f'{x:02d}', end="\n")
