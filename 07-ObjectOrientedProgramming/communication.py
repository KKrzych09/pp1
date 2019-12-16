import SMS
import Email

email = Email.E_mail("nowak@onet.pl", "kowalski@gmail.com", "Spotkanie w czwartek")
sms = SMS.Sms("Marian", "Stefan")

email.set_message("informuję, że nasze czwartkowe spotkanie zostało odwołane.")
email.send()

sms.set_message("jak będzie po drodze żabka to kup jeszcze czteropak.")
sms.send()