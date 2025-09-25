import os

import pandas as pd



files_folder = "files"



output_file = "res/RenameRentals 03-13-2025.xlsx"



start_number = 345  

agencyname = "stoughton"



filenames = os.listdir(files_folder)

df = pd.DataFrame({"Original": filenames})

df["RenamedAs"] = ""  

df["ScanDocName"] = ""  



if os.path.exists(output_file):

    existing_df = pd.read_excel(output_file)

    for column in df.columns:

        if column not in existing_df.columns:

            existing_df[column] = ""

    combined_df = pd.concat([existing_df, df], ignore_index=True)

else:

    combined_df = df

for index, row in combined_df.iterrows():

    if not row["RenamedAs"]:  

        original_filename = row["Original"]

        unique_id = original_filename.split("_")[-1].split(".")[0]  

        # reset this

        new_filename = f"scan_{start_number}_amazon_{agencyname}_rental_tolls_03-12-2025(bot)_{unique_id}{os.path.splitext(row['Original'])[1]}"

        scan_doc_name = f"scan_{start_number}_amazon_{agencyname}_rental_tolls_03-12-2025(bot){os.path.splitext(row['Original'])[1]}"

        old_file_path = os.path.join(files_folder, row["Original"])

        new_file_path = os.path.join(files_folder, new_filename)

        os.rename(old_file_path, new_file_path)

        combined_df.at[index, "RenamedAs"] = new_filename

        combined_df.at[index, "ScanDocName"] = scan_doc_name
   

        start_number += 1


combined_df.to_excel(output_file, index=False)


print(f"Filenames saved to {output_file}")