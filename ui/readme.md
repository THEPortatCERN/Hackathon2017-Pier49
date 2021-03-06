SmartBin User Interface
=======================

Installing the UI
-----------------

You must have tomcat8 installed on the pi.  If this is not currently the
case, use apt-get to install it:
```
   sudo apt-get install tomcat8
```
When you reboot the pi, tomcat8 should start automatically

1. Copy details.sh to the raspberry pi /etc directory. Make it executable

2. Add the line
```
   /etc/details.sh & 
```
   to the /etc/rc.local script.  This will cause details.sh to run when 
   the pi boots up.

3. Assemble the user interface program using the ant build file by calling:
```
   ant
```
   This will create a WAR file in dist:  ui.war

4. Copy the ui.war file to the /var/lib/tomcat8/webapps directory and set 
   its owner id to tomcat8 

5. The user interface is now available on the pi's port 8080.  Using a
   browser on the pi itself, go to:
```
   http://localhost:8080/ui
```

How it works
------------

The script details.sh looks for two files in /tmp: nonce and case_no.  If 
present, nonce contains the hash code, and case_no contains the currently 
authenticated user's case number.  details.sh then creates some json content 
that can be directly loaded by ajax calls in the user interface code to 
display the user id and all available user parameters.  If the files are
removed, the UI goes back to showing an unauthenticated screen. 
This approach was taken for two reasons.  The first is to bypass cross site
scripting constraints because the server code is running on a different 
machine that we we cannot modify, so headers that would allow XSite scripting
to occur could not be set.  The second is to keep the 
user authentication code independant from the SmartBin user interface in 
order to keep things simple and easy to change without too much risk of 
breaking other components.


