const removePopup = () => {
    let popup = document.getElementById("display")

    popup.innerHTML = ""
    popup.remove()
}
const display = async () => {
  emissionData = await getEmissions();

  footprint = Math.round(emissionData.emissions.co2e);
  let popup = document.createElement("div");
  popup.setAttribute("id", "display");
  popup.onclick = removePopup
  popup.innerHTML =
    '<div id = "header">Amber</div><div id = "main">Buyers Impact: Around ' +
    footprint +
    " Kilos of Carbon Dioxide</div>";
  page = document.getElementsByTagName("body")[0];
  console.log(page.isConnected);
  page.appendChild(popup);

  console.log("display run");
  setTimeout(removePopup
    
  , 10000);
};


window.addEventListener("load", display, false);
