from sugar.activity import activity
import logging
import sys, os
import gtk
import pygtk
pygtk.require('2.0')
from gtlib import translate as translate
import languages

 
class TranslateActivity(activity.Activity):
    def __init__(self, handle):
        print "running activity init", handle
        activity.Activity.__init__(self, handle)
        print "activity running"

        # Creates the Toolbox. It contains the Activity Toolbar, which is the
        # bar that appears on every Sugar window and contains essential
        # functionalities, such as the 'Collaborate' and 'Close' buttons.
        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # Creates a new button with the label "Hello World".
        #self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    	scrolled = gtk.ScrolledWindow()
        scrolled.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scrolled.props.shadow_type = gtk.SHADOW_NONE
        # When the button receives the "clicked" signal, it will call the
        # function hello() passing it None as its argument.  The hello()
        # function is defined above.
        #self.button.connect("clicked", self.hello, None)
    
	self.field_hbox = gtk.HBox(False, 0)
	self.languages_hbox = gtk.HBox(False, 0)
	self.vbox = gtk.VBox(False, 0)
	self.vbox.add(self.field_hbox)
	scrolled.add(self.vbox)
	
	self.input_field = gtk.Entry()
	self.button = gtk.Button('Translate')
	self.button.connect('clicked', self.handleTranslate)
	self.result_field = gtk.Entry()
	self.languages_buttons = []
        for lang in languages.LANGUAGES_CODES.items():
		lb = gtk.ToggleButton(lang[0])
		self.languages_buttons.append(lb)
		self.languages_hbox.add(lb)
		
	self.field_hbox.add(self.input_field)
	self.field_hbox.add(self.button)
	self.vbox.add(self.field_hbox)
	self.vbox.add(self.languages_hbox)
	self.vbox.add(self.result_field)


        # Set the button to be our canvas. The canvas is the main section of
        # every Sugar Window. It fills all the area below the toolbox.
        self.set_canvas(scrolled)
    
        # The final step is to display this newly created widget.
        scrolled.show_all()
    

    def handleTranslate(self, widget):
	#self.result_field.set_text('Loading...')
	to_langs = ''
	for lb in self.languages_buttons:
		if lb.get_active(): to_langs += languages.LANGUAGES_CODES[lb.get_label()] + ' '
	if len(to_langs.strip()) == 0: return
	result = translate(self.input_field.get_text(), to_langs.strip())
	for c in self.vbox.children()[2:]:
		self.vbox.remove(c)	
	
	
	for lang in result.items():
		result_field = gtk.Entry()
		result_field.set_text(lang[1].strip())
		field_hbox = gtk.HBox(False, 0)
		field_label = gtk.Label(languages.CODES_LANGUAGES[lang[0]])
		field_hbox.add(field_label)
		field_hbox.add(result_field)
		self.vbox.add(field_hbox)
		field_hbox.show_all()
