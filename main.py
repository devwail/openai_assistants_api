import time
from openai import OpenAI

ID = "assistants/your-assistant-id-here"  # replace with your assistant ID

client = OpenAI(api_key="YOUR_API_KEY_HERE")

chat = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "Who is the greatest businessman of all time?",  # your prompt here
        }
    ]
)

run = client.beta.threads.runs.create(thread_id=chat.id, assistant_id=ID)
print(f"👉 Run Created: {run.id}")


while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=chat.id, run_id=run.id)
    print(f"🏃 Run Status: {run.status}")
    time.sleep(0.5)
else:
    print(f"🏁 Run Completed!")

message_response = client.beta.threads.messages.list(thread_id=chat.id)
messages = message_response.data

latest_message = messages[0]
print(f"💬 Response: {latest_message.content[0].text.value}")
