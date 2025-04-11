there are 3 main types of anomalies:
- point anomalies ( in time series setup - industrial IoT those are spikes and nans)
- contextual anomalies - in our setup those are extreme events that are correlated with features like during holiday people are using water infrustructure more than when they're in the office during workday. or extreme flooding events when snow is melting and temperature is at certain level in the same time + after  heavy rain. ( in other ocassions heavy rain doesn't result in flooding)
- collective anomaly - anomalies are grouped together - in our case its sensor drifting - related to battery malfunctioning or connectivity issues - > we have a continous anomalous signal in time

