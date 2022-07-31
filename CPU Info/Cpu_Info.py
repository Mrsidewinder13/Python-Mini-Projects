# pip install py-cpuinfo
import cpuinfo as cpu

brand = cpu.get_cpu_info()['brand_raw']
bits = cpu.get_cpu_info()['bits']

all_data = cpu.get_cpu_info()

print(f' Brand: {brand} ')
print(f' bits: {bits}')

# print(all_data)