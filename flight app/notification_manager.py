from twilio.rest import Client

TWILIO_SID = "ACde6a306d91521b0dad494b984f42beea"
TWILIO_AUTH_TOKEN = "1533eabe1b7d6a4db613a6f4ce1830fc"
TWILIO_VIRTUAL_NUMBER = "+16165233176"
TWILIO_VERIFIED_NUMBER = "+2349134710006"





class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        # print(message.sid)
