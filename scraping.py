# Scraping Google Play Store reviews for the TikTok app
import csv

from google_play_scraper import reviews_all, Sort

reviews_data = reviews_all(
    app_id='com.ss.android.ugc.trill',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
)

output_file = 'reviews_tiktok.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in reviews_data:
        writer.writerow([review['content']])