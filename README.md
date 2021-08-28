# Tracardi plugin

This code can be run within Tracardi workflow.

# Is in time span action

The purpose of this plugin is to check if the local time is within 
defined time span.

This action minds the time zone to the event. Therefore, you must provide 
time zone. By default, time zone is included in browser event context. 


# Configuration

This node requires configuration. In order to read timezone 
you must define path to time zone. Use dot notation to do that.

Moreover, you need to set start and end of the time span. The time slots 
have no default values. 

Example of the configuration:
```json
{
  "start": "12:00:00",
  "end": "14:00:00"
}
```

# Input payload

This node does not process input payload.

# Output

[comment]: <> (This node has two output nodes.)

[comment]: <> (The first one &#40;IS IN TIME SPAN&#41; is active when event happened at given time span. )

[comment]: <> (Otherwise, the another node &#40;IS NOT IN TIME SPAN&#41; is active. )
 
