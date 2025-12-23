def seo_row_to_text(row):
    return (
        f"SEO Data:\n"
        f"URL: {row['url']}\n"
        f"Query: {row['query']}\n"
        f"Clicks: {row['clicks']}\n"
        f"Impressions: {row['impressions']}\n"
        f"CTR: {row['ctr']}\n"
        f"Average Position: {row['position']}"
    )


def analytics_row_to_text(row):
    return (
        f"Analytics Data:\n"
        f"Page: {row['page_path']}\n"
        f"Sessions: {row['sessions']}\n"
        f"Bounce Rate: {row['bounce_rate']}\n"
        f"Avg Session Duration: {row['avg_session_duration']} sec\n"
        f"Conversions: {row['conversions']}"
    )
