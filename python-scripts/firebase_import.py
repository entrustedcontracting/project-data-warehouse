import firebase_admin, json, psutil, time, polars as pl
from datetime import datetime, date
from firebase_admin import firestore

start_time = time.time()
process = psutil.Process()
start_memory_usage = process.memory_info().rss
start_cpu_usage = process.cpu_percent(interval=1)

cred = firebase_admin.credentials.Certificate("/Users/mattrobinson/Entrusted/proj_data_warehouse/project-data-warehouse/python-scripts/service_account.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

today_date = date.today()
timestamp = datetime.now().timestamp() - (60 * 60)

query = db.collection('clientDocs')
items = [doc.to_dict() for doc in query.stream()]
install_enforms = []
latest_install_enforms = []

# Iterate through Firebase database, extract INSTALL forms, and append them to an empty array.
for item in items:
    if "EnForms" in item:
        for enform in item["EnForms"]:
            if enform["subForm"] == "INSTALL":
                install_enforms.append(enform)

# Iterate through INSTALL forms and extract forms from last hour into an empty array.
for enform in install_enforms:
    if enform["slackTimeStampNum"] >= timestamp:
        latest_install_enforms.append(enform)

# Write the latest INSTALL forms into JSON format.






            
        



# ----
# ----
# insert all business logic above
# ----
# ----
end_memory_usage = process.memory_info().rss
memory_usage = end_memory_usage - start_memory_usage
print("Memory usage: {:.2f} bytes".format(memory_usage))
end_cpu_usage = process.cpu_percent(interval=1)
cpu_usage = end_cpu_usage - start_cpu_usage
print("CPU usage: {:.2f}%".format(cpu_usage))
end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))
