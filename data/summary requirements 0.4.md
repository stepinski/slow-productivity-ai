## summary requirements 0.4:
- ### hydraulics
First one is, Qa/Qc must understand open channel flow and just basic hydraulics.  For instance, if level goes up , velocity goes up than we know that the flow is going up..   It’s mean that should not flag data if there are correlation between velocity and level. Another point to improve could be also to look at redundant level sensors to improve anomalies detection.  Could we add a correlation rules between channels to improve the algorythm?
 
- ### rain event
We also need to determine what’s constitutes a rain event.  Peter says that a rain event should be at least 10 millimeters or more in the region’s eyes it’s 15 millimeters or more to starts a rain event.  In some cases, there are things level anomalies being removed by auto QAQC that they don't think should be as it’s not a significant rain event.