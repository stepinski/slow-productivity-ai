Hi Piotr, Mike,

Here is a summary on the meeting we had with EACOM regarding QA/QC.  Please look at the recording(recording is in the AECOM QA/QC files section in TEAMs) as we went over the March reports and they provide explaination for each wrong flag and missing flag.

Peter thinks it's a commercially viable product if you can make it works and it there's a lot of people that would be interested in this product. York region wants the product as auto QA/QC could do 80% of the heavy lifting, which frees up some of their time.

They seem happy with the results, but it remains some adjustment to be done to have a successful product.

-   First one is, Qa/Qc must understand open channel flow and just basic hydraulics.  For instance, if level goes up , velocity goes up than we know that the flow is going up..   It’s mean that should not flag data if there are correlation between velocity and level. Another point to improve could be also to look at redundant level sensors to improve anomalies detection.  Could we add a correlation rules between channels to improve the algorythm?
-   When they tried to override auto QAQC and it didn't work because the face function is not working. 
-   We also need to determine what’s constitutes a rain event.  Peter says that a rain event should be at least 10 millimeters or more in the region’s eyes it’s 15 millimeters or more to starts a rain event.  In some cases, there are things level anomalies being removed by auto QAQC that they don't think should be as it’s not a significant rain event.
-   Data of some sites are noisy and we detect anomalies as we should not.  We need to learn from those sites.
-   QA/QC remove in some cases a whole section of the data as it detect little drops. It should removed a smaller parts of the drop area.

Thanks

**David Fromont**


[[summary requirements 0.4]]

- ### glued anomalies
QA/QC remove in some cases a whole section of the data as it detect little drops. It should removed a smaller parts of the drop area.

### [further investigation ]Data of some sites are noisy and we detect anomalies as we should not.  We need to learn from those sites.
