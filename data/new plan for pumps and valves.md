
backsplashing
angles how valves are placed
phenomena causes vibrations - damage 
if your just focus on that area youll find amazing amount of data that will help
that is the most troubeling area

measure level of vibration - backsplashing issues -> predictive maintenance done so the valve is not damaged

= talk with Mike on pump - additional stuff we can do with the model - how we can describe what we have and so on


= greg - 
date - entire team provan - september 20


----------------------------
We a good dataset for both Valves and Pump - 
 # Condition Monitoring of Hydraulic Systems 
 https://www.kaggle.com/datasets/jjacostupa/condition-monitoring-of-hydraulic-systems
 
 https://www.kaggle.com/datasets/mayank1897/condition-monitoring-of-hydraulic-systems
 
 https://www.kaggle.com/code/mayank1897/predictive-maintenance-of-hydraulic-system/input


We have vibration data for Valves (related to Frank's comments)


number of models here:
https://www.kaggle.com/code/mayank1897/predictive-maintenance-of-hydraulic-system

public dataset:
https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems
description:
The data set was experimentally obtained with a hydraulic test rig. This test rig consists of a primary working and a secondary cooling-filtration circuit which are connected via the oil tank [1], [2]. The system cyclically repeats constant load cycles (duration 60 seconds) and measures process values such as pressures, volume flows and temperatures while the condition of four hydraulic components (cooler, valve, pump and accumulator) is quantitatively varied. Attribute Information: The data set contains raw process sensor data (i.e. without feature extraction) which are structured as matrices (tab-delimited) with the rows representing the cycles and the columns the data points within a cycle. The sensors involved are: Sensor Physical quantity Unit Sampling rate PS1 Pressure bar 100 Hz PS2 Pressure bar 100 Hz PS3 Pressure bar 100 Hz PS4 Pressure bar 100 Hz PS5 Pressure bar 100 Hz PS6 Pressure bar 100 Hz EPS1 Motor power W 100 Hz FS1 Volume flow l/min 10 Hz FS2 Volume flow l/min 10 Hz TS1 Temperature Â°C 1 Hz TS2 Temperature Â°C 1 Hz TS3 Temperature Â°C 1 Hz TS4 Temperature Â°C 1 Hz VS1 Vibration mm/s 1 Hz CE Cooling efficiency (virtual) % 1 Hz CP Cooling power (virtual) kW 1 Hz SE Efficiency factor % 1 Hz The target condition values are cycle-wise annotated in â€˜profile.txtâ€˜ (tab-delimited). As before, the row number represents the cycle number. The columns are 1: Cooler condition / %: 3: close to total failure 20: reduced effifiency 100: full efficiency 2: Valve condition / %: 100: optimal switching behavior 90: small lag 80: severe lag 73: close to total failure 3: Internal pump leakage: 0: no leakage 1: weak leakage 2: severe leakage 4: Hydraulic accumulator / bar: 130: optimal pressure 115: slightly reduced pressure 100: severely reduced pressure 90: close to total failure 5: stable flag: 0: conditions were stable 1: static conditions might not have been reached yet



description!!!!
https://www.kaggle.com/datasets/mayank1897/condition-monitoring-of-hydraulic-systems?select=documentation.txt

-- Cooler and Valve states are "easy" targets (perfect classification achieved), Pump and especially Accumulator states are more complex targets