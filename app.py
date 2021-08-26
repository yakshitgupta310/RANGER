from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from main import *
import emoji


app = Flask(__name__)


# Flask app route
@app.route("/")
def hello():
    return "Hello, This is scam check whatsapp bot!!!"

# Flask app route which handles all the backend part of the bot.


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    # Create reply
    resp = MessagingResponse()

    # To check is incoming message is a integer or not.
    onlyinteger = msg.isdecimal()

    # Responses for different messages.
    if msg == "Hi" or msg == "Hello" or msg == "hi" or msg == "hello":
        response = emoji.emojize("""*Hi! I am the Verification Bot* :wave: \nYou can give me the following commands: \n :black_small_square: *Verify* : Verify a number. \n :black_small_square: *Report* : Report a Cyber Crime.""", use_aliases=True)
        resp.message(response)

    elif msg == "Verify" or msg == "verify":
        resp.message("Provide the number to be verified.")

    elif msg == "Report" or msg == "report":
        response = emoji.emojize("If you have been a victim of any Cyber Crime such as Scam/Phishing. \nYou can file a complaint for the same on the *Govt. of India* :India: authorized portal. \nhttps://cybercrime.gov.in/", use_aliases=True)
        resp.message(response)

    elif onlyinteger is True:
        invalid = False

        # To check for valid number
        if len(msg) != 10:
            resp.message("Enter a valid mobile number.")
            invalid = True
        if not invalid:
            # Tally checks if specified mobile number is present in database.
            tally = numbercheck(msg)
            if tally == -1:
                resp.message("Number not found in database.")
            else:
                response = emoji.emojize(':warning: Number found. \nThis number has been reported for Fraud/Phishing related crimes.🚨 \nIf this number is trying to contact you report it.')
                resp.message(response)

    else:
        response = """Sorry, I don't understand. Send 'hello' for a list of commands."""
        resp.message(response)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
