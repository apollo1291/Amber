const getEmissions = async () => {
  // collectProductData should vary based on which online site is currently in use.
  // content scripts should run the file that defines collectProductData based on the url
  data = collectProductData();

  console.log(data);

  response = await fetch("http://localhost:5000/get_emissions", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
      origin: "*",
    },
    body: JSON.stringify(data),
  });
  emissionData = await response.json();
  console.log(emissionData);

  return emissionData;
};
