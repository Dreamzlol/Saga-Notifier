# SAGA Notifier

This is a Python script that checks for new objects on the [SAGA Hamburg](https://www.saga.hamburg/immobiliensuche) website and sends an email notification to a specified recipient email address if new objects are found.

## Prerequisites

- Python 3.6 or later
- Required Python packages:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone or download the repository.
2. Install the required Python packages by running `pip install -r requirements.txt`.

## Configuration

1. Open `ids.json` and add your email credentials and recipient email address.
2. You can also modify the `url` variable in the `main()` function if you want to check for new objects on a different website.
3. You can change the frequency of the script's checks by modifying the `time.sleep()` function in the `if __name__ == '__main__':` block.

## Usage

To start the script, run the following command in your terminal:

```

python saga_notifier.py

```

The script will start checking for new objects and will send an email notification if any are found. The script will continue to run and check for new objects after the specified interval until it is manually stopped.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
