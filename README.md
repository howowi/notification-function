# notification-function
This repo provides the source code for functions to send notification via OCI Notification and Telegram using OCI Functions.

## Invoke 
1. Invoke function via fn cli
> echo -n '{"api_key":"<Bot_Token>", "chat_id":"<Group_Chat_ID>", "text": "<Your_Message>"}' | fn invoke send-telegram send-telegram