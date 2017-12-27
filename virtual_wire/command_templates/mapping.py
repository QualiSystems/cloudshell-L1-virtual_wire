from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate

ACTION_MAP = OrderedDict()
ERROR_MAP = OrderedDict([(r'[Ee]rror:', 'Command error'), (r'[Cc]onflict', 'Port conflict'),
                         (r'[Pp]ort\s[Aa]ssoc\w*ation\s.+\salready\sexists', 'Port association already exists'),
                         (
                         r'[Uu]nable to find port-association to delete', 'Unable to find port-association to delete')])

ASSOCIATIONS = CommandTemplate('port-association-show format master-ports,slave-ports,name parsable-delim ":"',
                               ACTION_MAP, ERROR_MAP)
MAP_UNI = CommandTemplate(
    'port-association-create name {name} master-ports {master_ports} slave-ports {slave_ports} no-virtual-wire no-bidir',
    ACTION_MAP, ERROR_MAP)
MAP_BIDI = CommandTemplate(
    'port-association-create name {name} master-ports {master_ports} slave-ports {slave_ports} virtual-wire bidir',
    ACTION_MAP, ERROR_MAP)

MAP_CLEAR = CommandTemplate('port-association-delete name {name}', ACTION_MAP, ERROR_MAP)

PHYS_TO_LOGICAL = CommandTemplate('bezel-portmap-show format bezel-intf,port parsable-delim ":"', ACTION_MAP,
                                  ERROR_MAP)
UNI_ASSOCIATION_NAME = CommandTemplate(
    'port-association-show master-ports {master_ports} slave-ports {slave_ports} no-bidir format master-ports,slave-ports,name parsable-delim ":"',
    ACTION_MAP, ERROR_MAP)
