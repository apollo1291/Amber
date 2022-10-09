import {collectProductData} from "Scarpers/scrapeAmazon.js"

require("dotenv").config();

productData = collectProductData();

const getEstimate = () => {

    emission = fetch("https://beta3.api.climatiq.io/estimate", {
          "emission_factor": {
                "id": "electricity-energy_source_grid_mix",
                "region": "US-AZ"
              },
          "parameters": {
                "energy": 90,
                "energy_unit": "kWh"
              },
          
      'headers': {
        'Authorization': "Bearer " + Process.env.MY_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST"
    })

    return emission
}

data = collectProductData()
console.log(data)
serverTest = fetch("http://localhost:5000/get_emissions", {
  method: "POST",

  headers: {
    'Content-Type': "application/json"
  },
  body:{
    data: data
  }
})

console.log(serverTest)

