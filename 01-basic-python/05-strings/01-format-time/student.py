def format_time(hours, minutes, seconds):
    if hours < 10:
        hours = "0"+str(hours)

    if minutes < 10:
        minutes = "0"+str(minutes)
    
    if seconds < 10:
        seconds = "0"+str(seconds)
    
    return f'{hours}:{minutes}:{seconds}'