
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  
  reference_for_upperLimit = {
    'PASSIVE_COOLING'     : [0,35],
    'HI_ACTIVE_COOLING'   : [0,45],
    'MED_ACTIVE_COOLING'  : [0,40]
  }
  
  lowerLimit = reference_for_upperLimit.get(coolingType[0], 0)
  upperLimit = reference_for_upperLimit.get(coolingType[1], 0)

  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  
  alertTarget_reference = {
    'TO_CONTROLLER' : send_to_controller(breachType),
    'TO_EMAIL' : send_to_email(breachType)
  }

  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  alertMessage = alertTarget_reference.get(alertTarget, 'Invalid Alert Type!')
  return alertMessage


def send_to_controller(breachType):
  header = 0xfeed
  messageContent = f'{header}, {breachType}'
  printFunction(messageContent)
  return messageContent


def send_to_email(breachType):
  recepient = "a.b@c.com"
  emailBody_reference = {
    'TOO_LOW'  : 'Hi, the temperature is too low',
    'TOO_HIGH' : 'Hi, the temperature is too high'
  }

  email_content = emailBody_reference.get(breachType, 'Hi, Breach not found!')
  messageContent = f'To: {recepient} \n{email_content}'
  printFunction(messageContent)
  return messageContent


def printFunction(printData):
  print(printData)
