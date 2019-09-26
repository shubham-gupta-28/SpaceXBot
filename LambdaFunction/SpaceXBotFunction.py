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