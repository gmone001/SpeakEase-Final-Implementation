import json
import random

# Get recent messages
def get_recent_messages():
    # Define the file name and learn instructions
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job. Ask them about their experience and why they are interested in the job. Your name is Paula. The user is called Grace. Keep your answers to under 30 words"
    }
    
    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x > 0.5:
        learn_instruction["content"] += " Your Response will include some dry humor."
    else:
        learn_instruction["content"] += " Your Response will include a challenging question."
    
    #append message to instruction
    messages.append(learn_instruction)

    #get last messages
    try:
        with open(file_name) as user_data:
            data = json.load(user_data)
            
            # append last 5 rows of data, so it doesnt collect everything
            if data:
                if len(data) > 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)

    except Exception as e:
        print(e)
        pass

#return messages
    return messages

# Store message
def store_messages(request_message, response_message):

    #define the file name 
    file_name = "stored_data.json"

    #get the messages exclude the first one because we are adding it on every time
    messages = get_recent_messages()[1:]

    #add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}

    messages.append(user_message)
    messages.append(assistant_message)

    #save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)
    
#reset messages
def reset_messages():
        #overwrite the current file
        open("stored_data.json", "w")