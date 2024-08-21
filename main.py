import cv2
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag, ne_chunk

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Dictionary to map recognized words to corresponding sign language images
text_to_sign = {
    "hello": "path_to_hello_sign_image.png",
    "world": "path_to_world_sign_image.png",
    # Add more words and corresponding image paths here
}

def speech_to_text():
    """Capture and convert speech to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Request failed; check your internet connection")
        return None

def analyze_text(text):
    """Analyze text for common words and named entities."""
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Frequency distribution of words
    freq_dist = FreqDist(filtered_words)
    print("\nMost common words:")
    for word, frequency in freq_dist.most_common(10):
        print(f"{word}: {frequency}")

    # Part-of-Speech Tagging
    pos_tags = pos_tag(filtered_words)
    print("\nPart-of-Speech Tags:")
    for word, tag in pos_tags:
        print(f"{word}: {tag}")

    # Named Entity Recognition
    named_entities = ne_chunk(pos_tags)
    print("\nNamed Entities:")
    for chunk in named_entities:
        if hasattr(chunk, 'label'):
            print(f"{' '.join(c[0] for c in chunk)}: {chunk.label()}")

    return filtered_words

def display_sign_on_person_feed(gesture_image_path):
    """Overlay sign language images on the live camera feed."""
    cap = cv2.VideoCapture(0)  # Open the default camera
    sign_image = cv2.imread(gesture_image_path)  # Load the sign image

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Calculate the position where the sign image will be placed (above the face)
            x_offset, y_offset = x, y - sign_image.shape[0]
            if y_offset < 0:
                y_offset = 0

            # Overlay the sign image on the frame
            frame[y_offset:y_offset + sign_image.shape[0], x_offset:x_offset + sign_image.shape[1]] = sign_image

        # Display the resulting frame
        cv2.imshow('Sign Language AR', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    """Main loop to continuously capture speech, analyze, and display signs."""
    while True:
        text = speech_to_text()
        if text:
            print("\nText Analysis:")
            filtered_words = analyze_text(text)
            for word in filtered_words:
                if word.lower() in text_to_sign:
                    print(f"Displaying sign for word: {word.lower()}")
                    display_sign_on_person_feed(text_to_sign[word.lower()])
                else:
                    print(f"No sign language gesture found for the word: {word.lower()}")

if __name__ == "__main__":
    main()
