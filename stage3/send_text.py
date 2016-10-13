from twilio.rest import TwilioRestClient

# Your account sid and auth token from twilio.com/user/account
account_sid = "ACa4e84e1077405fb2911695a9d168bac9"
auth_token = "b8d8c7d5e5c8595d7eb433e26065c0d7"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "Wondering whether it will actually work...",
    to = "+61431566340", # Phone number to send too.
    from_ = "+61385928928") # Twilio number
print message.sid
