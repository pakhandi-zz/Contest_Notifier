#!/usr/bin/env python

import os
import sys
import pytz
import time
import signal
import thread
import urllib2

from Tkinter import *

from gi.repository import Gtk as gtk
from gi.repository import Notify as notify
from gi.repository import AppIndicator3 as appindicator

from datetime import datetime
from icalendar import vDatetime
from icalendar import Calendar, Event

local_tz = pytz.timezone('Asia/Calcutta')

global this_path

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

def aslocaltimestr(utc_dt):
    return str(utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z'))


APPINDICATOR_ID = 'myappindicator'

def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath(this_path+'/new_icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	notify.init(APPINDICATOR_ID)
	gtk.main()

def build_menu():
	menu = gtk.Menu()

	item_today = gtk.MenuItem('Today')
	item_today.connect('activate', today)
	menu.append(item_today)

	item_update = gtk.MenuItem('Sync')
	item_update.connect('activate', start_update)
	menu.append(item_update)

	item_clock = gtk.MenuItem('Clock')
	item_clock.connect('activate', elapse)
	menu.append(item_clock)

	nlist = fill()

	for event in nlist:
		this_event = event
		year_month_DateTimeSummary = this_event.split('-',2)
		date_time_summary = year_month_DateTimeSummary[2].split(' ', 2)
		item_contest = gtk.MenuItem(date_time_summary[0]+"-"+year_month_DateTimeSummary[1]+"-"+year_month_DateTimeSummary[0]+" ("+date_time_summary[1]+") "+date_time_summary[2])
		menu.append(item_contest)

	item_quit = gtk.MenuItem('Quit')
	item_quit.connect('activate', quit)
	menu.append(item_quit)

	menu.show_all()
	return menu

def fill():
	this_list = []
	
	extract_info("TC.ics",this_list)
	extract_info("CF.ics",this_list)
	this_list.sort()
	return this_list

def extract_info(file_name, this_list):
	now = time.strftime("%Y-%m-%d");
	now = now + " " + time.strftime("%H:%M:%S");

	g = open(this_path+'/'+file_name,'rb')
	gcal = Calendar.from_ical(g.read())
	for component in gcal.walk():
		if component.name == "VEVENT":
			start = component.get('dtstart')
			
			year = str(start.dt)
			year = year[:4]

			if(year<"2015"):
				continue

			start_time = aslocaltimestr(vDatetime.from_ical(start.to_ical()))
			temp_time = start_time.split(' ',3)
			final_time = str(temp_time[0])
			temp_time[1] = temp_time[1].split('.',2)
			final_time = final_time + " " + str(temp_time[1][0])
			
			if final_time < now:
				continue;

			this_summary = str(component.get('summary'))

			fstr = final_time+" --> "+this_summary
			this_list.append(fstr)
	g.close()
	return this_list

def today(_):

	nlist = fill()

	now = time.strftime("%Y-%m-%d");
	now_date = now

	for event in nlist:
		this_event = event
		year_month_DateTimeSummary = this_event.split('-',2)
		date_time_summary = year_month_DateTimeSummary[2].split(' ', 2)
		
		if( year_month_DateTimeSummary[0]+"-"+year_month_DateTimeSummary[1]+"-"+date_time_summary[0] != now_date ):
			continue
		
		notify.Notification.new("<b>Contest : </b>", date_time_summary[0]+"-"+year_month_DateTimeSummary[1]+"-"+year_month_DateTimeSummary[0]+" ("+date_time_summary[1]+") "+date_time_summary[2], None).show()


def start_update(_):
	thread.start_new_thread(update, ())

def update():
	download("https://www.google.com/calendar/ical/br1o1n70iqgrrbc875vcehacjg%40group.calendar.google.com/public/basic.ics","CF.ics")
	download("https://www.google.com/calendar/ical/appirio.com_bhga3musitat85mhdrng9035jg%40group.calendar.google.com/public/basic.ics","TC.ics")
	os.execv(__file__, sys.argv)

def download(url,file_name):
	'''
	#Uncomment to add support for proxy
	proxy = urllib2.ProxyHandler({'https': 'username:password@ip:port'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)
	'''
	response = urllib2.urlopen(url)
	html = response.read()
	if len(html) == 0:
		return
	f = open(this_path+"/"+file_name, 'w')
	f.write(html)

def quit(_):
	notify.uninit()
	gtk.main_quit()

global time1
global clock

def tick():
	global time1
	global clock
	time2 = datetime.now().replace(microsecond=0)
	clock.config(text=(time2-time1))
	clock.after(200, tick)


def elapse(_):
	root = Tk()
	root.wm_attributes('-topmost', 1)
	ws = root.winfo_screenwidth()
	root.geometry('+'+str(ws-30)+'+10')
	time1 = datetime.now().replace(microsecond=0)
	global clock
	clock = Label(root, font=('times', 20, 'bold'), bg='black',fg='green')
	clock.pack(fill=BOTH, expand=1)
	global time1
	time1 = datetime.now().replace(microsecond=0)
	tick()
	root.mainloop()

if __name__ == "__main__":
	global this_path
	if getattr(sys, 'frozen', False):
	    this_path = os.path.dirname(os.path.abspath(sys.executable))
	else:    
		this_path = os.path.dirname(os.path.abspath(__file__))
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()