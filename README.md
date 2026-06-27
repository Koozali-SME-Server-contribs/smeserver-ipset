# <img src="https://www.koozali.org/images/koozali/Logo/Png/Koozali_logo_2016.png" width="25%" vertical="auto" style="vertical-align:bottom"> smeserver-ipset

SMEServer Koozali developed git repo for smeserver-ipset contrib

## Wiki
<br />https://wiki.koozali.org/smeserver-ipset

## Bugzilla
Show list of outstanding bugs: [All](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=UNCONFIRMED&bug_status=CONFIRMED&bug_status=NEEDINFO&bug_status=IN_PROGRESS&bug_status=RESOLVED&bug_status=VERIFIED&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced)  
[Confirmed](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=CONFIRMED&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced)  
[Unconfirmed](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=UNCONFIRMED&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced)  
[Need Info](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=NEEDINFO&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced)  
[In Progress](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=IN_PROGRESS&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced)  
[Verified](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=VERIFIED&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced)  
[Resolved](https://bugs.koozali.org/buglist.cgi?action=wrap&bug_status=RESOLVED&classification=Contribs&component=smeserver-ipset&list_id=105781&order=changeddate+DESC%2Ccomponent%2Cpriority%2Cbug_severity&product=SME+Contribs&query_format=advanced) 

## Description

A Bash shell script which uses ipset and iptables to ban a large number of IP addresses published in IP blacklists. ipset uses a hashtable to store/fetch IP addresses and thus the IP lookup is a lot (!) faster than thousands of sequentially parsed iptables ban rules.

