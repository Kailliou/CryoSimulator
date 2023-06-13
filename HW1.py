import starfile
import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation

df = starfile.read("cryoem_heterogeneity_challenge_2023_second_dataset.star")
optics = df['optics']
particles = df['particles']
# clever math goes here
Rot = Rotation.random(33672).as_euler('zxy', degrees=True)
Rand = np.random.normal(10000,2000,33672)
for i in range(33672):
    particles.loc[i,'rlnAngleRot'] = Rot[i][0]
    particles.loc[i,'rlnAngleTilt'] = Rot[i][1]
    particles.loc[i,'rlnAnglePsi'] = Rot[i][2]
    particles.loc[i,'rlnDefocusU'] = Rand[i]
    particles.loc[i,'rlnDefocusV'] = Rand[i]
print(particles)
print(df)
starfile.write(particles, "cars.star", overwrite=True)

