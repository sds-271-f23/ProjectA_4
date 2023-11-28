# SDS271-Lab7 Project A Fit a curve and plot
The class is designed to analyze the relationship between altitude and temperature based on input data provided in a CSV file. The class utilizes the pandas library for data manipulation and the scipy.optimize.curve_fit function for curve fitting.

# Initialization

#Provide the path to the CSV file containing altitude and temperature data

csv_path = 'path/to/your/data.csv'

#Create an instance of the AltitudeTemperatureRelationship class

altitude_temp_relationship = AltitudeTemperatureRelationship(csv_path)

# Fit Data:

To fit the data to the specified line equation T = -rh + T0, use the fit_data method.

r, r_error, T0, T0_error = altitude_temp_relationship.fit_data()


# Plot Data and Fit:

To visualize the data and the fitted line, use the plot_data_and_fit method

altitude_temp_relationship.plot_data_and_fit()



