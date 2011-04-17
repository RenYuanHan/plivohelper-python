#!/usr/bin/env python
import resthelpers


#URL of the Rest Telefonie service
REST_API_URL = 'http://127.0.0.1:8088'

# Sid and AuthToken
SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

#Define Channel Variable - http://wiki.freeswitch.org/wiki/Channel_Variables
originate_dial_string = "bridge_early_media=true,hangup_after_bridge=true"

# Create a REST object
rest = helpers.REST(REST_API_URL, SID, AUTH_TOKEN)

# Initiate a new outbound call to user/1000 using a HTTP POST
# All parameters for bulk calls shall be separated by a delimeter
call_params = {
    'Delimeter' : '>', # Delimter for the bulk list
    'From': '919191919191', # Caller Id
    'To' : '1000>1000>1000>1000', # User Numbers to Call separated by delimeter
    'Gateways' : "user/>user/>user/>user/", # Gateway string for each number separated by delimeter
    'GatewayCodecs' : "'PCMA,PCMU'>'PCMA,PCMU'>'PCMA,PCMU'>'PCMA,PCMU'", # Codec string as needed by FS for each gateway separated by delimeter
    'GatewayTimeouts' : "60>30>30>30", # Seconds to timeout in string for each gateway separated by delimeter
    'GatewayRetries' : "2>1>1>1", # Retry String for Gateways separated by delimeter, on how many times each gateway should be retried
    'OriginateDialString' : originate_dial_string,
    'AnswerUrl' : "http://127.0.0.1:8082/answered/",
    'HangUpUrl' : "http://127.0.0.1:8082/hangup/",
    'RingUrl' : "http://127.0.0.1:8082/ringing/"
}

try:
    print rest.bulk_call(call_params)
except Exception, e:
    print e
    print e.read()