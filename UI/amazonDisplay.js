const display = async () =>{

var buyButton = document.getElementById("submit.buy-now-announce")
emissionData = await getEmissions()
buyButton.textContent = emissionData.emissions.co2e

}