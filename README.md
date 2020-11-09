# Temperature Alert
## Descriptions
Console application to alert for temperature values from console input. On start
up, user inputs freezing threshold, boiling threshold and fluctuation value.
Alerts are generated if temperature lower than or equal to freezing threshold or
higher or equal to boiling threshold. To clear alert status, temperature should
be in range (freezing threshold + fluctuation value, boiling threshold -
fluctuation value). Input `exit` to exit the application.

## How to run:
Please make sure you are using python >= 2.7.16
`$ python temperature_alert.py`

## Test Run Examples:
```
$ python temperature_alert.py
Please input number for freezing threshold:
0
Please input number for boiling threshold:
100
Please input number for fluctuation value:
0.5
Please input number(s) for alerting, input `exit` to exit app.
4 1 0.5 0 -0.5 0 0.5 0 -2 0 0.5 0.6 2
4.0
1.0
0.5
0.0 freezing
-0.5
0.0
0.5
0.0
-2.0
0.0
0.5
0.6 unfreezing
2.0
Please input number(s) for alerting, input `exit` to exit app.
exit
Exiting the alerting application
```

```
$ python temperature_alert.py
Please input number for freezing threshold:
0
Please input number for boiling threshold:
100
Please input number for fluctuation value:
0.5
Please input number(s) for alerting, input `exit` to exit app.
5 -0.5 0.5 -0.2 100 101
5.0
-0.5 freezing
0.5
-0.2
100.0 unfreezing boiling
101.0
Please input number(s) for alerting, input `exit` to exit app.
exit
Exiting the alerting application
```

```
$ python temperature_alert.py
Please input number for freezing threshold:
0
Please input number for boiling threshold:
100
Please input number for fluctuation value:
0.5
Please input number(s) for alerting, input `exit` to exit app.
0 0.3 0.5 0.4 0.7
0.0 freezing
0.3
0.5
0.4
0.7 unfreezing
Please input number(s) for alerting, input `exit` to exit app.
exit
Exiting the alerting application
```
