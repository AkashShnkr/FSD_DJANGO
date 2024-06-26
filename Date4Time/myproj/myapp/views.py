from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def date_time_view(request):
    # Get the current date and time
    now = datetime.now()
    
    # Calculate the time 4 hours ahead
    time_ahead = now + timedelta(hours=4)
    
    # Calculate the time 4 hours before
    time_before = now - timedelta(hours=4)
    
    # Create the HTML response
    html = """
    <html>
        <body>
            <p>Current date and time: {0}</p>
            <p>Four hours ahead: {1}</p>
            <p>Four hours before: {2}</p>
        </body>
    </html>
    """.format(now, time_ahead, time_before)
    
    # Return the HTTP response
    return HttpResponse(html)
