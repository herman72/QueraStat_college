import zlib
import zipfile

import numpy as np
np.savez('data.npz',unusual_game=unusual_game,season_prob=season_prob,a=a,b=b,c=c,p_a=p_a,p_b=p_b,p_c=p_c,p_d=p_d,p_e=p_e,p_f=p_f,pAB=pAB,pB_1=pB_1,check_law_total=check_law_total,check_bayes=check_bayes,bayes=bayes, allow_pickle=True)

def compress(file_names):
    print("File Paths:")
    print(file_names)

    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    with zipfile.ZipFile("result.zip", mode="w") as zf:
	    for file_name in file_names:
	        # Add file to the zip file
	        # first parameter file to zip, second filename in zip
	        zf.write('./'+file_name, file_name, compress_type=compression)


file_names= ["data.npz", "solution.ipynb"]
compress(file_names)
