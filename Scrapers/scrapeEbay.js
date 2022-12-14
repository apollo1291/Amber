const collectPoductCompany = () => {
    companyName = null;
    if (document.getElementById("bylineInfo")) {
      tentativeName = document.getElementById("bylineInfo").textContent;
      if (tentativeName.includes("Visit the")) {
        companyName = tentativeName.slice(10);
      } else if (tentativeName.includes("Brand: ")) {
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
  const collectPoductCategory = () => {
    try {
      Searchbox = document.getElementById("searchDropdownBox");
      options = Searchbox.children;
      // options is an html collection
      for (let i = 0; i < options.length; i += 1) {
        try {
          if (options[i].getAttribute("selected")) {
            console.log(options[i].textContent);
            cat = options[i].textContent;
            return cat;
          }
        } catch (err) {
          continue;
        }
      }
    } catch (err) {
      console.log(err);
      return;
    }
  };
  const collectPoductDesc = () => {
    try {
      descContainer = document.getElementById("feature-bullets");
      descTags = descContainer.getElementsByClassName("a-list-item");
    } catch (err) {
      return;
    }
  
    Desc = [];
    for (let i = 0; i < descTags.length; i += 1) {
      Desc.push(descTags[i].textContent.trim());
    }
    return Desc;
  };
  
  const collectProductCost = () => {
    try {
      dollarCost = parseInt(
        document.getElementsByClassName("a-price-whole")[0].textContent
      );
      centCost =
        parseInt(
          document.getElementsByClassName("a-price-fraction")[0].textContent
        ) / 100;
  
      totalCost = dollarCost + centCost;
  
      return totalCost;
    } catch (err) {
      return;
    }
  };
  
  const collectProductData = () => {
    productInfo = {
      companyName: "",
      productTitle: "",
      productDesc: "",
      productWeight: "",
      productCost: "",
      shippingFrom: "",
      Category: "",
    };
  
    // get Brand name
    productInfo.companyName = collectPoductCompany();
  
    // Get product Title for AI categorization
    productInfo.productTitle = collectProductTitle();
  
    // Get Product descriptions for further categorization.
    productInfo.productDesc = collectPoductDesc();
  
    // Get Product Cost for use in Carbon API unit
    productInfo.productCost = collectProductCost();
  
    // get the category of the product
    productInfo.Category = collectPoductCategory();
  
    return productInfo;
  };
  