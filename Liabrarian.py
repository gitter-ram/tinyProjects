import tkinter as tk
import tkinter.tix as tix
#global variables
PROPERTIES_DIALOG_ATTRIB = {}
ENTRY_DIALOG_INPUT = []

#Data specific classes
class BookInfo:
  def __init__(self, acc, name, author, *):
    self.acc = ac
    self.name = name
    self.auth = author

class EntryDialog:
  def __init__(self, parent, msg):
    self.top = tk.Toplevel(parent)
    top = self.top
    
    tk.Label(top, text=msg).pack()
    EntryField = tk.Entry(top)
    EntryField.pack()
    tk.Button(top, text="OK", command=evn_buttonPreseed).pack()
  
  def exportInput(self)
    global ENTRY_DIALOG_INPUT
    ENTRY_DIALOG_INPUT.append(self.EntryField.get())
    
  def evn_buttonPressed():
    self.exportInput()
    self.top.destroy()
    
class PropertiesDialog:
  def __init__(self, parent, attributes, editmode, tup_ControlsReq, tup_commands):
    self.root = parent
    self.top = tk.Toplevel(parent)
    top = self.top
    top.pack()
    
    if not editmode:
      j = 0
      for i in attributes:
        j += 1
        tk.Label(top, text=i, anchor=tk.W).grid(row=j, column=0, sticky=tk.W)
        tk.Label(top, text=" : ").grid(row=j, column=1)
        tk.Label(top, text=attributes[i]).grid(row=j, column=2)
      btn_OK = tk.Button(top, text="OK", command=evn_BTNPressed_OK)
      btn_OK.grid(row=(j + 1), column=1)
    else:
      #The properties need to be edited
      '''How this Works:
          The user passes the names of all the widgets that must be added to the Properties fields.
          Each widget is placed right next to the attribute it points to. Further, the widgets that utilize
          the 'command' parameter can be given custom funtions to be passed to the command attribute.
          All these functions are stored as objects in the 'commands'
          tuple, passed to the initializer.
      '''
      self.dict_Entries = {} #An empty dictionary containing <attribute_name>:<Entry_widget>
      self.dict_CheckBoxes = {} #an empty dictionary like the one above
      self.checkboxes = [] #state of all the checkboxes.
      j = 0
      for i in attributes:
        j += 1
        tk.Label(top, text=i, anchor=tk.W).grid(row=j, column=0, sticky=tk.W)
        tk.Label(top, text=" : ").grid(row=j, column=1)
        #Process which command is to be added
        if(tup_ControlsReq[j] == "Label"):
          tk.Label(top, text=attributes[i]).grid(row=j, column=2)
        elif (tup_ControlsReq[j] == "Entry"):
          self.dict_Entries.update({i:tk.Entry(top, text=attributes[i])})
          self.dict_Entries[i].grid(row=j, column=2)
        elif (tup_ControlsReq[j] == "Checkbox"):
          #Code for adding a checkbox                             (TO DO)
          self.dict_CheckBoxes.update({i:tk.Checkbutton(top, text=attributes[j], onvalue=True, offvalue=False, variable=checkboxes[j])})
          self.dict_CheckBoxes[i].grid(row=j, column=2)
      btn_OK = tk.Button(top, text="OK", command=evn_BTNPressed_OK)
      btn_OK.grid(row=(j + 1), column=0)
      btn_APPLY = tk.Button(top, text="Apply", command=evn_BTNPressed_APPLY)
      btn_APPLY.grid(row=(j + 1), column=1)
      btn_Cancel = tk.Button(top, text="Cancel", command=top.destroy)
      btn_Cancel.grid(row=(j + 1), column=2)
    #Copy the attributes to the global variable:
    for i in attributes:
      PROPERTIES_DIALOG_ATTRIB.update({i:atrributes[i]})
    
  def evn_BTNPressed_OK(self):
    self.top.destroy()
  
  def evn_BTNPressed_APPLY(self):
    global PROPERTIES_DIALOG_ATTRIB
    for i in self.dict_Entries:
      PROPERTIES_DIALOG_ATTRIB.update({i:self.dict_Entries[i].get()})
    j = 0
    for i in self.dict_CheckBoxes:
      PROPERTIES_DIALOG_ATTRIB.update({i:self.checkboxes[j]})
      j += 1
    #destroy:
    self.top.destroy()
#============================================--===================
#GUI specific functions:
def doLogin(parent):
  uname_dialog = EntryDialog(parent, "Enter your user name:")
  #Code to invoke the dialog:
  
