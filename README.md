# Uptime-Kuma Status Page Integration with LINE Bot

This project integrates Uptime-Kuma status page data with a LINE Bot. The bot analyzes the status page data using Google Gemini Pro and sends relevant information to the appropriate departments via LINE.

## Table of Contents

- [Uptime-Kuma Status Page Integration with LINE Bot](#uptime-kuma-status-page-integration-with-line-bot)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
    - [line\_controller.py](#line_controllerpy)
    - [kuma\_controller.py](#kuma_controllerpy)
    - [api.py](#apipy)
  - [License](#license)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/louis70109/line-bot-status-analyze.git
   cd line-bot-status-analyze
   ```

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up your environment variables. You can use a `.env` file for this:

   ```sh
   cp .env.example .env
   ```

4. Update the `.env` file with your configuration values:
   ```ini
   LINE_CHANNEL_SECRET=your_line_channel_secret
   LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
   ADMIN_LINE_ID=your_admin_line_id
   ```

## Configuration

- **LINE_CHANNEL_SECRET**: Your LINE channel secret.
- **LINE_CHANNEL_ACCESS_TOKEN**: Your LINE channel access token.
- **ADMIN_LINE_ID**: The LINE ID of the admin who will receive the messages.

## Usage

1. Run the application:

   ```sh
   python api.py
   ```

2. The application will be available at `http://localhost:8080`.

3. Use the following endpoints:
   - `POST /webhooks/line`: Endpoint for LINE webhook events.
     - If you want to use LINE bot, please using the `SSL domain`.
   - `POST /kuma`: Endpoint to receive Uptime-Kuma status page data.
   - `GET /kuma`: Endpoint to fetch and analyze Uptime-Kuma status page data.

## Project Structure

```plaintext
.
├── api.py
├── controller
│   ├── line_controller.py
│   └── kuma_controller.py
├── utils
│   ├── configmap.py
│   ├── gemini_service.py
│   ├── line_service.py
│   ├── kuma_service.py
│   └── logging_config.py
├── .env.example
├── requirements.txt
└── README.md
```

### line_controller.py

Handles LINE webhook events and processes messages containing the !bot command.

### kuma_controller.py

Processes Uptime-Kuma status page data, analyzes it using Google Gemini Pro, and sends the relevant information to the LINE bot.

### api.py

Main entry point of the application, sets up routes and initializes the Flask application.

## License

This project is licensed under the MIT License.
