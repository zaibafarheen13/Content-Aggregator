from flask import Flask, request, render_template

class TextGenerator:
    """
    A class to generate text.

    Attributes:
        text (str): The input text to generate.

    Methods:
        generate(): Generate the input text.
    """
    def __init__(self, text):
        self.text = text

    def generate(self):
        """
        Generate the input text.

        Returns:
            str: The generated text.
        """
        assert isinstance(self.text, str), "Input text must be a string"
        return self.text

class FileGenerator(TextGenerator):
    """
    A class to generate text file.

    Attributes:
        text (str): The input text to generate.
        filename (str): The name of the file to be generated.

    Methods:
        generate(): Generate the input text file.
    """
    def __init__(self, text, filename):
        super().__init__(text)
        self.filename = filename

    def generate(self):
        """
        Generate the input text file.

        Raises:
            AssertionError: If filename is not a string.

        Returns:
            None.
        """
        assert isinstance(self.filename, str), "Filename must be a string"
        with open(self.filename, "w") as f:
            f.write(self.text)
class Feed:
    @staticmethod
    def feed():
        wiki_url = '/wiki'
        weather_url = '/weather'
        news_url = '/news'
        home_url = '/'
        feed_url = '/feed'
        """
        Generate text file from the input text.

        Returns:
            str: A message indicating the success or error message.
        """
        message = ""
        if request.method == 'POST':
            try:
                text = request.form['text']
                name = request.form['name']
                assert text != "" and name != "", "Input fields cannot be empty"
                file_generator = FileGenerator(text, f"{name}.txt")
                file_generator.generate()
                message = f"Feed '{name}' generated successfully!"
            except AssertionError as e:
                message = f"Error: {e}"
            except Exception as e:
                message = f"An error occurred: {e}"
        
        return render_template('feed.html', message=message,  home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url, feed_url=feed_url)
