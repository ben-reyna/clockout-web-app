from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            # Get form data
            current_hours = float(request.form['current_hours'])
            max_hours = float(request.form['max_hours'])
            clock_in_str = request.form['clock_in']

            # Parse clock-in time
            clock_in = datetime.strptime(clock_in_str, "%H:%M")
            remaining_hours = max_hours - current_hours

            if remaining_hours <= 0:
                result = "You're already at or over the limit. Make like a tree, and get outta there."
            else:
                remaining_time = timedelta(hours=remaining_hours)
                clock_out = clock_in + remaining_time
                clock_out_str = clock_out.strftime("%I:%M %p")
                result = f"You need to clock out by: {clock_out_str} to stay under {max_hours} hours."

        except Exception as e:
            error = f"Error: {str(e)}. Please check your input."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=False)