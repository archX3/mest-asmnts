import smtplib
import smtpd
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import the smtplib module. It should be included in Python by default
# set up the SMTP server
#region
MY_ADDRESS = "georgeranch31@gmail.com"
#endregion

#region
PASSWORD = "hopeit31win"
#endregion
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    guests = {}
    #
    #
    #     # send dem som'n
    #     pass
    # dataList = [None, None, None, None, None]
    guestsTracker = 0
    questions = ["name", "email"]
    PROMPT = ">> "

    commands = ["exit", "add guest", "send emails to guest"]
    lth = len(commands)
    length = len(questions)

    s = smtplib.SMTP(host = 'smtp.gmail.com', port = 587, local_hostname = "localhost")
    s.starttls()

    s.login(MY_ADDRESS, PASSWORD)

    while True :
        print("Type:")

        idx = 0
        while idx < lth :
            print(str(idx + 1) + " to " + commands[idx])
            # print( "{} to {}". format(str(idx + 1), commands[idx]))

            idx += 1

        command = input(PROMPT)

        if (command == "1") :
            print(guests)
            break

        elif (command == "2") :
            guest = ["name", "email"]  # intentionally adding data to avoid populating all the tym

            i = 0
            while i < length :
                print("\n contact's " + questions[i])
                guest[i] = input(" >>")
                i += 1
            guests[guest[0]] = guest[1]

        elif (command == "3") :
            email_template_str = read_template("msg_template.txt")

            for name, email in guests.items() :
                msg = MIMEMultipart()  # create a message

                # add in the actual person name to the message template
                message = email_template_str.substitute(PERSON_NAME = name.title())

                # Prints out the message body for our sake
                print(message)

                # setup the parameters of the message
                msg['From'] = MY_ADDRESS
                msg['To'] = email
                msg['Subject'] = "This is TEST"

                # add in the message body
                msg.attach(MIMEText(message, 'plain'))

                # send the message via the server set up earlier.
                s.send_message(msg)
                del msg

                # Terminate the SMTP session and close the connection
            s.quit()

        else :
            print("command not found")

if __name__ == '__main__' :
    main()


