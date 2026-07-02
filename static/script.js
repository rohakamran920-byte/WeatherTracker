```javascript
// Welcome message
console.log("Welcome to WeatherTracker");

// Check if city field is empty
function validateForm(){

    let city = document.getElementsByName("city")[0].value;

    if(city.trim() === ""){

        alert("Please enter a city name.");

        return false;
    }

    return true;
}

// Refresh page
function refreshWeather(){

    location.reload();

}
```
