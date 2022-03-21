# Notification Functions
This repo provides the source code for functions to send notification via OCI Notification and Telegram using OCI Functions.

## **Send Notification via Telegram**

### **1.Create Telegram Bot**
1. Search for BotFather in telegram search bar.
2. In the BotFather chat, type `/newbot`
3. Give a nice name to the bot eg. `OCI Telebot`
4. Give a username for the bot. This must be unique and must end in `bot`. for example: `OciTeleBot` or `oci_telebot`.
5. Once the bot is created successfully, Bot access token will be shown. Safe keep this token as this will be needed to send message through the bot.

```
Done! Congratulations on your new bot. You will find it at t.me/***bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5*******:A***********8
Keep your token secure and store it safely, it can be used by anyone to control your bot.
```

### **2(a).Create Channel For Notification Broadcast**
1. Press the "New Message" icon ![new_message](img/new_message_icon.png)
2. Select "New Channel" and press "Create Channel".
3. Give a meaningful channel name and press "Next".
4. Select "Public" channel type and key in a unique channel name after `https://t.me/`.
5. Press "Done" and the channel will be created.
6. Click on Channel Info (the channel name on the chat), press "Administrators" and press "Add Admin".
7. In the search bar, key in the bot name, select the bot and press "Done".

### **2(b).Create Group Chat for Notification Broadcast**
1. Press the "New Message" icon ![new_message](img/new_message_icon.png)
2. Select "New Group" and add the bot to the group.
3. Give a meaningful group name and press "Create".
4. To check the Chat ID, go to [Web Telegram](https://web.telegram.org) and login using your account.
5. Click on the group chat, you will see the Chat ID on the url after #. For example, `https://web.telegram.org/z/#-123456789`, Chat_ID = -123456789.

### 3.Send message via fn cli for testing 
1. Invoke function via fn cli
```
echo -n '{"api_key":"<Bot_Token>", "chat_id":"<Chat_ID or Channel_Name>", "text": "<Your_Message>"}' | fn invoke send-telegram send-telegram
```

`Bot_Token`: Refer to step 1.5

`Channel_Name`: Refer to step 2(a).4

`Chat_ID`: Refer to step 2(b).5

For example:
```
echo -n '{"api_key":"5****:AAF******Tw", "chat_id":"-772650973", "text": "How are you doing today?"}' | fn invoke send-telegram send-telegram
```
```
echo -n '{"api_key":"5****:AAF******Tw", "chat_id":"@ocitelebot", "text": "How are you doing today?"}' | fn invoke send-telegram send-telegram
```

## **Send Notification via OCI Notification**

### 1.Create Notification Topic and Subscription
1. Press "Create Topic" and input a meaningful name. Press "Create".
2. On the Topic Details page, press "Create Subsciption".
3. Select "Email", key in the recipient email address and press "Create".
4. You will receive an email titled "Oracle Cloud Infrastructure Notifications Service Subscription Confirmation". Click "Confirm subscription"
5. Return to Topic Details page, copy the topic OCID.

### 2.Send message via fn cli for testing 
1. Invoke function via fn cli
```
echo -n '{"topic_id":"<topic_id>", "title":"<Message_Title>", "message": "<Your_Message>"}' | fn invoke send-notification send-notification
```

`topic_id`: Refer to step 1.5

For example:
```
echo -n '{"topic_id":"ocid1.onstopic.oc1.phx.aaaaaaaahpepyvcuzddrswhy6wqqjwt2my222mejpb27liqog5ky2gaxohgq", "title":"Sent From Functions", "message": "How are you doing today?"}' | fn invoke send-notification send-notification
```