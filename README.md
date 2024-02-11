# Automatic Rain Alert System

This is a simple Python script that provides an automatic rain alert based on weather forecast data. The script utilizes the OpenWeatherMap API to fetch weather information for a specified location and uses Twilio to send an SMS alert if rain is forecasted.

## Getting Started

### Prerequisites

Before running the script, you need to have the following:

- OpenWeatherMap API Key: Get your API key by signing up at [OpenWeatherMap](https://openweathermap.org/).
- Twilio Account SID and Auth Token: Obtain these credentials by signing up at [Twilio](https://www.twilio.com/).

### Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Sakib-Dalal/Automatic_Rain_Alert.git
    ```

2. Install required packages:

    ```bash
    pip install requests twilio
    ```

3. Open `main.py` and replace the placeholder values with your OpenWeatherMap API key, Twilio credentials, and receiver's phone number.

## Usage

Run the script by executing:

```bash
python main.py
```

The script will check the weather forecast for the specified location and send an SMS alert if rain is forecasted.

## Configuration

- **API_KEY**: Your OpenWeatherMap API key.
- **URL**: OpenWeatherMap API endpoint for forecast data.
- **SID**: Your Twilio Account SID.
- **TOKEN**: Your Twilio Auth Token.
- **P_NUM**: Your Twilio phone number.
- **MY_LAT**, **MY_LNG**: Latitude and longitude of the location for weather forecast.
- **parameters**: Additional parameters for the OpenWeatherMap API request.

## Contributing

Feel free to contribute to improve this project. Create a pull request or open an issue to discuss potential changes.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace placeholder values and customize the content as needed.
