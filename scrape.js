const collectPodructCompany = () =>{

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
}

return companyName
}

const collectProductTitle = () => {
    Title = document.getElementById("productTitle")
    if (Title){
        productTitle = Title.textContent
    }

    return productTitle
}

const collectProductData = () =>{
    
    procuctInfo = {
    companyName: "",
    procuctTitle: "",
    productWeight: "",
    shippingFrom: "",
    merchantCountry: "",
}

// get Brand name  
    procuctInfo.companyName = collectPodructCompany()

// Get product Title for AI categorization
Title = document.getElementById("productTitle")
if (Title){
    productTitle = Title.textContent
}

console.log(productTitle)

// get Weight, if no weight get dimensions. 

console.log(collectPodructTitle())
console.log(companyName)

}



collectProductData()