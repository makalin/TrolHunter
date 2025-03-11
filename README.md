# TrolHunter

**TrolHunter** is a Python-based tool designed to detect and identify troll accounts on X (Twitter), with a focus on Turkish-language content. It analyzes user profiles, tweets, and behavior patterns to assign a "troll score," helping you decide whether to block or ignore aggressive accounts attacking your profile.

## Features
- Fetches X user data (followers, following, tweets, account age) using the X API via `tweepy`.
- Performs sentiment analysis on tweets using a multilingual BERT model.
- Detects troll-like behavior with heuristics (e.g., low follower-to-following ratio, excessive posting).
- Includes a customizable list of Turkish troll keywords.
- Outputs results to a CSV file for easy review.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/makalin/TrolHunter.git
   cd TrolHunter
   ```

2. **Install Dependencies**:
   ```bash
   pip install tweepy transformers pandas torch
   ```

3. **Set Up X API Credentials**:
   - Get your API keys from [developer.x.com](https://developer.x.com).
   - Replace the placeholders in `trolhunter.py`:
     ```python
     API_KEY = "your_api_key"
     API_SECRET = "your_api_secret"
     ACCESS_TOKEN = "your_access_token"
     ACCESS_TOKEN_SECRET = "your_access_token_secret"
     ```

## Usage

1. **Edit the Target Users**:
   - Open `trolhunter.py` and update the `target_users` list with X handles you want to analyze:
     ```python
     target_users = ["user1", "user2", "user3"]
     ```

2. **Run the Script**:
   ```bash
   python trolhunter.py
   ```

3. **Check Results**:
   - Results are printed to the console and saved in `troll_detection_results.csv`.
   - Look for the "Is Troll?" column: "Yes" indicates a likely troll.

## Example Output
```
Analyzing user1: Troll (Score: 10)
Analyzing user2: Not a Troll (Score: 3)
Analyzing user3: Troll (Score: 8)
Results saved to troll_detection_results.csv
```

## Customization
- **Troll Keywords**: Expand the `troll_keywords` list in the script with more Turkish terms:
  ```python
  troll_keywords = ["salak", "aptal", "kudur", ...]
  ```
- **Threshold**: Adjust the troll score threshold (default: 8) in the `analyze_user` function.
- **Model**: Swap the sentiment model for a Turkish-specific one (e.g., `dbmdz/bert-base-turkish-cased`).

## Limitations
- Requires an X API account (free tier has rate limits).
- May have false positives/negatives; tweak heuristics for accuracy.
- Sentiment analysis is multilingual but not Turkish-optimized by default.

## Contributing
Feel free to fork, submit issues, or send pull requests! Ideas for improvement:
- Add more advanced NLP for Turkish.
- Implement real-time monitoring.
- Enhance scoring with machine learning.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [tweepy](https://github.com/tweepy/tweepy) and [transformers](https://github.com/huggingface/transformers).
- Inspired by the need to fend off X trolls in Turkish.
