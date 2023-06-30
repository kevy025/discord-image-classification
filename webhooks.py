from discord_webhook import DiscordWebhook
import time
import random
r = 0
# rand = 0
# webhook = 0
# print(webhook)
webhook_url = 'https://discord.com/api/webhooks/1122883876948295732/RJAVOzYqorbK8wwJ2bTt7BKW81avaQ9ywkuOjmeZRbYOPi4aGgVJV-6kmgYQObkdcYWy'
test_img_url = 'https://i.etsystatic.com/39165197/r/il/8454e5/4829122423/il_570xN.4829122423_5nrn.jpg'

while r != 1 :
 webhook = DiscordWebhook(url=webhook_url,rate_limit_retry=False,content='Hello New Employee!')
 time.sleep(.2)
 r += 1
 rand = random.randint(100000910000091000009,999999999999999999999)
 response = webhook.execute()
 print(webhook)
 time.sleep(.5)






# webhook = DiscordWebhook(url=webhook_url,rate_limit_retry=False,content='You find yourself at your new job')
# time.sleep(.2)
# # r += 1
# # rand = random.randint(100000910000091000009,999999999999999999999)
# response = webhook.execute()
# print(webhook)
# time.sleep(.5)




# from discord_webhook import DiscordWebhook, DiscordEmbed

# webhook = DiscordWebhook(url=webhook_url)

# # create embed object for webhook
# # you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
# embed = DiscordEmbed(title='New Employee', description='Minimum Waige, working at the ~~**REDACTED**~~ company', color='03b2f8')

# # add embed object to webhook
# webhook.add_embed(embed)

# response = webhook.execute()






from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url=webhook_url)

# create embed object for webhook
embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color='03b2f8')

# set author
embed.set_author(name='Etsy', url='https://www.etsy.com/listing/1438506120/youre-a-girlboss-justin-bieber-meme', icon_url=test_img_url)

# set image
embed.set_image(url=test_img_url)

# set thumbnail
embed.set_thumbnail(url=test_img_url)

# set footer
embed.set_footer(text='Embed Footer Text', icon_url=test_img_url)

# set timestamp (default is now)
embed.set_timestamp()

# # add fields to embed
embed.add_embed_field(name='Field 1', value='Lorem ipsum')
embed.add_embed_field(name='Field 2', value='dolor sit')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()