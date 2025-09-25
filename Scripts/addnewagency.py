import os
from pprint import pprint
from tkinter import Y
import pandas as pd
import re
import os
import pdfplumber
import datetime
import getpass
def bowmandeldotprocess():
        output_list = []
        df = pd.DataFrame()
        rowDict = {"TOLL AGENCY":"","LP":"","LP STATE":"","TRXN.DATE & TIME":"","EXIT LANE/LOCATION":"","ACCOUNT#":"", "REFERENCE # OR INVOICE #":"","VIOLATION#":"","AMOUNT DUE":"","DUE DATE":"","PIN NO#":"","INVOICE#":"" }
        workingDir = f"Downloaded_Scans\\"
        outputDir = f"SRTS_OUTPUT\\"
        for i in os.listdir(workingDir):
            df = pd.DataFrame()
            with pdfplumber.open(workingDir+i) as pdf:
                for page in pdf.pages:
                    pageText = page.extract_text()
                    print(pageText)
                   
                        
                        
                        
            #         output_list.append(rowDict)
            #         dff = pd.DataFrame(output_list)
            #         output_list = []
            #         df = pd.concat([df, dff])
            #         df.drop_duplicates(inplace = True)
                    
                    
            # print("writing out"+i)
            # df.to_excel(str(outputDir+i).replace(".pdf","")+".xlsx", index=False)
            
            
bowmandeldotprocess()

# import logging

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG

# # Create a logger
# logger = logging.getLogger(__name__)

# def main():
#     # Your script logic here
#     logger.debug('This is a debug message')
#     logger.info('This is an info message')
#     logger.warning('This is a warning message')
#     logger.error('This is an error message')
#     logger.critical('This is a critical message')

# if __name__ == "__main__":
#     main()
