from twilio.rest import Client

def msg_mom_and_dad(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'ACf35f5d9954dc582740331774b0a3e796'
    auth_token = 'd03195fd957e1440ea37ba199ad94026'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Dad':'+919417534406', 'Mom': '+919417909836}

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'Good Morning {} !'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,

            )

        print(msg_loved_ones.sid)
