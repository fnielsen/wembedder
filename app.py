"""Script to start webserving."""


from wembedder.app import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
