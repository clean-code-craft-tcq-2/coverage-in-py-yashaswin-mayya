from random import randrange
import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    
    coolingType_list = {
      'PASSIVE_COOLING'     : [0,35],
      'HI_ACTIVE_COOLING'   : [0,45],
      'MED_ACTIVE_COOLING'  : [0,40]
    }
  
    for cooling_type in coolingType_list.keys():
      batteryChar = dict()
      batteryChar['coolingType'] = cooling_type

      lowerLimit = coolingType_list.get(cooling_type)[0]
      upperLimit = coolingType_list.get(cooling_type)[1]

    
      self.assertTrue(typewise_alert.classify_temperature_breach(cooling_type, lowerLimit-1) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach(batteryChar['coolingType'], upperLimit) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach(batteryChar['coolingType'], lowerLimit+1) == 'NORMAL')

      self.assertTrue(typewise_alert.classify_temperature_breach(batteryChar['coolingType'], (lowerLimit+upperLimit)/2) == 'NORMAL')

      self.assertTrue(typewise_alert.classify_temperature_breach(batteryChar['coolingType'], upperLimit+1) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach(batteryChar['coolingType'], upperLimit) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach(batteryChar['coolingType'], upperLimit-1) == 'NORMAL')

      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, lowerLimit-1) == '65261, TOO_LOW')
      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, (lowerLimit+upperLimit)/2) == '65261, NORMAL')
      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, upperLimit+1) == '65261, TOO_HIGH')

      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, lowerLimit-1) == 'To: a.b@c.com \nHi, the temperature is too low')
      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, (lowerLimit+upperLimit)/2) == 'To: a.b@c.com \nHi, Breach not found!')
      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, upperLimit+1) == 'To: a.b@c.com \nHi, the temperature is too high')

      self.assertTrue(typewise_alert.check_and_alert('TO_SMS', batteryChar, randrange(lowerLimit, upperLimit)) == 'Invalid Alert Type!')

      print('All is well')


      


if __name__ == '__main__':
  unittest.main()
