import io
import json
import logging
from datetime import datetime, timezone
import oci

from fdk import response

def handler(ctx, data: io.BytesIO = None):
    datetimeNow= datetime.now(timezone.utc).isoformat(timespec='seconds')
    try:
        request_body = json.loads(data.getvalue())
        topicID = request_body.get("topic_id")
        message = request_body.get("message")
        msgTitle = request_body.get("title")
        dashboardURL = request_body.get("url")
        alertType = request_body.get("alert_type")
        
        signer = oci.auth.signers.get_resource_principals_signer()
        ons_client = oci.ons.NotificationDataPlaneClient(config={},signer=signer)

        publish_message_response = ons_client.publish_message(
            topic_id=topicID,
            message_details=oci.ons.models.MessageDetails(
                body="["+alertType+"] "+message+" at "+datetimeNow+"\n\nPlease view the dashboard via this link "+dashboardURL,
                title="["+alertType+"] "+msgTitle),
            message_type="RAW_TEXT"
        )
        send_status = 'succeed'
        logging.getLogger().info("Message sent successfully")
        logging.getLogger().info(publish_message_response.data)

    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))
        send_status = 'failed'

        return response.Response(
        ctx, response_data=json.dumps({"status": format(send_status), "message_id" : format(ex)}),
        headers={"Content-Type": "application/json"}
        )

    return response.Response(
        ctx, response_data=json.dumps({"status": format(send_status), "message_id": format(publish_message_response.data.message_id)}),
        headers={"Content-Type": "application/json"}
    )
