import tweepy
from transformers import pipeline
import re
import pandas as pd
from datetime import datetime, timedelta

# Your X API credentials (replace with your own)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Authenticate with X API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Load a pre-trained sentiment analysis model (multilingual, works with Turkish)
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Turkish keywords commonly associated with trolling (expand this list as needed)
troll_keywords = [
    "salak", "aptal", "sahtekar", "yalancı", "terbiyesiz", 
    "kudur", "bela", "rezil", "trol", "provokasyon",
    "geri zekalı", "şerefsiz", "korkak", "palavracı", "haysiyetsiz",
    "köpek", "it", "çakal", "yavşak", "alçak",
    "boş yapma", "sus lan", "hadi oradan", "sen kimsin", "ağzını topla",
    "kafa bulma", "dalga geçme", "sataşma", "bana bulaşma", "işine bak",
    "zırvalama", "saçmalama", "atıp tutma", "yemezler", "numara yapma",
    "kışkırtma", "fitneci", "dedikoducu", "fasa fiso", "uydurma",
    "bırak bu işleri", "gaza gelme", "artistlik yapma", "havlama", "safsata"
]

def clean_text(text):
    """Clean text by removing URLs, mentions, and special characters."""
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

def analyze_user(user_handle):
    """Analyze an X user profile for troll-like behavior."""
    try:
        # Fetch user info
        user = api.get_user(screen_name=user_handle)
        
        # Get recent tweets (up to 50)
        tweets = api.user_timeline(screen_name=user_handle, count=50, tweet_mode="extended")
        
        # Extract user metrics
        follower_count = user.followers_count
        following_count = user.friends_count
        account_age = (datetime.now() - user.created_at).days
        tweet_count = user.statuses_count
        
        # Analyze tweet content
        troll_score = 0
        tweet_texts = [clean_text(tweet.full_text) for tweet in tweets if hasattr(tweet, 'full_text')]
        
        # Sentiment analysis on tweets
        for text in tweet_texts:
            if text:  # Skip empty texts
                sentiment = sentiment_analyzer(text)[0]
                # Negative sentiment might indicate aggression
                if sentiment["label"] == "NEGATIVE" and sentiment["score"] > 0.8:
                    troll_score += 1
                
                # Check for troll keywords
                if any(keyword in text.lower() for keyword in troll_keywords):
                    troll_score += 2
        
        # Calculate ratios and heuristics
        follower_following_ratio = follower_count / max(following_count, 1)  # Avoid division by zero
        tweets_per_day = tweet_count / max(account_age, 1)
        
        # Scoring logic (tweak thresholds based on testing)
        if follower_following_ratio < 0.1:  # Very few followers compared to following
            troll_score += 3
        if tweets_per_day > 10:  # Excessive posting
            troll_score += 2
        if account_age < 30:  # Very new account
            troll_score += 3
        if "bot" in user.description.lower() or "trol" in user.description.lower():
            troll_score += 4
        
        # Final decision (threshold of 8, adjust as needed)
        is_troll = troll_score >= 8
        
        # Prepare result
        result = {
            "Username": user_handle,
            "Troll Score": troll_score,
            "Is Troll?": "Yes" if is_troll else "No",
            "Follower/Following Ratio": follower_following_ratio,
            "Tweets per Day": tweets_per_day,
            "Account Age (days)": account_age,
            "Sample Tweets": tweet_texts[:3]  # Show first 3 tweets for reference
        }
        
        return result
    
    except tweepy.TweepError as e:
        return {"Username": user_handle, "Error": str(e)}

def main():
    # Example usage: input a list of usernames attacking your account
    target_users = ["user1", "user2", "user3"]  # Replace with actual handles
    
    results = []
    for user in target_users:
        result = analyze_user(user)
        results.append(result)
        print(f"Analyzing {user}: {'Troll' if result.get('Is Troll?') == 'Yes' else 'Not a Troll'} "
              f"(Score: {result.get('Troll Score', 0)})")
    
    # Save results to a CSV for review
    df = pd.DataFrame(results)
    df.to_csv("troll_detection_results.csv", index=False)
    print("Results saved to troll_detection_results.csv")

if __name__ == "__main__":
    main()