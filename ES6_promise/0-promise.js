function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      // Replace with your API call or async operation
  
      // Simulated response for testing:
      setTimeout(() => {
        resolve("Sample API response data");
      }, 2000); // Simulating a 2-second delay
    });
  }
  
  export default getResponseFromAPI;
  