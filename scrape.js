const collectPoductCompany = () =>{
    companyName = null
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
        productTitle = Title.textContent.strip()
        return productTitle
    }

    return null
}

const collectProductData = () => {

    productInfo = {
    companyName: "",
    productTitle: "",
    productWeight: "",
    shippingFrom: "",
    merchantCountry: "",
}

// get Brand name  
    productInfo.companyName = collectPoductCompany()

// Get product Title for AI categorization
    productInfo.productTitle = collectProductTitle()



// get Weight, if no weight get dimensions. 

console.log(productInfo)

}



collectProductData()