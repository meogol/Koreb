import asyncio

class SendDataToTaker():
    def send_pakage(self, list_of_commands):


        delay = 20*len(list_of_commands)
        if delay > 2000:
            delay = 2000
        await asyncio.sleep(delay)


    def send_com_list_to_taker(self):

        pass