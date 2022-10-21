var buyButton = document.getElementById("submit.buy-now-announce")

emissionData = getEmissions()
buyButton.textContent = emissionData.emissions.co2e