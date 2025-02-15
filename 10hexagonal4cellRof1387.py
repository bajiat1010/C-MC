
import math 
# Parameters 
R = 1.387  # Cell Radius in km 
n = 4  # Number of cells 
N = 60  # Total number of channels 
area = round(2.5981 * R**2)  # Area covered per cell (rounded) 
C = N / 4  # Number of channels per cell 
A = 9  # Traffic intensity from Erlang C chart with GOS = 0.05 and Au = 0.029 
 
# Question (a) 
Au = 0.029  # Traffic per user 
U = math.floor(A / Au)  # Total number of users 
U_per = round(U / area)  # Number of users per square km 
print(f"(a) Number of users per square km: {U_per} users/sq km\n") 
 
# Question (b) 
lambda_ = 1  # Arrival rate in hours 
H = (Au / lambda_) * 3600  # Holding time in seconds 
t = 10  # Time delay in seconds (assumed to be 10s as per the MATLAB code) 
Prb = math.exp((-(C - A) * t) / H)  # Probability of delay 
print(f"(b) The probability that a delayed call will have to wait: {Prb * 100:.2f}%\n") 
 
# Question (c) 
Prc = 0.05 * Prb * 100  # 5% probability of a delayed call 
print(f"(c) The probability that a call will be delayed: {Prc:.2f}%\n") 