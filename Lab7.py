import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class AltitudeTemperatureRelationship:
    def __init__(self, csv_path):
        # read in data and save it
        self.data = pd.read_csv(csv_path)
        # get 'Temperature_K' from 'Temperature (C)'
        self.data["Temperature (K)"] = self.data["Temperature (C)"] + 273.15

    @staticmethod
    def fit_function(h, r, T0):
        # Equation for the line T = -rh + T0
        return -r * h + T0

    def fit_data(self):
        df = self.data
        df_drop_na = df.dropna()
        print(df_drop_na)
        # Fit the data to the line using curve_fit
        result = curve_fit(self.fit_function, df_drop_na["Altitude (km)"], df_drop_na["Temperature (K)"], full_output = True)
        # Extract parameters and their errors
        r = result[0][0]
        r_error = result[1][0][0]**(1/2)
        T0 = result[0][1]
        T0_error = result[1][1][1]**(1/2)
        return r, r_error, T0, T0_error

    def plot_data_and_fit(self):
        df = self.data
        df_drop_na = df.dropna()
        fit_data = self.fit_data()
        # Get parameters from the fit
        parameters = [fit_data[0], fit_data[2]]
        plt.scatter(df_drop_na["Altitude (km)"], df_drop_na["Temperature (K)"], label = "Data")
        # Plot the fit line
        plt.plot(df_drop_na["Altitude (km)"], self.fit_function(df_drop_na["Altitude (km)"], *parameters), color = "r", label = "T = -6.492h + 288.16")
        plt.legend()
        plt.show()
        return

altitude_temp_relationship = AltitudeTemperatureRelationship('atm_data.csv')
r, r_error, T0, T0_error = altitude_temp_relationship.fit_data()
altitude_temp_relationship.plot_data_and_fit()