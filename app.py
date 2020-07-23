import time 
import sys
from bs4 import BeautifulSoup
from notifications import Notification
from connection import Network 

app = "Updates Notifier"
icon_path = "./icon.jpg"
urgency = 2     #for normal urgency

print(app, " is running on cli. ")

def main():
    if len(sys.argv) < 2:
        print('Usage: app.py urls.txt ')
        sys.exit(1)
    

    feed_rss_path = sys.argv[1]

    feed_rss_file = open("./" + feed_rss_path, "r")
    feed_rss_read = feed_rss_file.read()

    feed_rss_list = feed_rss_read.split('\n')
    feed_rss_file.close()

    for i in range (len(feed_rss_list)):

        feed_rss = feed_rss_list[i]
        
        net = Network(feed_rss)

        updates = net.headlines()



        for update in updates: 

            new_notification = Notification()
            nw = new_notification.notify(app, icon_path, urgency)
        
            soup = BeautifulSoup(update['description'], features="html.parser")
            
            description = soup.get_text()

            nw.update(update['title'].upper(), description, icon_path) 
            
            nw.show() 
             
            time.sleep(60)


if __name__ == '__main__':
    main()
    
     
                
