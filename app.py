from flask import Flask, request, render_template



# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------
@app.route('/')
def main():
        
    return render_template("index.html")

@app.route('/getcsv')
def getcsv():
    return render_template("CSV_input.html")

@app.route('/capture_packets')
def capture_packets():
    return render_template("capture_packets.html")
        
@app.route('/pcap_kdd')
def pcap_kdd():
    return render_template("pcap_kdd.html")

@app.route('/About')
def About():
    return render_template("About.html")
    

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
