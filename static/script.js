var oXHR = new XMLHttpRequest();


oXHR.onreadystatechange = reportStatus;
oXHR.open("GET", "./static/puckdata.json", true);
oXHR.send();



function reportStatus() {
    if (oXHR.readyState == 4) {		
        document.getElementById('uptime').innerHTML = JSON.parse(this.responseText).uptime;
  }
}