const display = async () =>{

var buyButton = document.getElementById("submit.buy-now-announce")
emissionData = await getEmissions()
buyButton.textContent = emissionData.emissions.co2e + " kg of Carbon Dioxide"

var b = document.getElementsByTagName('body');
b.innerHTML = b.innerHTML + "<div id=\"display\"><div id = \"header\">Amber</div><div id = \"main\">Buyers Impact: 2 Kilos of Carbon Dioxide</div></div>";

}

display()

