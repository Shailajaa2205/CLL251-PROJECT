# with HRV.
import matplotlib.pyplot as plt

# Constants
Cp = 1.005  # specific heat capacity of air in kJ/kg*K
rho = 1.2   # air density in kg/m³
V = 200     # house volume in m³
eta_HRV = 0.5  # efficiency of Heat Recovery Ventilator
eta_ac = 0.7  # efficiency of air conditioner
eta_furnace = 0.7  # efficiency of furnace

# Summer temperature equations
def summer_temp(hour):
    if 0 <= hour < 6:
        return -1.07 * hour + 33.42
    elif 6 <= hour < 16:
        return 1.36 * hour + 18.82
    elif
        16 < hour < 24:
        return -1.07 * hour + 59.14

# Winter temperature equations
def winter_temp(hour):
    if 0 <= hour < 6:
        return -0.9375 * hour + 10.625
    elif 6 <= hour < 14:
        return 1.875 * hour - 6.25
    elif 14 <= hour < 24:
        return -0.9375 * hour + 33.125

# Calculate mass of air in the house
mass = rho * V  # kg

# Initialize lists to store hourly energy consumption
summer_energy = []
winter_energy = []

# Simulate energy consumption for each hour
for hour in range(24):
    # Summer simulation
    outdoor_temp_summer = summer_temp(hour)
    precooled_temp = eta_HRV* (21 - outdoor_temp_summer) + outdoor_temp_summer
    delta_T_summer = precooled_temp - 21  # temperature difference for cooling

    Q_summer = mass * Cp * delta_T_summer  # heat energy for cooling in kJ
    E_summer = Q_summer / eta_ac  # actual energy consumption of air conditioner in kJ
    summer_energy.append(E_summer / 3600)  # convert kJ to kWh and add to list

    # Winter simulation
    outdoor_temp_winter = winter_temp(hour)
    preheated_temp = outdoor_temp_winter + eta_HRV * (26 - outdoor_temp_winter)
    delta_T_winter = 26 - preheated_temp  # temperature difference for heating

    Q_winter = mass * Cp * delta_T_winter   # heat energy for heating in kJ
    E_winter = Q_winter / eta_furnace   # actual energy consumption of furnace in kJ
    winter_energy.append(E_winter / 3600)  # convert kJ to kWh and add to list

# Plot hourly energy consumption
hours = list(range(24))

plt.plot(hours, summer_energy, label='Summer')
plt.plot(hours, winter_energy, label='Winter')
plt.xlabel('Hour')
plt.ylabel('Energy Consumption by (air-conditioner/furnace) (kWh)')
plt.title('Hourly Energy Consumption in a day with HRV')
plt.legend()
plt.grid(True)
plt.show()

