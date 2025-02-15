import math 
 
def calculate_frequency_reuse_factor(N): 
    Q = math.sqrt(3 * N) 
    return Q 
 
def calculate_SIR(io, n, Q): 
    SI = 10 * math.log10((1 / io) * (Q ** n)) 
    return SI 
 
def find_optimal_parameters(R_SI, io, N): 
    for n in [4, 3]: 
        Q = calculate_frequency_reuse_factor(N) 
        SI = calculate_SIR(io, n, Q) 
        print(f"For n = {n}:") 
        print(f"Frequency reuse factor (Q): {Q}") 
        print(f"Signal to interference ratio (SI): {SI} dB") 
        print(f"Cluster = {N}:") 
 
        if SI < R_SI: 
            # Adjusting parameters 
            i = 2 
            j = 2 
            N = i ** 2 + i * j + j ** 2 
            Q = calculate_frequency_reuse_factor(N) 
            SI = calculate_SIR(io, n, Q) 
            print("Adjusting parameters:") 
            print(f"New Frequency reuse factor (Q): {Q}") 
            print(f"New Signal to interference ratio (SI): {SI} dB") 
            print(f"Cluster = {N}:") 
        print() 
R_SI = 15  # Required signal to interference ratio (dB) 
io = 6  # Path loss exponent 
 
# Finding optimal parameters 
find_optimal_parameters(R_SI, io, 7)