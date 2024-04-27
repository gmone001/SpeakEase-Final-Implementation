import { useState } from "react";
import Title from "./Title";
import axios from "axios";
import RecordMessage from "./RecordMessage";

const Controller = () => {
  // State to manage loading status
  const [isLoading, setIsLoading] = useState(false);
  //State to store messages
  const [messages, setMessages] = useState<any[]>([]);

  //create a URL for an audio Blob object
  function createBlobURL(data: any) {
    const blob = new Blob([data], { type: "audio/mpeg" }); // Create a new Blob object
    const url = window.URL.createObjectURL(blob); // Generate a URL for the Blob
    return url;
  }

  //  handle the stop event from recording
  const handleStop = async (blobUrl: string) => {
    setIsLoading(true); // Set loading true

    // Append the recorded message to the messages array
    const myMessage = { sender: "me", blobUrl };
    const messagesArr = [...messages, myMessage];

    // conver the blob URL to a Blob object
    fetch(blobUrl)
      .then((res) => res.blob())
      .then(async (blob) => {
        // Construct FormData to send the file
        const formData = new FormData();
        formData.append("file", blob, "myFile.wav");

        //send FormData to the backend API endpoint
        await axios
          .post("http://localhost:8000/post-audio", formData, {
            headers: {
              "Content-Type": "audio/mpeg",
            },
            responseType: "arraybuffer", //check that the response is treated as binary data
          })
          .then((res: any) => {
            const blob = res.data;
            const audio = new Audio(); // create a new audio object
            audio.src = createBlobURL(blob); // Set the source of the audio to the blob URL

            //append the response from teacher to the messages array
            const rachelMessage = { sender: "rachel", blobUrl: audio.src };
            messagesArr.push(rachelMessage);
            setMessages(messagesArr); // Update the state with the new messages

            //playing audio
            setIsLoading(false);
            audio.play();
          })
          .catch((err: any) => {
            console.error(err); 
            setIsLoading(false); // reset loading state on error
          });
      });
  };

  return (
    <div className="h-screen overflow-y-hidden">
      {/* Title component with a function to set messages */}
      <Title setMessages={setMessages} />

      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        {/* Container for conversation messages */}
        <div className="mt-5 px-5">
          {messages?.map((audio, index) => (
            <div
              key={index + audio.sender}
              className={
                "flex flex-col " +
                (audio.sender === "rachel" ? "flex items-end" : "")
              }>
              {/* Display sender */}
              <div className="mt-4">
                <p
                  className={
                    audio.sender === "rachel"
                      ? "text-right mr-2 italic text-green-500"
                      : "ml-2 italic text-blue-500"
                  }>
                  {audio.sender}
                </p>
                {/* Audio player for each message */}
                <audio
                  src={audio.blobUrl}
                  className="appearance-none"
                  controls
                />
              </div>
            </div>
          ))}
          {/* Prompt when no messages are available */}
          {messages.length === 0 && !isLoading && (
            <div className="text-center font-light italic mt-10">
              Start Speaking to Begin Your Lesson...
            </div>
          )}
          {/* Loading indicator */}
          {isLoading && (
            <div className="text-center font-light italic mt-10 animate-pulse">
              One Moment Please...
            </div>
          )}
        </div>

        {/* Fixed recorder bar at the bottom of the screen */}
        <div className="fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-indigo-500 to-purple-500">
          <div className="flex justify-center items-center w-full">
            <RecordMessage handleStop={handleStop} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Controller;
