const collectPoductCompany = () => {
  companyName = null;
  if (document.getElementById("bylineInfo")) {
    tentativeName = document.getElementById("bylineInfo").textContent;
    if (tentativeName.includes("Visit the")) {
      companyName = tentativeName.slice(10);
    } else if (tentativeName.includes("Brand: ")) {
      console.log("as");
      companyName = tentativeName.slice(tentativeName.indexOf(":") + 2);
    }
  }

  return companyName;
};

const collectProductTitle = () => {
  Title = document.getElementById("productTitle");
  if (Title) {
    productTitle = Title.textContent.trim();
    return productTitle;
  }

  return null;
};

const collectPoductDesc = () => {
  descContainer = document.getElementById("feature-bullets");
  if (descContainer){
  descTags = descContainer.getElementsByClassName("a-list-item");

}
else{
  return
}
  Desc = [];
  for (let i = 0; i < descTags.length; i += 1) {
    Desc.push(descTags[i].textContent.trim());
  }
  console.log(Desc);
  return Desc;
};

const collectProductCost = () => {
  dollarCost = parseInt(
    document.getElementsByClassName("a-price-whole")[0].textContent
  );
  centCost =
    parseInt(
      document.getElementsByClassName("a-price-fraction")[0].textContent
    ) / 100;

  totalCost = dollarCost + centCost;

  return totalCost;
};

const collectProductData = () => {
  productInfo = {
    companyName: "",
    productTitle: "",
    productDesc: "",
    productWeight: "",
    productCost: "",
    shippingFrom: "",
    merchantCountry: "",
  };

  // get Brand name
  productInfo.companyName = collectPoductCompany();

  // Get product Title for AI categorization
  productInfo.productTitle = collectProductTitle();

  // Get Product descriptions for further categorization.
  productInfo.productDesc = collectPoductDesc();

  // Get Product Cost for use in Carbon API unit
  productInfo.productCost = collectProductCost();

  // get Weight, if no weight get dimensions.

  console.log(productInfo);
  return productInfo
};


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
fetch("http://localhost:5000/get_emissions", {
  method: "POST",

  headers: {
    'Content-Type': "application/json",
    'Access-Control-Allow-Headers': Accept

  },
  body:{
    data: data
  }
}).then((serverTest) => {
  console.log(serverTest)
});



