import notify2 


class Notification:
    def __init__(self, loop=None):
        self.loop = loop

    def exit(self, n):
        self.loop.quit()


    def notify( self, app_name=None, icon_path=None, urgency=2):
        
        notify2.init(app_name)

        n = notify2.Notification(None, icon = icon_path)


        if urgency == 1:
            n.set_urgency(notify2.URGENCY_LOW)

        elif urgency == 2:
            n.set_urgency(notify2.URGENCY_NORMAL)

        elif urgency == 3:
            n.set_urgency(notify2.URGENCY_CRITICAL)

        else:
            exit()
        
        n.set_timeout(100000)

        return n