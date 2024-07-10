from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Route for displaying the form
@app.route('/')
def form():
    """
    This function renders the HTML form.
    """
    return render_template('form.html')

# Route for handling the form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    """
    This function handles the form submission.
    It processes the form data and redirects the user to a success page.
    """
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Here you can add code to process the form data, such as saving it to a database

    # Redirect to a success page (or render a success template)
    return redirect(url_for('success'))

# Route for displaying the success page
@app.route('/success')
def success():
    """
    This function renders the success page after form submission.
    """
    return "Form submitted successfully!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
