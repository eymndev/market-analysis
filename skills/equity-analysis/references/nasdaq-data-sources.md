# Nasdaq data sources

## Source priority

1. SEC EDGAR: Forms 10-K, 10-Q, 8-K, Form 4, and other event filings.
2. Official Nasdaq company, historical-price, calendar, short-interest, and market pages.
3. Company investor relations: presentations, earnings releases, transcripts, and guidance.
4. Secondary providers only when their methodology and as-of date are verifiable.

## User-supplied Python package note

The supplied `nasdaq-public-api` 0.2.0 page describes access to profiles, six quarters of revenue and earnings, historical prices, insider transactions, institutional holdings, short interest, earnings calendars, screeners, news, dividends, ratios, option chains, and SEC filings.

The package requires Python 3.12+, Chrome, and Selenium/ChromeDriver, and its page labels the project Alpha. Cookie automation and unofficial public endpoints can be affected by Nasdaq changes, rate limits, browser updates, and terms of service. Do not install it unless the user explicitly asks. When used:

- verify the current version and source repository;
- comply with rate limits and terms;
- confirm critical fundamentals against SEC or company filings;
- test whether prices are adjusted;
- report browser or cookie failures as missing data, never as zero values.
