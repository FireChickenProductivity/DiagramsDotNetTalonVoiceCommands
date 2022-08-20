from talon import actions, Module, Context

module = Module()
@module.action_class
class Actions:
    def fire_chicken_diagrams_os_normalized_keypress(keys: str):
        '''Presses keys but converts Windows keyboard shortcuts to Mac keyboard shortcuts on Mac for diagrams.net'''
        normalized_keys = actions.user.fire_chicken_diagrams_os_normalize_keys(keys)
        actions.key(normalized_keys)
    def fire_chicken_diagrams_os_normalize_keys(keys: str):
        '''Normalizes Windows keyboard shortcuts to Mac when needed. On windows does nothing.'''
        return keys

mac_context = Context()
mac_context.matches = r'''
os: mac
'''
@mac_context.action_class('user')
class MacActions:
    def fire_chicken_diagrams_os_normalize_keys(keys: str):
        '''Normalizes Windows keyboard shortcuts to Mac when needed.'''
        return keys.replace('ctrl', 'cmd')
