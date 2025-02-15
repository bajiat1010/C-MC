# Input cluster sizes as a list, e.g., [4, 7, 12] 
cluster_sizes = list(map(int, input("Enter Cluster Sizes with [ ] around Them: ").strip("[]").split())) 
# Parameters 
bw = 33000         # Total Bandwidth in kHz 
sim_ch_bw = 25         # Simplex channel bandwidth in kHz 
dup_ch_bw = 2 * sim_ch_bw         # Duplex channel bandwidth in kHz 
t_ch = bw / dup_ch_bw          # Total available channels 
cc_bw = 1000            # Control channel bandwidth 
t_cc = cc_bw / dup_ch_bw          # Number of available control channels 
# Calculating results for each cluster size 
for N in cluster_sizes: 
    # Calculate the desired results for each system use 
    ch_per_cell = round(t_ch / N)         # Channels available per cell 
    vc = round((t_ch - t_cc) / N)        # Voice channels 
    cc = ch_per_cell - vc              # Control channels 
     
    # Print the results 
    print(f"For Cluster size N = {N}") 
    print("-------------------------") 
    print(f"Total number of channels available per cell: {ch_per_cell} channels") 
    print(f"Voice Channel: {vc} channels") 
    print(f"Control Channel: {cc} channels\n") 