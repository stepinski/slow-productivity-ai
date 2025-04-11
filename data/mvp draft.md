mvp draft

-   Problem Drilldown: (Understand pain, what is root cause)​
    
-   How to replace Face with Tesler (minimizing number of calculated channels, reduce  latency & get more time efficiency)​
    
-    Removing zeros with tesler (adding Python functions to easily transform data in fewer steps – broad scripting capabilities and functions and functions that Python offers in manipulating data)


mvp steps
- identify transformations that we want to move to Tesler
	- tesler : template -> bundle ( 100s of sites with the same set of FACE functions)
	- define Tesler template and bundle with inputs / outputs
- transform FACE formulas to Python code in Teseler
- shedule Tesler job
- feedback meeting with the client


estimate:
- 1 sprint discovery design
	- understanding FACE routine
- 1 sprint implementation testing
	- implement in Python and run in Tesler

review in 2 weeks

* in phase 2 :
	* evaluation with DSL  (instead of Python script we can propose FlowScript in Tesler)

optional phase 2 ( it might be an option for phase 1):
instead of Python script we can propose FlowScript in Tesler

* with  [https://langium.org/](https://langium.org/ "https://langium.org/")
- does it make more sense to show to the client only flowworks version of the routine?




