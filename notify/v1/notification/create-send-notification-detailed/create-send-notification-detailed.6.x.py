# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

notification = client.notify \
                     .services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .notifications \
                     .create(
                          apn={
                              'aps': {
                                  'alert': {
                                      'title': 'Short title for Watch.'
                                  }
                              }
                          },
                          body='This is the body for all Bindings',
                          data={
                              'custom_key1': 'custom value 1',
                              'custom_key2': 'custom value 2'
                          },
                          fcm={
                              'notification': {
                                  'title': 'New alert',
                                  'body': 'Hello Bob!'
                              }
                          },
                          identity='00000001',
                          title='Generic loooooooong title for all Bindings'
                      )

print(notification.sid)
