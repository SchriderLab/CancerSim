import pandas as pd
import os
params = os.listdir('./sim_results')
for param in params:
    val_dfs = []
    val_files = os.listdir(os.path.join('./sim_results/',param))
    for val_file in val_files:
        val_file_path = os.path.join('./sim_results/', param)
        val_file_path = os.path.join(val_file_path, val_file)
        val = val_file[:-4]
        val_df = pd.read_csv(val_file_path)
        val_df['value'] = [val]*len(val_df.index)
        val_dfs.append(val_df)
    param_df = pd.concat(val_dfs)
    save_path = os.path.join('./sim_results/', param + '.csv')
    param_df.to_csv(save_path, index=False)


