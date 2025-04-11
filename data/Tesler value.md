Tesler thoughts

- non bigdata: It's a major advantage of Tesler -> you can write your code directly in Python without any databricks specific libraries / technology.
using CSV - comon interface
you don't process massive amount of data 

- tesler RT is it's major advantage - continously producing transformed TS > stream processing that is not cloud native. with scalable servless architecture ( like nucleo or KFservice) we can offer very advanced tool here

- maybe you'd like to use Tesler as it is to run only predict() for particular channel [[spark fit predict scenario]]

- it automates timeseries processing - FACE was an engine to run simple functions on time series - we'd like to have something that is capable to run more complicated functions on timeseries data

- thanks to Tesler we can for any scenario involving number timeseries data automate running of custom processing in Python or other language

- in the future we may use Kubeflow to scale fitting or to include pipelines in Tesler

- Tesler main advantage is that you can shedule models like raven or Swmm - engeneering specific models that you run for number of parameters

- to think: Ring app to deploy as cloud native app ( Azure / AWS / GC) that runs Tesler with specific storage and internal or external kafka

- to think: Tesler migh be a chart in k8s 

- to think: Hilo scenario app or Script where we use known tools and run 1click deployment [[hilo-auto script]]
- 

