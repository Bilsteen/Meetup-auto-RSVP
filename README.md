# Meetup-auto-RSVP
This repository is created in order to complete the take home qualification task provide by CCExtractor the link to which is https://ccextractor.org/public/gsoc/takehome

The aim of this project is to  write a program for meetup.com that sends an auto-RSVP to specific groups of users choice. One of the use cases of this project would be , suppose you are a member of a very popular meetup group which organises some very popular events. Thus as a result of this all the slots in the events gets occupied very quickly. Henceforth we want to create a program that checks if there are new events added by the group and sign in as quickly as possible so that we can reserve a seat in the groups event before all the slots are filled.

Thus the main goal of the program is to search for events in user configured groups , automatically sign in on user's behalf and henceforth send a RSVP i.e book a slot in the event before slots are closed.

The above program consists of a web scraping script which checks for new events on the specified group and returns a list of links for all the upcoming events . This list is then passed on to an automation script which logs into the meetup website using user's facebook credentials and then send an RSVP to all the upcoming events. Once executed the program checks for new events in every 30 minutes until the program is terminated via a Keyboard Interrupt on the terminal. 

# Setup
1.Clone the Meetup-auto-RSVP repo on local machine <br />
2.Create a virtual environment using the following command(optional) ``` virtualenv -p python3.8 qtask ```<br />
3.Install the required libraries using command ``` pip3 install -r requirements.txt ```<br />
4.To run the program type ``` python3 meetup.py ``` on the terminal<br />
5.Enter your facebook email-id and password <br />
6.To terminate the program press ```Ctrl + C ```<br />

# References
This project uses

1.[Selenium](https://selenium-python.readthedocs.io/index.html)<br />
2.[Beautifull Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)<br />
3.[Requests](https://pypi.org/project/requests/)<br />
4.[Time](https://docs.python.org/3/library/time.html)<br />
