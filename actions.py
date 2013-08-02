# Victoria Tisdale
# actions.py

from controlflow import GetRDMAction
from ola import PidStore

class GetDeviceInfo(GetRDMAction):
  """An action that GETs DEVICE_INFO."""
  PID = "DEVICE_INFO"

  def ShouldExecute(self):
    """SKip this action if we already have DEVICE_INFO."""
    print self._data
    return self.PID not in self._data

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value

class GetSupportedParams(GetRDMAction):
  """
  """
  PID = "SUPPORTED_PARAMETERS"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return self.PID not in self._data

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = set(p['param_id'] for p in value['params'])

class GetDeviceLabel(GetRDMAction):
  """
  """
  PID = "DEVICE_LABEL"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    pid_key = self._pid_store.GetName(self.PID)
    return (self.PID not in self._data 
                            and pid_key in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["label"]


# ############################ Get Basic Info ############################

class GetProductDetailIds(GetRDMAction):
  PID = "PRODUCT_DETAIL_ID_LIST"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID]= set(
                            data['detail_id'] for data in value['detail_ids'])

class GetDeviceModel(GetRDMAction):
  """
  """
  PID = "DEVICE_MODEL_DESCRIPTION"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["description"]

class GetManufacturerLabel(GetRDMAction):
  """
  """
  PID = "MANUFACTURER_LABEL"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["label"]

class GetFactoryDefaults(GetRDMAction):
  """
  """
  PID = "FACTORY_DEFAULTS"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["using_defaults"]

class GetSoftwareVersion(GetRDMAction):
  """
  """
  PID = "SOFTWARE_VERSION_LABEL"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["label"]

class GetBootSoftwareVersion(GetRDMAction):
  """
  """
  PID = "BOOT_SOFTWARE_VERSION"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["version"]

class GetBootSoftwareLabel(GetRDMAction):
  """
  """
  PID = "BOOT_SOFTWARE_LABEL"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["label"]


# ############################ Get DMX Info ############################

class GetDmxPersonality(GetRDMAction):
  """
  """
  PID = "DMX_PERSONALITY"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value

class GetPersonalityDescription(GetRDMAction):
  """
  """
  PID = "DMX_PERSONALITY_DESCRIPTION"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      index = value["personality"]
      personalities = self._data.setdefault(self.PID, {})
      self._data[self.PID][index] = {"slots_required":value["slots_required"],
                                     "name":value["name"]}
      

class GetStartAddress(GetRDMAction):
  """
  """
  PID = "DMX_START_ADDRESS"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["dmx_address"]

class GetSlotInfo(GetRDMAction):
  """
  """
  PID = "SLOT_INFO"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value

class GetSlotDescription(GetRDMAction):
  """
  """
  PID = "SLOT_DESCRIPTION"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value

class GetDefaultSlotValue(GetRDMAction):
  """
  """
  PID = "DEFAULT_SLOT_VALUE"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value


# ############################ Get Sensors Info ############################

# the following classes need data

class GetSensorDefinition(GetRDMAction):
  """
  """
  PID = "SENSOR_DEFINITION"
    
  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value

class GetSensorValue(GetRDMAction):
  """
  """
  PID = "SENSOR_VALUE"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value


# # ############################ Get Setting Info ############################

class GetDeviceHours(GetRDMAction):
  """
  """
  PID = "DEVICE_HOURS"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["hours"]
 
class GetLampHours(GetRDMAction):
  """
  """
  PID = "LAMP_HOURS"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["hours"]

class GetLampStrikes(GetRDMAction):
  """
  """
  PID = "LAMP_STRIKES"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["strikes"]

class GetLampState(GetRDMAction):
  """
  """
  PID = "LAMP_STATE"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["state"]

class GetLampOnMode(GetRDMAction):
  """
  """
  PID = "LAMP_ON_MODE"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["mode"]

class GetPowerCycles(GetRDMAction):
  """
  """
  PID = "DEVICE_POWER_CYCLES"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["power_cycles"]

class GetPowerState(GetRDMAction):
  """
  """
  PID = "POWER_STATE"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["power_state"]


# # ############################ Get Config Info ############################
class GetLanguageCapabilities(GetRDMAction):
  """
  """
  PID = "LANGUAGE_CAPABILITIES"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["languages"]

class GetLanguage(GetRDMAction):
  """
  """
  PID = "LANGUAGE"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["language"]

class GetDisplayInvert(GetRDMAction):
  """
  """
  PID = "DISPLAY_INVERT"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["invert_status"]

class GetDisplayLevel(GetRDMAction):
  """
  """
  PID = "DISPLAY_LEVEL"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["level"]

class GetPanInvert(GetRDMAction):
  """
  """
  PID = "PAN_INVERT"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["invert"]

class GetTiltInvert(GetRDMAction):
  """
  """
  PID = "TILT_INVERT"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["invert"]

class GetPanTiltSwap(GetRDMAction):
  """
  """
  PID = "PAN_TILT_SWAP"

  def ShouldExecute(self):
    """" Skip this action if we already have the supported params"""
    return (self.PID not in self._data 
                            and self.PID in self._data["PARAM_NAMES"])

  def UpdateDict(self, succeeded, value):
    if succeeded:
      self._data[self.PID] = value["swap"]

  # def _get_real_time(self):
  #   pid_key = self._pid_store.GetName("REAL_TIME_CLOCK")
  #   if (pid_key.value in self._uid_dict[self.cur_uid]['SUPPORTED_PARAMETERS']
  #         and "REAL_TIME_CLOCK" not in self._uid_dict[self.cur_uid]):
  #     self.ola_thread.rdm_get(self.universe.get(), 
  #                             self.cur_uid,
  #                             0, 
  #                             pid_key.name, 
  #                             lambda b, s: self._get_real_time_complete(b, s)
  #                             )
  #   else:
  #     self._notebook.RenderConfigInformation(self._uid_dict[self.cur_uid])

  # def _get_real_time_complete(self, succeeded, data):
  #   if succeeded:
  #     print ""
  #     self._uid_dict[self.cur_uid]["REAL_TIME_CLOCK"] = data
  #   else:
  #     print "failed"
  #   # store the results in the uid dict
  #   self._notebook.RenderConfigInformation(self._uid_dict[self.cur_uid])
