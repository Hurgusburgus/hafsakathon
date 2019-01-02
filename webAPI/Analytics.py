from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os
from os.path import dirname, realpath


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
GRANDPARENT_FOLDER = dirname(dirname(dirname(realpath(__file__))))  # dir contains the project
KEY_FILE_LOCATION = GRANDPARENT_FOLDER + os.sep + 'client_secrets.json'
VIEW_ID = '187139795'


def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
    An authorized Analytics Reporting API V4 service object.
    """
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            KEY_FILE_LOCATION, SCOPES)
    except FileNotFoundError:
        print('Private key for analytics api not found')
        return -1

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics=initialize_analyticsreporting(), days=7, metrics=['ga:sessions'], dimensions=None):
    """Queries the Analytics Reporting API V4.

    Args:
    analytics: An authorized Analytics Reporting API V4 service object.
    days: Number of days the report will include (up until current date).
    metrics: The metrics the report will include.
    dimensions: The dimensions the report will include.
    (metrics and dimensions names: https://developers.google.com/analytics/devguides/reporting/core/dimsmets)
    Returns:
    The Analytics Reporting API V4 response.
    """
    if analytics == -1:
        return None
    date_range = str(int(days)) + 'daysAgo'
    metrics = [{'expression': m} for m in metrics]
    if dimensions:
        dimensions = [{'name': d} for d in dimensions]
        return analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': VIEW_ID,
                        'dateRanges': [{'startDate': date_range, 'endDate': 'today'}],
                        'metrics': metrics,
                        'dimensions': dimensions
                    }]
            }
        ).execute()

    return analytics.reports().batchGet(
        body={
            'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': date_range, 'endDate': 'today'}],
                'metrics': metrics
            }]
            }
                    ).execute()
