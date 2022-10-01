
const collectProductData = () =>{
    procuctInfo = {
    companyName: "",
    productWeight: "",
    shippingFrom: "",
    merchantCountry: ""
}

// get Brand name  
if (document.getElementById('bylineInfo')){

tentativeName = document.getElementById('bylineInfo').textContent
if(tentativeName.includes("Visit the")){
    companyName = tentativeName
    .slice(10)
}
else if(tentativeName.includes("Brand: ")){
    console.log('as')
    companyName = tentativeName
    .slice(
        tentativeName.indexOf(':')
    )   
}

// get Weight, if no weight get dimensions. 

console.log(companyName)

}

}

collectProductData()