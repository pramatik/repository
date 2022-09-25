#Our imports
import os
import discord
import asyncio
import datetime
from twilio.rest import Client

#Variables
my_secret_ID = os.getenv('TOKEN_ID')
my_secret_AUTH = os.getenv('AUTH_TOKEN')
client = discord.Client()

#Auto-message that pops up when discord server is initially accessed
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  #Welcome message to greet user. The user is presented with 3 options, where they can enter 1, 2, or restart.
  await client.get_channel(962181938423160955).send("Welcome to our reminder bot! Here are some things you can say:")
  #First options tells user how much water to drink
  await client.get_channel(962181938423160955).send("How much water should I drink? Enter 1 for this option. ")
  #Second option presents user with facts from the CDC on why they shold drink water.
  await client.get_channel(962181938423160955).send("Tell me why I should drink water. Enter 2 for this option")
  #When the user types "restart" they are presented with the options again.
  await client.get_channel(962181938423160955).send("And lastly, you can say 'restart!' to make the bot list the options again.")

#Messages that send if the user enters 1 or 2  
@client.event
async def on_message(message):
  #Messages that send if the user enters 2
  #Presents CDC information on the benefits of drinking water
  if message.content.startswith('restart!') and len(message.content)==8:
    await on_ready()
  if message.content.startswith('2') and len(message.content)==1:
      await message.channel.send('According to the CDC, drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.')
  #Messages that send if the user enters 1
  if message.content.startswith('1') and len(message.content)==1:
      channel = message.channel
      await channel.send('That is a good question! How much do you weigh?')
      def check(m):
        return m.author == message.author and m.channel == channel
      #Variable that holds the weight the user enters.
      weight_input = await client.wait_for('message', check=check)
      await channel.send('Thank you for your input! How old are you?')
      #Variable that holds the age the user enters.
      age_input = await client.wait_for('message', check=check)
      #Variable to calculate the amount of water the user needs to drink in cups
      water_needed = calculate_water(weight_input.content,age_input.content)
      cups = int(water_needed/8)
      await channel.send('The recommended amount of water you need per day is: ' + str(water_needed) + ' ounces. This means that you have to drink ' + str(cups) + ' cups a day.')
    
      await channel.send('Around what time do you usually wake up at? Type in an integer in 24-hour time.')
    #Variable that stores the time the user wakes up
      wakeup_time = await client.wait_for('message', check=check)
      await channel.send('Around what time do you usually go to bed? Type in an integer in 24-hour time.')
    #Variable that stores the time the user goes to bed
      bed_time = await client.wait_for('message', check=check)
    #Variable that holds the time intervals the user should drink water. This is calculated by subtracting the wake up time from the bed time and dividing the result by the number of cups of water the user should drink(calculated using age and weight).
      time_interval_hours = (int(bed_time.content) - int(wakeup_time.content))/cups 
      await channel.send('Lastly, what is your phone number? Please input without spaces and with country code.')
      phone_number = await client.wait_for('message', check=check)
      await channel.send('Ok ! I will message you every ' + str(time_interval_hours) + ' hours starting at ' + wakeup_time.content + 'AM tomorrow to remind you to drink water.')
      time_interval_seconds = time_interval_hours * 60 * 60
      await schedule_message(time_interval_seconds,message.author)
    
#Calculation to determine the amount of water user needs to drink based on the age and weight they enter.  
def calculate_water(weight, age):
  w = float(weight)
  a = float(age)
  new_weight = float(w / 2.2)
  #If the user is younger than 30 years old, then multiply the weight by 40
  if(a < 30):
    new_weight *= 40
  #Else if the user is less than or equal to 55 years old, then multiply the weight by 35
  elif(a <= 55):
    new_weight *= 35
  else:
  #Otherwise, multiply the weight by 35
    new_weight *= 30
  #Divide the calculation derived by 28.3 constant, and return this value to the user.
  return float(new_weight/28.3)

#Sends reminders on discord to the user at scheduled times
async def schedule_message(time_interval,user):
  #Variable that holds the current date and time.
  now = datetime.datetime.today()
  #Variable that holds the incremental time of when the user should next be reminded to drink water.
  then = now+datetime.timedelta(seconds=20)
  while True:
    #Variable that holds the current time
    time = datetime.datetime.today()
    print(time)
    #time variable will continue to increment in a while loop, until the hour, minute, and second values equal the hour, minute, and second values inputed by the user. Once the times match up, the user will be presented with the message to drink water
    if time.hour == then.hour and time.minute == then.minute and time.second==then.second:
      message ="Hi there ! It's time for your messages to drink water! Respond to this message with a water drop emoji in 60 seconds or else we will send you a text message."
      await client.get_channel(962181938423160955).send(message)
      def check(m):
        return m.channel == client.get_channel(962181938423160955)
      bool = False
      start = datetime.datetime.today()
      #The 
      while True:
        now = datetime.datetime.today()
        print(now)
        then = start+datetime.timedelta(seconds=20)
        print(then)
        if(now.hour>=then.hour and now.minute>=then.minute and now.second>=then.second):
          break
        #The user must respond back with a water drop emoji within 60 seconds.
        try:
          emoji_input = await client.wait_for('message',timeout=7.0,check=check)
          if(emoji_input.content=='💧'):
            bool = True
            break
        except asyncio.TimeoutError:
          continue
          
      if(bool==True):
        await client.get_channel(962181938423160955).send('Thank you for responding! We will now text you in ' + str(int(time_interval/3600)) + ' hours reminding you to drink water')
        #If the user does not respond with a water drop emoji, then they are sent another message.
      else:
        await client.get_channel(962181938423160955).send('Sorry! We have to send you a text message now!')
        send_message()
      break   
  #Sends reminder 8 times a day since it is recommended to drink 8 cups of water a day
  for num in range(8):
    await asyncio.sleep(60)
    channel = client.get_channel(962181938423160955)
    response = f'It is time to drink water! {user.mention}'
    await channel.send(response)
    send_message()

#Sends reminder text to a phone number
def send_message():
  account_sid = 'AC14b59827a2240bcf2b58a2e266bccebd'  
  auth_token = '3023a29c50230c744234c700310189c4'

  client = Client(account_sid, auth_token)

  myTwilioNumber = "+17572804402"
  annaikas_phone = "17322841311"
  myCellPhone = "14107187248"

  message = client.messages.create(
                              body='Hi there! Do not forget to drink your water!',
                              from_=myTwilioNumber,
                              to=annaikas_phone
                          )

  print(message.sid)

client.run(os.getenv("TOKEN"))
