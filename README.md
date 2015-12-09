# Contest_Notifier
This is a basic Linux based desktop app to keep one informed with upcoming contests on TopCoder and CodeForces.

<img src="https://github.com/pakhandi/Contest_Notifier/blob/master/PyCal3.png">

<h3>Index</h3>
<ol>
<li><a href="#requisites">Requisites</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#techused">Technology Used</a></li>
<li><a href="#testing">Testing</a></li>
</ol>

<a name="requisites"><h3>Requisites</h3></a>
<ul>
<li>Linux (Tested on Ubuntu-14.04)</li>
<li>See the <a href="#installation">installation</a> section to see how to install dependencies.</li>
</ul>

<a name="installation"><h3>Installation</h3></a>
<ul>
<li>Install the following modules in Python to run the application :
	<ul>
	<li>pytz
		<ul>
		<li>Download zip file from <a href = "https://pypi.python.org/pypi/pytz/" target="_blank">here</a></li>
		<li>Unzip the zip file and run <b>python setup.py install</b></li>
		</ul>
	</li>
	<li>Tkinter
		<ul>
		<li><b>sudo apt-get install python python-tk idle python-pmw python-imaging</b></li>
		</ul>
	</li>
	<li>icalendar
		<ul>
		<li><b>sudo apt-get install python-icalendar</b></li>
		</ul>
	</li>
	</ul>
</li>
</ul>

<a name="usage"><h3>Usage</h3></a>
<ul>
<li>If you work behind a proxy, GoTo line:140 in <i>ini.py</i> and make suitable changes.</li>
<li>Configure your timezone at line:21 in <i>ini.py</i>.</li>
<li>If you have just installed the application, <i>Sync</i> to update the calendar.</li>
<li>To add the application to StartUp Applications :
	<ul>
	<li>Press the "Windows Key" or Click on "Search Button" on top of Unity Bar. Search for "StartUp Applications".
	<img src="https://github.com/pakhandi/Contest_Notifier/blob/master/PyCal1.png">
	</li>
	<li>Click on "Add".
	<img src="https://github.com/pakhandi/Contest_Notifier/blob/master/PyCal2.png">
	</li>
	<li>Enter a name, "ContestNotifier".</li>
	<li>The command will be of format "python &ltpath&gt"</li>
	<li>Click "Add"</li>
	</ul>
</li>
<li><b>Today</b> tells the contest on that particular day.</li>
<li><b>Sync</b> will sync the calendar.</li>
<li><b>Clock</b> will start a lapse time clock.</li>
</ul>

<a name="techused"><h3>Technology Used</h3></a>
<ul>
<li>The application is made using Python-2.7.9</li>
<li><b>icalendar</b>, <b>Tkinter</b> and <b>pytz</b> modules are used.
</ul>

<a name="testing"><h3>Testing</h3></a>
The program has been tested on Ubuntu14.04, 64-bit

For Hugs and Bugs drop a mail at <b>asimkprasad@gmail.com</b>
