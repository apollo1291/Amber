

data = collectProductData()

console.log(data)

fetch("http://localhost:5000/get_emissions", {
  method: "POST",

  headers: {
    'Content-Type': "application/json",
    'origin': '*'

  },
  body: JSON.stringify( data )
}).then((serverTest) => {
  serverTest.json().then((serverBody) => {
    console.log(serverBody)
  })
});



