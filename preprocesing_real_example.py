import numpy as np
np.set_printoptions(suppress= True, linewidth=100,precision=2)

#Importing the data
raw_data_np = np.genfromtxt(r"C:\Users\Danie\Desktop\real example for numpy\A-Real-Example-of-Loan-Data-Preprocessing-with-Numpy\loan-data.csv",
                            delimiter=';',
                            skip_header=1,
                            autostrip=True)

#checking for incomplete data
#print(np.isnan(raw_data_np).sum())

temporary_fill = np.nanmax(raw_data_np) + 1
temporary_mean = np.nanmean(raw_data_np, axis=0)
temporary_statistics = np.array([np.nanmin(raw_data_np,axis=0),
                                 temporary_mean,
                                 np.nanmax(raw_data_np,axis=0)])

#splitting the dataset
##splitting the columns
columns_string = np.argwhere(np.isnan(temporary_mean)).squeeze()
columns_numeric = np.argwhere(np.isnan(temporary_mean)  == False).squeeze()

#Ri-importing the dataset
loan_data_string = np.genfromtxt(r"C:\Users\Danie\Desktop\real example for numpy\A-Real-Example-of-Loan-Data-Preprocessing-with-Numpy\loan-data.csv",
                                 delimiter=';',
                                 skip_header=1,
                                 autostrip = True,
                                 usecols=columns_string,
                                 dtype = str)

loan_data_numeric = np.genfromtxt(r"C:\Users\Danie\Desktop\real example for numpy\A-Real-Example-of-Loan-Data-Preprocessing-with-Numpy\loan-data.csv",
                                 delimiter=';',
                                 skip_header=1,
                                 autostrip = True,
                                 usecols = columns_numeric,
                                 filling_values= temporary_fill)

#The name of the columns
header_full = np.genfromtxt(r"C:\Users\Danie\Desktop\real example for numpy\A-Real-Example-of-Loan-Data-Preprocessing-with-Numpy\loan-data.csv",
                            delimiter=';',
                            skip_footer=raw_data_np.shape[0],
                            autostrip=True,
                            dtype=str)
header_string, header_numeric = header_full[columns_string], header_full[columns_numeric]

#Creating Checkpoints:
def checkpoint(file_name,
               checkpoint_header,
               checkpoint_data):
    np.savez(file_name,header = checkpoint_header,
             data = checkpoint_data)
    checkpoint_variable = np.load(file_name + ".npz")
    return(checkpoint_variable)
checkpoint_test = checkpoint("checkpoint-test",
                             header_string , 
                             loan_data_string)

#manipulating string columns
header_string[0] = "issue_date"
loan_data_string[:,0] = np.char.strip(loan_data_string[:,0],"-15")
months = np.array(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov',
                   'Dec'])
for i in range(13):
    loan_data_string[:,0] = np.where(loan_data_string[:,0] == months[i],
                                     i,
                                     loan_data_string[:,0])

#Loan Status
status_bad = np.array(['Charged Off',
                      'Default',
                      'Late (31-120 days)'])

loan_data_string[:,1] = np.where(np.isin(loan_data_string[:,1] , status_bad), 
                                 0,
                                 1)































































































