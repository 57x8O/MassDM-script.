import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('')      # Put your message between the quotations.
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('token', bot=False)
