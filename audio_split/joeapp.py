from pydub import AudioSegment

def convert_to_wav(input_file, output_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)
    
    # Export the audio as WAV
    audio.export(output_file, format="wav")

def split_and_save_audio(input_file, output_file1, output_file2):
    # Load the WAV file
    audio = AudioSegment.from_wav(input_file)
    
    # Calculate the split point (half of the audio duration)
    split_point = len(audio) // 2
    
    # Split the audio into two parts
    part1 = audio[:split_point]
    part2 = audio[split_point:]
    
    # Save the split parts as separate WAV files
    part1.export(output_file1, format="wav")
    part2.export(output_file2, format="wav")

if __name__ == "__main__":
    input_file = "Essence.mp3"        # Specify your input MP3 file
    temp_wav_file = "temp.wav"       # Specify temporary WAV file
    output_file1 = "output1.wav"    # Specify the name for the first split part
    output_file2 = "output2.wav"    # Specify the name for the second split part

    # Convert MP3 to WAV
    convert_to_wav(input_file, temp_wav_file)

    # Split and save audio
    split_and_save_audio(temp_wav_file, output_file1, output_file2)
