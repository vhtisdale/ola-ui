from collections import deque

class RDMAction(object):
  """The base class all actions inherit from."""
  def Execute(self, on_complete):
    on_complete()

class GetRDMAction(RDMAction):
  """An action which performs an RDM GET."""
  def __init__(self, data_dict, get_fn, get_data = None):
    """Create a new GET action.

    Args:
      data_dict: the dict to update
      get_fn: the function to use for RDM GETs
    """
    self._data = data_dict
    self._get_fn = get_fn
    self._get_data = get_data

  def params(self):
    """This method provides the parameters for the GET."""
    return []

  def update_dict(succeeded, params):
    """This method is called when the GET completes."""
    pass

  def should_execute(self):
    """This method controls if the action should be skipped."""
    return True

  def execute(self, universe, uid, on_complete):
    """Perform the RDM GET."""
    if not self.should_execute():
      on_complete()
      return

    self._get_fn(
        universe, uid, 0, self.PID,
        lambda b, s: self._complete(b, s, on_complete),
        [self._get_data])

  def _complete(self, succeeded, params, on_complete):
    """Called when the GET completes."""
    self.update_dict(succeeded, params)
    on_complete()

class SetRDMAction(RDMAction):
  """An action which performs an RDM GET."""
  def __init__(self, data_dict, set_fn, set_data = None):
    """Create a new GET action.

    Args:
      data_dict: the dict to update
      get_fn: the function to use for RDM GETs
    """
    self._data = data_dict
    self._set_fn = set_fn
    self._set_data = set_data

  def params(self):
    """This method provides the parameters for the SET."""
    return []

  def update_dict(succeeded, params):
    """This method is called when the SET completes."""
    pass

  def should_execute(self):
    """This method controls if the action should be skipped."""
    return True

  def execute(self, universe, uid, on_complete):
    """Perform the RDM GET."""
    if not self.should_execute():
      on_complete()
      return

    self._set_fn(
        universe, uid, 0, self.PID,
        lambda b, s: self._complete(b, s, on_complete),
        [self._set_data])

  def _complete(self, succeeded, params, on_complete):
    """Called when the GET completes."""
    self.update_dict(succeeded, self._set_data)
    on_complete()

class GetIdentify(GetRDMAction):
  """An example GET IDENTIFY_DEVICE action.

  This action always executes, since we want the latest information.
  """
  PID = "IDENTIFY_DEVICE"

  def update_dict(self, succeeded, params):
    if succeeded:
      self._data[self.PID] = params['identify_state']

class RDMControlFlow(object):
  """Create a new Control Flow.

  Args:
    universe: the universe to use
    uid: the uid to use
    actions: the list of actions to perform
    on_complete: the method to call when the control flow completes.
  """
  def __init__(self, universe, uid, actions, on_complete):
    self._universe = universe
    self._uid = uid
    self._actions = deque(actions)
    self._on_complete = on_complete

  def run(self):
    """Run the control flow."""
    self._perform_next_action()

  def _perform_next_action(self):
    if self._actions:
      # run next action
      action = self._actions.popleft()
      action.execute(self._universe, self._uid, self._perform_next_action)
    else:
      self._on_complete()

# --------------------
# !! Should I just delete all of this? !!
# example code

# def on_complete():
#   print 'control flow completed'

# def get_fn(universe, uid, sub_device, pid, callback):
#   # This just simulates a RDM GET for now
#   print 'GET %s %s %d %s' % (universe, uid, sub_device, pid)
#   if pid == 'IDENTIFY_DEVICE':
#     callback(True, {'identify_state': True})
#   elif pid == 'DEVICE_INFO':
#     callback(True, {})
#   else:
#     callback(False, {})

# def test():
#   uid = None
#   data = {}
#   flow = RDMControlFlow(
#       1,
#       uid,
#       [
#         GetIdentify(data, get_fn),
#         GetDeviceInfo(data, get_fn)

#       ],
#       on_complete)
#   flow.Run()
#   print data
  
#   print ''
#   print 'Running again...'

#   flow = RDMControlFlow(
#       1,
#       uid,
#       [
#         GetIdentify(data, get_fn),
#         GetDeviceInfo(data, get_fn)

#       ],
#       on_complete)
#   flow.Run()

# def main():
#   test()

# if __name__  ==  "__main__":
#   main()
