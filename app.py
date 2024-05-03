from flask import Flask, render_template, request, redirect, url_for, session
from Nmapscanner import nmapscan
from gobusterscanner import run_gobuster

app = Flask(__name__, template_folder='templates')
app.secret_key = 'key'

@app.route("/", methods=["GET","POST"])
def home():
  return render_template("home.html")

@app.route("/scan", methods=["GET", "POST"])
def scan():
  if request.method == "GET":
      return render_template("index.html")
  elif request.method == "POST":
    ip_addr = request.form.get("ip_addr", "")  # Get the IP address from the form
    if not ip_addr:
      return render_template("index.html", error_message="Please enter an IP address to scan.")
    try:
      from ipaddress import IPv4Address
      IPv4Address(ip_addr)
    except ValueError:
      return render_template("index.html", error_message="Invalid IP address.")
    
    nmscan_results = nmapscan(ip_addr)  # Call nmapscan with the retrieved IP
    
    if nmscan_results is None:  # Handle exit or invalid IP (handled by nmapscan)
      return render_template("index.html", error_message="Scan cancelled or exited.")
    else:
      session['nmscan_results'] = nmscan_results
      return redirect(url_for("show_nmap_results"))

@app.route("/nmap_results")
def show_nmap_results():
    nmscan_results = session.get('nmscan_results')
    if nmscan_results:
      return render_template("nmap_results.html", nmscan_results=nmscan_results)
    else:
      return redirect(url_for("scan"))

@app.route("/run_gobuster/<ip_addr>", methods=["GET", "POST"])
def execute_gobuster(ip_addr):
  if request.method == "GET":
    goresult = run_gobuster(ip_addr)
    return render_template("gobuster_results.html", goresult=goresult)

if __name__ == "__main__":
  app.run(debug=True)
