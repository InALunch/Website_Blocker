# Website_Blocker
This is a Python website blocker for Windows that blocks distracting websites for a set amount of time so you can focus on your work. Unlike more common implementations like StayFocusd, this a) blocks websites at the DNS level so it's not browser-dependent and b) provides an easy way to block for X period of time after starting the program rather than between certain hours.

IMPORTANT: You must run this program with administrator privileges. 
NOTE: This is just an alpha version. Use at your own risk.


Core functionality:
- From the command line, "python website_blocker.py" will block websites in the "blocked sites list" between certain hours on a 24-hour clock (default is 10 to 18)
- From the command line, "python website_blocker.py X minutes" will block websites in the "blocked sites list" for X minutes after the program starts. You can also say "python website_blocker.py 33 seconds" or "python website_blocker.py .765 hrs", with expected functionality
- You can rename "website_blocker.py" to "website_blocker.pyw" and then just double-click to run the program, without needing the command line interface.


TODOs: 
- Option to block by time after program is called, rather than by hours of the day -DONE
- Refactor code so we don't edit the file if it doesn't need to be edited. -DONE
- Create a separate .txt document for blocked sites
- Let Users add blocked sites from command line
- Should store default variables in classes rather than globally
- Extends usability to Mac and Linux
- Easy reversal.
  -- fails gracefully if the program is closed by Ctrl-C or shutting down, right now websites will continue to be blocked.
- use a Python cron package rather than the time.sleep hack.

Implementation Details:
- If you want to add (or remove) sites to be blocked, edit the website_list in website_blocker.py
- If you want to change the hours the default hours to block websites, edit the "condition" function in website_blocker.py (the default starting time of the blocker is 10, and ending time is 18)
