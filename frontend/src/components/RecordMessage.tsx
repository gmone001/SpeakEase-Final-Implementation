import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
  //function to handle the stop event from recording
  handleStop: any;
};
// the content here is just to render the record button and display the status of the recording
const RecordMessage = ({ handleStop }: Props) => {
  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-white p-4 rounded-full"
          >
            <RecordIcon
              classText={
                status == "recording"
                  ? "animate-pulse text-red-500"
                  : "text-sky-500"
              }
            />
          </button>
          <p className="mt-2 text-white font-light">{status}</p>
        </div>
      )}
    />
  );
};

export default RecordMessage;
