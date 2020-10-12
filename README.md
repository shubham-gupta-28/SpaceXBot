# SpacexBot Project

SpaceXBot project is a Amazon Lex chatbot project. It is developed to get information related to SpaceX Rockets, Missions & Launches. 

## Technologies

Amazon Lex : Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational interactions. 

Amazon Lambda : AWS Lambda lets you run code without provisioning or managing servers. With Lambda, you can run code for virtually any type of application or backend service - all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

Amazon Lex Web Interface : It is an open source project. It provides a chatbot UI component that can be integrated in your website. The interface allows a user to interact with a Lex bot directly from a browser using text or voice. UI Component is created using VueJS framework.

Amazon S3 : Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9's) of durability, and stores data for millions of applications for companies all around the world.

Amazon Cognito : Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0. 

Python : Programming language used to create chatbot backend.

SpaceX REST API : To get data related to SpaceX Launches, Rockets & Missions.

## Amazon Lex Bot Model

```json

{
  "metadata": {
    "schemaVersion": "1.0",
    "importType": "LEX",
    "importFormat": "JSON"
  },
  "resource": {
    "name": "SpaceXBot",
    "version": "1",
    "intents": [
      {
        "rejectionStatement": {
          "messages": [
            {
              "contentType": "PlainText",
              "content": "Okay. Mission details will not be fetched from SpaceX."
            }
          ]
        },
        "name": "Missions",
        "version": "3",
        "fulfillmentActivity": {
          "codeHook": {
            "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
            "messageVersion": "1.0"
          },
          "type": "CodeHook"
        },
        "sampleUtterances": [
          "I would like to know about SpaceX Missions",
          "Tell me about SpaceX Missions",
          "Tell me about Missions",
          "I would like to know about Missions",
          "I need information about SpaceX Missions",
          "I need information about Missions",
          "I need information about {Mission} mission",
          "Tell me about {Mission} mission",
          "I would like to know about {Mission} mission"
        ],
        "slots": [
          {
            "sampleUtterances": [],
            "slotType": "Mission",
            "slotTypeVersion": "1",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "Which mission details you want?"
                }
              ],
              "maxAttempts": 2
            },
            "priority": 1,
            "name": "Mission"
          }
        ],
        "confirmationPrompt": {
          "messages": [
            {
              "contentType": "PlainText",
              "content": "Are you sure, you want details for [lastSelectedMissionName]?"
            }
          ],
          "maxAttempts": 3
        },
        "dialogCodeHook": {
          "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
          "messageVersion": "1.0"
        }
      },
      {
        "rejectionStatement": {
          "messages": [
            {
              "contentType": "PlainText",
              "content": "Okay. Rocket details will not be fetched from SpaceX."
            }
          ]
        },
        "name": "Rockets",
        "version": "6",
        "fulfillmentActivity": {
          "codeHook": {
            "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
            "messageVersion": "1.0"
          },
          "type": "CodeHook"
        },
        "sampleUtterances": [
          "I would like to know about SpaceX rockets",
          "I would like to know about rockets",
          "Tell me about SpaceX rockets",
          "Tell me about rockets",
          "I need information about rockets",
          "I need information about SpaceX rockets",
          "Tell me about {Rocket} rocket",
          "I need information about {Rocket} rocket",
          "I would like to know about {Rocket} rocket"
        ],
        "slots": [
          {
            "sampleUtterances": [],
            "slotType": "Rocket",
            "slotTypeVersion": "1",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "Which Rocket details you want ?"
                }
              ],
              "maxAttempts": 2
            },
            "priority": 1,
            "name": "Rocket"
          }
        ],
        "confirmationPrompt": {
          "messages": [
            {
              "contentType": "PlainText",
              "content": "Are you sure, you want details for [lastSelectedRocketName] ?"
            }
          ],
          "maxAttempts": 3
        },
        "dialogCodeHook": {
          "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
          "messageVersion": "1.0"
        }
      },
      {
        "name": "End",
        "version": "1",
        "fulfillmentActivity": {
          "codeHook": {
            "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
            "messageVersion": "1.0"
          },
          "type": "CodeHook"
        },
        "sampleUtterances": [
          "Bye",
          "Stop",
          "End"
        ],
        "slots": [],
        "dialogCodeHook": {
          "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
          "messageVersion": "1.0"
        }
      },
      {
        "name": "Welcome",
        "version": "1",
        "fulfillmentActivity": {
          "codeHook": {
            "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
            "messageVersion": "1.0"
          },
          "type": "CodeHook"
        },
        "sampleUtterances": [
          "Hi",
          "Hello",
          "Good Morning",
          "Good Afternoon",
          "Good Evening",
          "Help me"
        ],
        "slots": [],
        "dialogCodeHook": {
          "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
          "messageVersion": "1.0"
        }
      },
      {
        "rejectionStatement": {
          "messages": [
            {
              "contentType": "PlainText",
              "content": "Okay, Launch details will not be fetched from SpaceX"
            }
          ]
        },
        "name": "Launches",
        "version": "2",
        "fulfillmentActivity": {
          "codeHook": {
            "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
            "messageVersion": "1.0"
          },
          "type": "CodeHook"
        },
        "sampleUtterances": [
          "I would like to know about launches",
          "Tell me about launches",
          "Tell me about SpaceX launches",
          "I would like to know about SpaceX launches",
          "I need information about launches",
          "I need information about SpaceX launches",
          "Tell me about {Launch} launch",
          "I need information about {Launch} launch",
          "I would like to know about {Launch} launch"
        ],
        "slots": [
          {
            "sampleUtterances": [],
            "slotType": "Launch",
            "slotTypeVersion": "1",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "Which launch details you want  to check ?"
                }
              ],
              "maxAttempts": 2
            },
            "priority": 1,
            "name": "Launch"
          }
        ],
        "confirmationPrompt": {
          "messages": [
            {
              "contentType": "PlainText",
              "content": "Are you sure, you want details {Launch} launch ?"
            }
          ],
          "maxAttempts": 3
        },
        "dialogCodeHook": {
          "uri": "arn:aws:lambda:eu-west-1:283266096342:function:SpaceXBotFunction",
          "messageVersion": "1.0"
        }
      }
    ],
    "slotTypes": [
      {
        "description": "List of SpaceX Mission Slot",
        "name": "Mission",
        "version": "1",
        "enumerationValues": [
          {
            "value": "F4F83DE",
            "synonyms": []
          },
          {
            "value": "Iridium NEXT",
            "synonyms": []
          },
          {
            "value": "SES",
            "synonyms": []
          },
          {
            "value": "Telstar",
            "synonyms": []
          },
          {
            "value": "9D1B7E0",
            "synonyms": []
          },
          {
            "value": "593B499",
            "synonyms": []
          },
          {
            "value": "F3364BF",
            "synonyms": []
          },
          {
            "value": "AsiaSat",
            "synonyms": []
          },
          {
            "value": "6C42550",
            "synonyms": []
          },
          {
            "value": "Thaicom",
            "synonyms": []
          },
          {
            "value": "EE86F74",
            "synonyms": []
          },
          {
            "value": "Commercial Resupply Services",
            "synonyms": []
          }
        ],
        "valueSelectionStrategy": "ORIGINAL_VALUE"
      },
      {
        "description": "Available Rocket",
        "name": "Rocket",
        "version": "1",
        "enumerationValues": [
          {
            "value": "falconheavy",
            "synonyms": []
          },
          {
            "value": "falcon1",
            "synonyms": []
          },
          {
            "value": "falcon9",
            "synonyms": []
          },
          {
            "value": "bfr",
            "synonyms": []
          }
        ],
        "valueSelectionStrategy": "ORIGINAL_VALUE"
      },
      {
        "description": "List of Launch (Upcoming, Next, Latest)",
        "name": "Launch",
        "version": "1",
        "enumerationValues": [
          {
            "value": "Upcoming",
            "synonyms": []
          },
          {
            "value": "Next",
            "synonyms": []
          },
          {
            "value": "Latest",
            "synonyms": []
          }
        ],
        "valueSelectionStrategy": "ORIGINAL_VALUE"
      }
    ],
    "voiceId": "Salli",
    "childDirected": false,
    "locale": "en-US",
    "idleSessionTTLInSeconds": 300,
    "clarificationPrompt": {
      "messages": [
        {
          "contentType": "PlainText",
          "content": "Sorry, can you please repeat that?"
        }
      ],
      "maxAttempts": 5
    },
    "abortStatement": {
      "messages": [
        {
          "contentType": "PlainText",
          "content": "Sorry, I could not understand. Goodbye."
        }
      ]
    }
  }
}

```
## Lambda Function Code (SpaceXBotFunction.py) 

```python
import json
import logging
import botocore.vendored.requests as requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message, response_card):
    logger.debug('Elicit slot values method called')
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message,
            'responseCard': response_card
        }
    }


def close(session_attributes, fulfillment_state, message,response_card):
    logger.debug('Close method called')
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message,
            'responseCard': response_card
        }
    }

    return response


def delegate(session_attributes, slots):
    logger.debug('Delegate method called')
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


def build_response_card(title, subtitle, options):
    #Build a responseCard with a title, subtitle, set of options which should be displayed as buttons.
    buttons = None
    if options is not None:
        buttons = []
        for i in range(min(5, len(options))):
            buttons.append(options[i])

    return {
        'contentType': 'application/vnd.amazonaws.card.generic',
        'version': 1,
        'genericAttachments': [{
            'title': title,
            'subTitle': subtitle,
            'buttons': buttons
        }]
    }

def try_ex(func):
    #Call passed in function in try block. If KeyError is encountered return None.
    try:
        return func()
    except KeyError:
        return None

def build_options(slot):
    logger.debug('Build response card options method called for slot={}'.format(slot))
    if slot == 'Rocket':
        logger.debug('Building Rocket List')
        rockets = getRockets()
        options = []
        for rocket_id in rockets:
            options.append({'text': rockets[rocket_id], 'value': rocket_id })
        return options
        
    elif slot == 'Mission':
        logger.debug('Building Mission List')
        missions = getMissions()
        options = []
        for mission_id in missions:
            options.append({'text': missions[mission_id], 'value': mission_id })
        return options
    
    elif slot == 'Launch':
        logger.debug('Building Launch List')
        launches = getLaunches()
        options = []
        for launch in launches:
            options.append({'text': launch, 'value': launch })
        return options
        
    
def build_validation_result(is_valid, violated_slot, message_content):
    logger.debug('Building slot validation result. Is Valid : {}'.format(is_valid))
    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }

""" Validate Slot Values  """
def validate_slots(slots):
    logger.debug('Validate Slot Function Called')
    selectedRocket =  try_ex(lambda: slots['Rocket'])
    selectedMission =  try_ex(lambda: slots['Mission'])
    selectedLaunch =  try_ex(lambda: slots['Launch'])

    if selectedRocket:
        rockets = getRockets()
        if selectedRocket not in rockets.keys():
            logger.debug('{} is not present in Rockets {}'.format(selectedRocket,rockets.items()))
            return build_validation_result(False,
                                          'Rocket',
                                          'We do not have {} rocket in Rockets. Please select from following options.'.format(selectedRocket))
    if selectedMission:
        missions = getMissions()
        if selectedMission not in missions.keys():
            logger.debug('{} is not present in Missions {}'.format(selectedMission,missions.items()))
            return build_validation_result(False,
                                          'Mission',
                                          'We do not have {} mission in Missions. Please select from following options.'.format(selectedMission))

    if selectedLaunch:
        launches = getLaunches()
        if selectedLaunch not in launches:
            logger.debug('{} is not present in Launches {}'.format(selectedLaunch,launches))
            return build_validation_result(False,
                                          'Launch',
                                          'We do not have {} launch in Launches. Please select from following options.'.format(selectedLaunch))
    
    logger.debug('Slot Validation Successfull')
    return {'isValid': True}
    
#Get list of all rockets Method
def getRockets():
    logger.debug('Get list of all rockets method called.')
    rocketDict = {}
    try:
        #Calling SpaceX Rockets API
        logger.debug('Calling SpaceX Rockets API')
        response = requests.get('https://api.spacexdata.com/v3/rockets')
        responses = response.json()
        if responses:
            for i in responses:
                rocketDict[i['rocket_id']] = i['rocket_name']
    except Exception as e:
        logger.debug('Exception Occurred while getting rocket list : {}'.format(e))
        raise e
    logger.debug('Returning Rocket List: {}'.format(rocketDict))
    return rocketDict

#Get detail of a rocket on the basis of rocket_id
def getRocketDetails(rocket_id):
    logger.debug('Get rocket details method called.')
    try:
        #Calling SpaceX Rockets API
        logger.debug('Calling SpaceX Rockets API')
        response = requests.get('https://api.spacexdata.com/v3/rockets/'+rocket_id)
        responses = response.json()
    except Exception as e:
        logger.debug('Exception Occurred while getting rocket details : {}'.format(e))
        raise e
    logger.debug('Returning Rocket Details: {}'.format(responses))
    return responses

#Get list of all missions Method
def getMissions():
    logger.debug('Get list of all missions method called.')
    missionDict = {}
    try:
        #Calling SpaceX Missions API
        logger.debug('Calling SpaceX Missions API')
        response = requests.get('https://api.spacexdata.com/v3/missions')
        responses = response.json()
        if responses:
            for i in responses:
                missionDict[i['mission_id']] = i['mission_name']
    except Exception as e:
        logger.debug('Exception Occurred while getting mission list : {}'.format(e))
        raise e
    logger.debug('Returning Mission List: {}'.format(missionDict))
    return missionDict
    
#Get detail of a mission on the basis of mission_id
def getMissionDetails(mission_id):
    logger.debug('Get mission details method called.')
    try:
        #Calling SpaceX Rockets API
        logger.debug('Calling SpaceX Mission API')
        response = requests.get('https://api.spacexdata.com/v3/missions/'+mission_id)
        responses = response.json()
    except Exception as e:
        logger.debug('Exception Occurred while getting mission details : {}'.format(e))
        raise e
    logger.debug('Returning Mission Details: {}'.format(responses))
    return responses


def getLaunches():
    logger.debug('Get list of launches method called.')
    launches = ['Latest','Next']
    return launches

def getLaunchDetails(launch):
    logger.debug('Get launch details method called.')
    try:
        #Calling SpaceX Rockets API
        logger.debug('Calling SpaceX Launch API')
        response = requests.get('https://api.spacexdata.com/v3/launches/'+launch)
        responses = response.json()
    except Exception as e:
        logger.debug('Exception Occurred while getting launch details : {}'.format(e))
        raise e
    logger.debug('Returning Launch Details: {}'.format(responses))
    return responses
    
    
""" --- Functions that control the bot's behavior --- """


def call_rockets(intent_request):
    logger.debug('Inside call_rockets method')
    logger.debug('Reading Rocket slot value')
    selectedRocket = intent_request['currentIntent']['slots']['Rocket']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    logger.debug('Storing operation details in session attributes')
    operation = json.dumps({
        'IntentName': 'Rockets',
        'Rocket': selectedRocket,
    })
    output_session_attributes['currentOperation'] = operation
    
    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['currentIntent']['slots']
        validation_result = validate_slots(slots)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message'],
                build_response_card(
                    'Specify {}'.format(validation_result['violatedSlot']),
                    validation_result['message']['content'],
                    build_options(validation_result['violatedSlot'])
                )
            )

        if not selectedRocket:
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                intent_request['currentIntent']['slots'],
                'Rocket',
                {'contentType': 'PlainText', 'content': 'Which Rocket you want to select?'},
                build_response_card(
                    'Specify Rocket',
                    'Which Rocket you want to select?',
                    build_options('Rocket')
                )
            )
        
        if selectedRocket:
           #Get rocket name for selected rocket
           rocketName = getRockets()[selectedRocket]
           logger.debug('Rocket Name is : {}'.format(rocketName))
           output_session_attributes['lastSelectedRocketName'] = rocketName
           output_session_attributes['lastSelectedRocket'] = selectedRocket
        else:
           try_ex(lambda: output_session_attributes.pop('lastSelectedRocketName'))
           try_ex(lambda: output_session_attributes.pop('lastSelectedRocket'))
        
        output_session_attributes['currentOperation'] = operation
        return delegate(output_session_attributes, slots)

    # Call Get Rocket detail function
    rocketData = getRocketDetails(try_ex(lambda: output_session_attributes['lastSelectedRocket']))
    rocketLinks = []
    if rocketData['flickr_images']:
        for image in rocketData['flickr_images']:
            rocketLinks.append({
                'title': '{} Images'.format(rocketData['rocket_name']),
                'attachmentLinkUrl': rocketData['wikipedia'],
                'imageUrl': image 
            })
    else:
        rocketLinks.append({
            'title': '{} Images not available.'.format(rocketData['rocket_name']),
            'attachmentLinkUrl': rocketData['wikipedia'],
        })   
        
    try_ex(lambda: output_session_attributes.pop('lastSelectedRocketName'))
    try_ex(lambda: output_session_attributes.pop('lastSelectedRocket'))
    try_ex(lambda: output_session_attributes.pop('currentOperation'))
    output_session_attributes['lastConfirmedOperation'] = operation

    return close(
        output_session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': 'Description: {} , Company: {} , Success Rate: {}% , First Flight: {} , Cost Per Launch: USD {}'.format(rocketData['description'],rocketData['company'],rocketData['success_rate_pct'],rocketData['first_flight'], rocketData['cost_per_launch'])
        },
        {
            'version': '1',
            'contentType': 'application/vnd.amazonaws.card.generic',
            'genericAttachments': rocketLinks 
        }
    )

def call_missions(intent_request):
    logger.debug('Inside call_missions method')
    logger.debug('Reading Mission slot value')
    selectedMission = intent_request['currentIntent']['slots']['Mission']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    logger.debug('Storing operation details in session attributes')
    operation = json.dumps({
        'IntentName': 'Missions',
        'Rocket': selectedMission,
    })
    output_session_attributes['currentOperation'] = operation
    
    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['currentIntent']['slots']
        validation_result = validate_slots(slots)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message'],
                build_response_card(
                    'Specify {}'.format(validation_result['violatedSlot']),
                    validation_result['message']['content'],
                    build_options(validation_result['violatedSlot'])
                )
            )

        if not selectedMission:
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                intent_request['currentIntent']['slots'],
                'Mission',
                {'contentType': 'PlainText', 'content': 'Which Mission you want to select?'},
                build_response_card(
                    'Specify Mission',
                    'Which Mission you want to select?',
                    build_options('Mission')
                )
            )
        
        if selectedMission:
           #Get mission name for selected rocket
           missionName = getMissions()[selectedMission]
           logger.debug('Mission Name is : {}'.format(missionName))
           output_session_attributes['lastSelectedMissionName'] = missionName
           output_session_attributes['lastSelectedMission'] = selectedMission
        else:
           try_ex(lambda: output_session_attributes.pop('lastSelectedMissionName'))
           try_ex(lambda: output_session_attributes.pop('lastSelectedMission'))
        
        output_session_attributes['currentOperation'] = operation
        return delegate(output_session_attributes, slots)

    # Call Get Mission detail function
    missionData = getMissionDetails(try_ex(lambda: output_session_attributes['lastSelectedMission']))
    
    try_ex(lambda: output_session_attributes.pop('lastSelectedMissionName'))
    try_ex(lambda: output_session_attributes.pop('lastSelectedMission'))
    try_ex(lambda: output_session_attributes.pop('currentOperation'))
    output_session_attributes['lastConfirmedOperation'] = operation

    return close(
        output_session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': 'Description: {}'.format(missionData['description'])
        },
        {
            'version': '1',
            'contentType': 'application/vnd.amazonaws.card.generic',
            'genericAttachments': [
                {
                'title': '{}'.format(missionData['mission_name']),
                'attachmentLinkUrl' : missionData['wikipedia']
                }
            ]
        }
    )

def call_launches(intent_request):
    logger.debug('Inside call_launches method')
    logger.debug('Reading Launch slot value')
    selectedLaunch = intent_request['currentIntent']['slots']['Launch']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    logger.debug('Storing operation details in session attributes')
    operation = json.dumps({
        'IntentName': 'Launches',
        'Launch': selectedLaunch,
    })
    output_session_attributes['currentOperation'] = operation
    
    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['currentIntent']['slots']
        validation_result = validate_slots(slots)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                slots,
                validation_result['violatedSlot'],
                validation_result['message'],
                build_response_card(
                    'Specify {}'.format(validation_result['violatedSlot']),
                    validation_result['message']['content'],
                    build_options(validation_result['violatedSlot'])
                )
            )

        if not selectedLaunch:
            return elicit_slot(
                output_session_attributes,
                intent_request['currentIntent']['name'],
                intent_request['currentIntent']['slots'],
                'Launch',
                {'contentType': 'PlainText', 'content': 'Which Launch you want to select?'},
                build_response_card(
                    'Specify Launch',
                    'Which Launch you want to select?',
                    build_options('Launch')
                )
            )
        
        if selectedLaunch:
           output_session_attributes['lastSelectedLaunch'] = selectedLaunch
        else:
           try_ex(lambda: output_session_attributes.pop('lastSelectedLaunch'))
        
        output_session_attributes['currentOperation'] = operation
        return delegate(output_session_attributes, slots)

    # Call Get Launch detail function
    launchData = getLaunchDetails(try_ex(lambda: output_session_attributes['lastSelectedLaunch']))
    launchLinks = []
    if launchData['links']['flickr_images']:
        for image in launchData['links']['flickr_images']:
            launchLinks.append({
                'title': '{} Images'.format(launchData['rocket']['rocket_name']),
                'attachmentLinkUrl': launchData['links']['wikipedia'],
                'imageUrl': image 
            })
    else:
        launchLinks.append({
            'title': 'Images not Available',
            'attachmentLinkUrl': launchData['links']['wikipedia'],
        })

    try_ex(lambda: output_session_attributes.pop('lastSelectedLaunch'))
    try_ex(lambda: output_session_attributes.pop('currentOperation'))
    output_session_attributes['lastConfirmedOperation'] = operation

    return close(
        output_session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': 'Flight Number: {} , Mission Name: {} , Rocket Name: {} , Launch Date(UTC): {} , Details: {}'.format(launchData['flight_number'],launchData['mission_name'],launchData['rocket']['rocket_name'],launchData['launch_date_utc'],launchData['details'])
        },
        {
            'version': '1',
            'contentType': 'application/vnd.amazonaws.card.generic',
            'genericAttachments': launchLinks 
        }
    )

def welcome_message(intent_request):
    logger.debug('Welcome Message method called.')
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    message = 'Hi, I am SpaceX Bot, You can ask me about Rockets, Missions & Launches. Either select from option or Type \'Tell me about SpaceX Rockets/Missions/Launches \''
    return close(output_session_attributes,
                 'Fulfilled',
                  {
                    'contentType': 'PlainText',
                    'content': message
                  },
                  {
                    'version': '1',
                    'contentType': 'application/vnd.amazonaws.card.generic',
                    'genericAttachments': [
                        {
                            'title': 'Get SpaceX Information',
                            'subTitle': 'Please select',
                            'buttons':[
                                {
                                'text':'Rockets',
                                'value':'Tell me about SpaceX Rockets'
                                },
                                {
                                'text':'Missions',
                                'value':'Tell me about SpaceX Missions'
                                },
                                {
                                'text':'Launches',
                                'value':'Tell me about SpaceX Launches'
                                }
                            ]
                        }
                    ]
                  }
                )

def end_message(intent_request):
    logger.debug('End Message method called.')
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    message = {'contentType': 'PlainText','content': 'Good Bye, Have a nice day.'}
    response = {
        'sessionAttributes': output_session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': message
        }
    }
    return response
                  
#Dispatch Method
def dispatch(intent_request):
    # Get current intent name
    intent_name = intent_request['currentIntent']['name']
    logger.debug('Intent Called = {}'.format(intent_name))
    if intent_name == 'Rockets':
        # Calling Rockets Intent Fulfillment Code
        logger.debug('Calling Rockets Intent Fulfillment Code')
        return call_rockets(intent_request)
    elif intent_name == 'Missions':
        # Calling Missions Intent Fulfillment Code
        logger.debug('Calling Missions Intent Fulfillment Code')
        return call_missions(intent_request)
    elif intent_name == 'Launches':
        # Calling Missions Intent Fulfillment Code
        logger.debug('Calling Launches Intent Fulfillment Code')
        return call_launches(intent_request)
    elif intent_name == 'Welcome':
        # Welcome Intent Fulfillment Code
        logger.debug('Welcome Intent Fulfillment Code')
        return welcome_message(intent_request)
    elif intent_name == 'End':
        logger.debug('End Intent Fulfillment Code')
        return end_message(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')
    
#Main Handler
def lambda_handler(event, context):
    logger.debug('Started : {}'.format(event['bot']['name']))
    logger.debug('Calling dispatch function with intent request')
    return dispatch(event)
```

## Web App Code (main.js)
```javascript
import Vue from 'vue';
import Vuex from 'vuex';
import Vuetify from 'vuetify';
import {
  Config as AWSConfig,
  CognitoIdentityCredentials
} from 'aws-sdk/global';
import LexRuntime from 'aws-sdk/clients/lexruntime';
import Polly from 'aws-sdk/clients/polly';
import 'roboto-fontface/css/roboto/roboto-fontface.css';
import 'material-design-icons/iconfont/material-icons.css';
import 'vuetify/dist/vuetify.min.css';
import 'aws-lex-web-ui/dist/lex-web-ui.css';
import {
  Plugin as LexWebUi,
  Store as LexWebUiStore
} from 'aws-lex-web-ui/dist/lex-web-ui';

Vue.use(Vuex);
Vue.use(Vuetify);

const poolId = 'eu-west-1:3de4a6cc-970f-4ed5-b723-272ed255b31d';
const region = 'eu-west-1';
const credentials = new CognitoIdentityCredentials(
  { IdentityPoolId: poolId },
  { region }
);
const awsConfig = new AWSConfig({ region, credentials });
const lexRuntimeClient = new LexRuntime(awsConfig);
const pollyClient = new Polly(awsConfig);

const store = new Vuex.Store(LexWebUiStore);

// see the configuration section for details about the config fields
const config = {
  cognito: { poolId },
  lex: {
    botName: 'SpaceXBot',
    botAlias: '$LATEST',
    initialText: '',
    initialSpeechInstruction:
      "Say 'Tell me about Rockets' or 'Tell me about Missions' or 'Tell me about Launches' to get started."
  },
  ui: {
    parentOrigin: '',
    toolbarTitle: 'SpaceX Bot',
    toolbarLogo: '',
    enableLogin: false,
    AllowSuperDangerousHTMLInMessage: true,
    shouldDisplayResponseCardTitle: true,
    pushInitialTextOnRestart: true,
    directFocusToBotInput: true
  }
};

Vue.use(LexWebUi, { config, awsConfig, lexRuntimeClient, pollyClient });

// instantiate Vue
const vm = new Vue({
  el: '#lex-web-ui',
  // vuex store is in the lexWebUi instance
  store,
  // you can use the global LexWebUi/<lex-web-ui> commponent in templates
  template: `
    <div id="lex-web-ui-app">
      <lex-web-ui
        v-on:updateLexState="onUpdateLexState"
      ></lex-web-ui>
    </div>`,
  methods: {
    onUpdateLexState(lexState) {
      // handle lex state change events
    }
  }
});
```

## Author

Shubham Gupta
