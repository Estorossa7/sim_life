
#   atoms
set_seed = 0                            # random seed
height = 420
width = 420                          

fps = 60
max_sec = 10                            #   no of sec sim runs for
ball_height = 5
ball_width = 5
turn_fraction = 0.618033

scale = 200
ball_color = (153,0,0)

population = 400
mutation_rate = 0.3
targets = [(128, 0, 128), (0,64,255), (185,215,237), (13, 148, 148)]

save_genes = 'F:\\sim_life\\saved_genes\\'
save_screen = 'F:\\sim_life\\saved_screen\\'

#   molecules
max_duration = fps * max_sec                #      max no of frames the sim can run for
offset = height/2

#   possible variable
total_connection = 10

