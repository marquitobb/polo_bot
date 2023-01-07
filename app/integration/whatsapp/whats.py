from heyoo import WhatsApp
messenger = WhatsApp('EABJj1xxxxxx',phone_number_id='1130xxxxxxxx')
# For sending a Text messages
messenger.send_message('Hello I am WhatsApp Cloud API', '91989155xxxx')
# For sending an Image
messenger.send_image(
        image="https://i.imgur.com/YSJayCb.jpeg",
        recipient_id="91989155xxxx",
    )