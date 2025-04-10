
---

### 📂 `streaming_ingestion.py`

This is your Pub/Sub-triggered entry point:

```python
import base64
import json
from inference_handler import send_to_vertex

def pubsub_callback(event, context):
    try:
        message_data = base64.b64decode(event["data"]).decode("utf-8")
        record = json.loads(message_data)

        cleaned_input = {
            "amount": record.get("amount", 0.0),
            "merchant": record.get("merchant", "unknown"),
            "category": record.get("category", "uncategorized"),
            "location": record.get("location", "NA")
        }

        prediction = send_to_vertex(cleaned_input)
        print("✅ Inference response:", prediction)

    except Exception as e:
        print("⚠️ Error processing message:", str(e))
