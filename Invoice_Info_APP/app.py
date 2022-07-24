from flask import Flask
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

invoicefile = "database/invoice.json"
with open(invoicefile, "r") as f:
    invoices = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return ({
        "uri": "/",
        "subresource_uris": {
            "invoice": "/invoice",
            "invoices": "/invoices/Invoice_Number",
            "pending": "/pending",
            "pendings": "/pending/<invoice_amount>",
            "processed": "/processed",
            "process": "/processed/<date>"
        }
    })


@app.route("/invoice", methods=['GET'])
def invoice_list():
    return (invoices)


pendingfile = "database/invoice_pending.json"
with open(pendingfile, "r") as f:
    pending = json.load(f)


@app.route("/pending/<client_name>", methods=['GET'])
def pending_info(client_name):
    if client_name not in pending:
        raise NotFound

    result = pending[client_name]
    result["uri"] = "/pending/{}".format(client_name)

    return (result)

@app.route("/pending", methods=['GET'])
def pending_record():
    return (pending)

paidfile = "database/invoice_paid.json"
with open(paidfile, "r") as f:
    processed = json.load(f)


@app.route("/processed", methods=['GET'])
def processed_list():
    return (processed)


@app.route("/processed/<date>", methods=['GET'])
def processed_record(date):
    if date not in processed:
        raise NotFound
    return (processed[date])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")