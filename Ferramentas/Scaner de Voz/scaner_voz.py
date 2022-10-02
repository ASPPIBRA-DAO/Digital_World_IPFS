def video_test():
	#video_path = 'test.mp4'
	#videos = load_lecture(video_path)
	desired_voice = load_files('test.mp3')
	voice_model = create_model(desired_voice)

	#predict_on_video(voice_model, 'test_1.mp4', 'results.mp4')
	#speak('make_a_video.py completed.  View results.py')

	letter_to_sound = get_letter_to_sound()
	letter_to_sound['g'] = 'ge'
	letter_to_sound['c'] = 'gs'
	letter_to_sound['S'] = 'gs'
	letter_to_sound['k'] = 'gs'
	letter_to_sound['T'] = 'gs'
	letter_to_sound['z'] = 'gs'

	words_to_num = {'three': 3, 'two': 2}
	text = 'the three '
	#text = 'the two '
	#text = 'hello, it\'s me'
	#text = 'hello, can you hear me?'
	#text = 'hello?'
	#simplified_text = tts.text_to_sequence(text, ['english_cleaners'])
	simplified_text = [text_to_sequence(sentence, ['english_cleaners'] + ['english_regular_numbers'], letter_to_sound) for sentence in text.split('.')]

	teacher_forcing = False
	clip_end_filepath = 'clip_end.wav'
	last_output_filepath = 'last_output_{}.wav'
	test_1_filepath = 'test_synthesis_1.mp4'
	test_filepath = 'test_synthesis.mp4'
	test_ wavefilepath = 'test_synthesis.wav'
	predict_on_text(text, voice_model, teacher_forcing, simplified_text, 'test_synthesis', last_output_filepath)


'''
need to install
tensorflow==1.10.0 
pydub==0.23.0
PyYAML==4.2b1
numpydoc==0.8.0
smc-tts==1.1.2
networkx==2.1
'''
if __name__ == '__main__':
	(X, mels, mags) = load_data('test.mp3')
	mel = MAX_WAV_VALUE * mels[0][1000:2000]
	mel = mel[::-1]
	spec = invert_mel(mel, mags[0][0,0,:], mel_basis)
	fs = 22050

	ipd.Audio(mel,rate=fs)
	ipd.Audio(spec,rate=fs)

	test = 0