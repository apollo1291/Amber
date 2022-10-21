var buyButton = document.getElementById("buy-now-button")

emissionData = getEmissions()
buyButton.textContent = emissionData.emissions.co2e