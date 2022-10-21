
const getEmissions = () =>{
  
  // collectProductData should vary based on which online site is currently in use. 
  // content scripts should run the file that defines collectProductData based on the url 
  data = collectProductData()

console.log(data)

fetch("http://localhost:5000/get_emissions", {
  method: "POST",

  headers: {
    'Content-Type': "application/json",
    'origin': '*'

  },
  body: JSON.stringify( data )
}).then((response) => {
  response.json().then((serverBody) => {
    console.log(serverBody)
    // not defined in the global scope
    var emissionData = serverBody
  })
});

return emissionData
}

getEmissions()



