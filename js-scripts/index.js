const admin = require("firebase-admin");
const fs = require("fs");
const process = require("process");
const { DateTime } = require("luxon");

const serviceAccount = require("./service_account.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const db = admin.firestore();

const startTime = process.hrtime();
const startMemoryUsage = process.memoryUsage().heapTotal;
const startCpuUsage = process.cpuUsage();

const timestamp = DateTime.now().minus({ hours: 1 }).toJSDate();
const storageTime =
  DateTime.fromJSDate(timestamp).toFormat("yyyy-MM-dd-HH:mm");

const query = db.collection("clientDocs");
const items = [];

query
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
      items.push(doc.data());
    });
      
    const installEnforms = [];
    const latestInstallEnforms = [];

    // Iterate through Firebase database, extract INSTALL forms, and append them to an empty array.
    items.forEach((item) => {
      if (item.EnForms) {
        item.EnForms.forEach((enform) => {
          if (enform.subForm === "INSTALL") {
            installEnforms.push(enform);
          }
        });
      }
    });

    // Iterate through INSTALL forms and extract forms from last hour into an empty array.
    installEnforms.forEach((enform) => {
      if (enform.slackTimeStampNum >= (timestamp.getTime() / 1000)) {
        latestInstallEnforms.push(enform);
      }
    });
    console.log(latestInstallEnforms)

    // Write the latest INSTALL forms into JSON format.
    const jsonData = JSON.stringify(latestInstallEnforms, null, 4);
    fs.writeFileSync(`js-scripts/latest_install_enforms-${storageTime}.json`, jsonData);

    const endMemoryUsage = process.memoryUsage().heapTotal;
    const memoryUsage = endMemoryUsage - startMemoryUsage;
    console.log(`Memory usage: ${memoryUsage} bytes`);

    const endCpuUsage = process.cpuUsage();
    const cpuUsageMicros = endCpuUsage.user - startCpuUsage.user;
    const cpuUsage = cpuUsageMicros / 1000000; // Convert to seconds
    console.log(`CPU usage: ${cpuUsage.toFixed(2)}%`);

    const endTime = process.hrtime(startTime);
    const executionTime = endTime[0] + endTime[1] / 1e9;
    console.log(`Execution time: ${executionTime.toFixed(2)} seconds`);
  })
  .catch((error) => {
    console.error("Error getting documents:", error);
  });
