function getResponseFromAPI() {
    return new Promise((resolve, reject) => {


      setTimeout(() => {
        resolve('Sample API response data');
      }, 2000);
    });
  }

  export default getResponseFromAPI;
