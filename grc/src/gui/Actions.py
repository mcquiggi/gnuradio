"""
Copyright 2007 Free Software Foundation, Inc.
This file is part of GNU Radio

GNU Radio Companion is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

GNU Radio Companion is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
"""

import pygtk
pygtk.require('2.0')
import gtk

######################################################################################################
# Action Names
######################################################################################################
APPLICATION_INITIALIZE = 'app init'
APPLICATION_QUIT = 'app quit'
PARAM_MODIFY = 'param modify'
BLOCK_MOVE = 'block move'
BLOCK_ROTATE_LEFT = 'block rotate left'
BLOCK_ROTATE_RIGHT = 'block rotate right'
BLOCK_PARAM_MODIFY = 'block param modify'
BLOCK_INC_TYPE = 'block increment type'
BLOCK_DEC_TYPE = 'block decrement type'
BLOCK_ENABLE = 'block enable'
BLOCK_DISABLE = 'block disable'
BLOCK_CUT = 'block cut'
BLOCK_COPY = 'block copy'
BLOCK_PASTE = 'block paste'
PORT_CONTROLLER_INC = 'port controller increment'
PORT_CONTROLLER_DEC = 'port controller decrement'
ELEMENT_CREATE = 'element create'
ELEMENT_DELETE = 'element delete'
ELEMENT_SELECT = 'element select'
NOTHING_SELECT = 'nothing select'
FLOW_GRAPH_OPEN = 'flow graph open'
FLOW_GRAPH_UNDO = 'flow graph undo'
FLOW_GRAPH_REDO = 'flow graph redo'
FLOW_GRAPH_SAVE = 'flow graph save'
FLOW_GRAPH_SAVE_AS = 'flow graph save as'
FLOW_GRAPH_CLOSE = 'flow graph close'
FLOW_GRAPH_NEW = 'flow graph new'
FLOW_GRAPH_GEN = 'flow graph gen'
FLOW_GRAPH_EXEC = 'flow graph exec'
FLOW_GRAPH_KILL = 'flow graph kill'
FLOW_GRAPH_SCREEN_CAPTURE = 'flow graph screen capture'
ABOUT_WINDOW_DISPLAY = 'about window display'

######################################################################################################
# Action Key Map
######################################################################################################
_actions_key_map = {
	#action name: (key name, mask)
	FLOW_GRAPH_NEW: ('n', gtk.gdk.CONTROL_MASK),
	FLOW_GRAPH_OPEN: ('o', gtk.gdk.CONTROL_MASK),
	FLOW_GRAPH_SAVE: ('s', gtk.gdk.CONTROL_MASK),
	FLOW_GRAPH_CLOSE: ('w', gtk.gdk.CONTROL_MASK),
	APPLICATION_QUIT: ('q', gtk.gdk.CONTROL_MASK),
	FLOW_GRAPH_UNDO: ('z', gtk.gdk.CONTROL_MASK),
	FLOW_GRAPH_REDO: ('y', gtk.gdk.CONTROL_MASK),
	ELEMENT_DELETE: ('Delete', 0),
	BLOCK_ROTATE_LEFT: ('Left', 0),
	BLOCK_ROTATE_RIGHT: ('Right', 0),
	BLOCK_PARAM_MODIFY: ('Return', 0),
	BLOCK_ENABLE: ('e', 0),
	BLOCK_DISABLE: ('d', 0),
	BLOCK_CUT: ('x', gtk.gdk.CONTROL_MASK),
	BLOCK_COPY: ('c', gtk.gdk.CONTROL_MASK),
	BLOCK_PASTE: ('v', gtk.gdk.CONTROL_MASK),
	FLOW_GRAPH_GEN: ('F5', 0),
	FLOW_GRAPH_EXEC: ('F6', 0),
	FLOW_GRAPH_KILL: ('F7', 0),
	FLOW_GRAPH_SCREEN_CAPTURE: ('Print', 0),
}

######################################################################################################
# Actions
######################################################################################################
_actions_list = (
	gtk.Action(FLOW_GRAPH_NEW, '_New', 'Create a new flow graph', 'gtk-new'),
	gtk.Action(FLOW_GRAPH_OPEN, '_Open', 'Open an existing flow graph', 'gtk-open'),
	gtk.Action(FLOW_GRAPH_SAVE, '_Save', 'Save the current flow graph', 'gtk-save'),
	gtk.Action(FLOW_GRAPH_SAVE_AS, 'Save _As', 'Save the current flow graph as...', 'gtk-save-as'),
	gtk.Action(FLOW_GRAPH_CLOSE, '_Close', 'Close the current flow graph', 'gtk-close'),
	gtk.Action(APPLICATION_QUIT, '_Quit', 'Quit program', 'gtk-quit'),
	gtk.Action(FLOW_GRAPH_UNDO, '_Undo', 'Undo a change to the flow graph', 'gtk-undo'),
	gtk.Action(FLOW_GRAPH_REDO, '_Redo', 'Redo a change to the flow graph', 'gtk-redo'),
	gtk.Action(ELEMENT_DELETE, '_Delete', 'Delete the selected blocks', 'gtk-delete'),
	gtk.Action(BLOCK_ROTATE_LEFT, 'Rotate _Left', 'Rotate the selected blocks 90 degrees', 'gtk-go-back'),
	gtk.Action(BLOCK_ROTATE_RIGHT, 'Rotate _Right', 'Rotate the selected blocks -90 degrees', 'gtk-go-forward'),
	gtk.Action(BLOCK_PARAM_MODIFY, '_Properties', 'Modify params for the selected block', 'gtk-properties'),
	gtk.Action(BLOCK_ENABLE, 'E_nable', 'Enable the selected blocks', 'gtk-connect'),
	gtk.Action(BLOCK_DISABLE, 'D_isable', 'Disable the selected blocks', 'gtk-disconnect'),
	gtk.Action(BLOCK_CUT, 'Cu_t', 'Cut', 'gtk-cut'),
	gtk.Action(BLOCK_COPY, '_Copy', 'Copy', 'gtk-copy'),
	gtk.Action(BLOCK_PASTE, '_Paste', 'Paste', 'gtk-paste'),
	gtk.Action(ABOUT_WINDOW_DISPLAY, '_About', 'About this program', 'gtk-about'),
	gtk.Action(FLOW_GRAPH_GEN, '_Generate', 'Generate the flow graph', 'gtk-convert'),
	gtk.Action(FLOW_GRAPH_EXEC, '_Execute', 'Execute the flow graph', 'gtk-execute'),
	gtk.Action(FLOW_GRAPH_KILL, '_Kill', 'Kill the flow graph', 'gtk-stop'),
	gtk.Action(FLOW_GRAPH_SCREEN_CAPTURE, 'S_creen Capture', 'Create a screen capture of the flow graph', 'gtk-print'),
)
def get_all_actions(): return _actions_list

_actions_dict = dict((action.get_name(), action) for action in _actions_list)
def get_action_from_name(action_name):
	"""
	Retrieve the action from the action list.
	Search the list and find an action with said name.
	@param action_name the action name(string)
	@throw KeyError bad action name
	@return a gtk action object
	"""
	if _actions_dict.has_key(action_name): return _actions_dict[action_name]
	raise KeyError('Action Name: "%s" does not exist'%action_name)

_accel_group = gtk.AccelGroup()
def get_accel_group(): return _accel_group

#load the actions key map
#set the accelerator group, and accelerator path
#register the key and mod with the accelerator path
for action_name, (key_name, mod) in _actions_key_map.iteritems():
	get_action_from_name(action_name).set_accel_group(get_accel_group())
	get_action_from_name(action_name).set_accel_path('<main>/'+action_name)
	gtk.accel_map_add_entry('<main>/'+action_name, gtk.gdk.keyval_from_name(key_name),mod)
