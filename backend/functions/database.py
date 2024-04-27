import json
import random #for randomizing the learn instruction to make a more dynamic persona

# get recent messages
def get_recent_messages():
    # define the file name where the messages are being stored 
    file_name = "stored_data.json"
    #learn persona instructions
    learn_instruction = {
        "role": "system",
        "content": "You are helping the user learn Spanish. You primarily speak in English. Encourage the user to speak to you in Spanish. Ask them simple questions about their day or suggest words to say in Spanish. Your name is signora Andrea."
    }
    
    # initialize messages as an empty list
    messages = []

    # including a random element
    x = random.uniform(0, 1)
    #if x is greater than 0.5, the response will include ... 
    if x > 0.5:
        learn_instruction["content"] += " Add some dry humor in English to your responses."
        #if x is less than 0.5, the response will include ...
    else:
        learn_instruction["content"] += " Include a fact about latin culture in your responses."
    
    #append message to instruction to the messages list
    messages.append(learn_instruction)

    #get last messages
    try:
        with open(file_name) as user_data:
            data = json.load(user_data)
            
            # append last 5 rows of data, so it doesnt collect everything over time
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

#store messages in json file to keep track of the conversation and build on a persona
def store_messages(request_message, response_message):

    #define the file name 
    file_name = "stored_data.json"

    #get the messages exclude the first one because it is set every time the user begins
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