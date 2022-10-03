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
        productTitle = Title.textContent.trim()
        return productTitle
    }

    return null
}

const collectPoductDesc = () => {
    descContainer = document.getElementById("feature-bullets")
    descTags = descContainer.getElementsByClassName("a-list-item")
    Desc = []
    for(let i = 0; i < descTags.length; i += 1){
        Desc.push(descTags[i].textContent.trim())
    }
    console.log(Desc)
    return Desc

}

const collectProductData = () => {

    productInfo = {
    companyName: "",
    productTitle: "",
    productDesc: "",
    productWeight: "",
    shippingFrom: "",
    merchantCountry: "",
}

// get Brand name  
    productInfo.companyName = collectPoductCompany()

// Get product Title for AI categorization
    productInfo.productTitle = collectProductTitle()

// Get Product descriptions for further categorization.
    productInfo.productDesc = collectPoductDesc()



// get Weight, if no weight get dimensions. 

console.log(productInfo)

}



collectProductData()